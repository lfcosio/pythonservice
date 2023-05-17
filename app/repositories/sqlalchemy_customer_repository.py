from sqlalchemy.orm import Session

from .data_mapper import customer_entity_to_model, customer_model_to_entity
from .entities.entities import Customer
from .models.models import CustomerModel
from .repositories.customer_repository import CustomerRepository

# a sentinel value for keeping track of entities removed from the repository
REMOVED = object()


class SqlAlchemyCustomerRepository(CustomerRepository):
    """SqlAlchemy implementation of ListingRepository"""

    def __init__(self, session: Session, identity_map=None):
        self.session = session
        self._identity_map = identity_map or dict()

    def add(self, entity: Customer):
        self._identity_map[entity.id] = entity
        instance = customer_entity_to_model(entity)
        self.session.add(instance)

    def remove(self, entity: Customer):
        self._check_not_removed(entity)
        self._identity_map[entity.id] = REMOVED
        listing_model = self.session.query(CustomerModel).get(entity.id)
        self.session.delete(listing_model)

    def get_by_id(self, id):
        instance = self.session.query(CustomerModel).get(id)
        return self._get_entity(instance)

    def get_by_name(self, name):
        instance = self.session.query(CustomerModel).filter_by(name=name).one()
        return self._get_entity(instance)

    def _get_entity(self, instance):
        if instance is None:
            return None
        entity = customer_model_to_entity(instance)
        self._check_not_removed(entity)

        if entity.id in self._identity_map:
            return self._identity_map[entity.id]

        self._identity_map[entity.id] = entity
        return entity

    def __getitem__(self, key):
        return self.get_by_id(key)

    def _check_not_removed(self, entity):
        assert self._identity_map.get(entity.id, None) is not REMOVED, f"Entity {entity.id} already removed"

    def persist(self, entity: Customer):
        self._check_not_removed(entity)
        assert entity.id in self._identity_map, "Cannot persist entity which is unknown to the repo. Did you forget " \
                                                "to call repo.add() for this entity?"
        instance = customer_entity_to_model(entity)
        merged = self.session.merge(instance)
        self.session.add(merged)

    def persist_all(self):
        for entity in self._identity_map:
            if entity is not REMOVED:
                self.persist(entity)
