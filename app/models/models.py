from uuid import UUID
from sqlalchemy import Column, String
from sqlalchemy.orm import declarative_base
Base = declarative_base()


class CustomerModel(Base):
    customer_id = Column(UUID(as_uuid=True), primary_key=True)
    first_name = Column(String(150))
    last_name = Column(String(150))
    dob = Column(String(150))
    street_addr = Column(String(150))
    country = Column(String(150))
    phone_number = Column(String(150))
