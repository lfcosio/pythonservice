from app.models.models import CustomerModel
from app.entities.entities import Customer


def customer_model_to_entity(instance: CustomerModel) -> Customer:

    return Customer(
        first_name=instance.first_name,
        last_name=instance.last_name,
        dob=instance.dob,
        street_addr=instance.street_addr,
        phone_number=instance.phone_number,
        country=instance.country
    )


def customer_entity_to_model(customer: Customer, existing=None) -> CustomerModel:
    return CustomerModel(
        first_name=customer.first_name,
        last_name=customer.last_name,
        dob=customer.dob,
        street_addr=customer.street_addr,
        phone_number=customer.phone_number,
        country=customer.country)
