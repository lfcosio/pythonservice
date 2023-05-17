import abc
from uuid import UUID

from app.entities.entities import Customer

CustomerId= UUID


class CustomerRepository(metaclass=abc.ABCMeta):
    """An interface to listing repository"""

    @abc.abstractmethod
    def add(self, entity: Customer):
        """Adds new entity to a repository"""
        raise NotImplementedError()

    @abc.abstractmethod
    def remove(self, entity: Customer):
        """Removes existing entity from a repository"""
        raise NotImplementedError()

    @abc.abstractmethod
    def get_by_id(self, customer_id: CustomerId) -> Customer:
        """Retrieves entity by its identity"""
        raise NotImplementedError()

    def __getitem__(self, index) -> Customer:
        return self.get_by_id(index)
