from app.models.models import Customer


class SqlAlchemyAccessor:

    def __init__(self, db):
        self.db = db

    def create(self, customer):
        if self.fetch_by_name(customer.first_name, customer.last_name) is None:
            return -1
        self.db.session.add(customer)
        self.db.session.commit()
        return customer.customer_id

    def delete(self):
    def update(self):


    def fetch_by_id(customer_id):
        customer = Customer.query.get(customer_id)
        if customer is None:
            return None
        return customer

    def fetch_by_name(self, first_name, last_name):
        customer = Customer.query(Customer).filter(Customer.first_name==first_name, Customer.last_name == last_name).first()
        if customer is None:
            return None
        return customer