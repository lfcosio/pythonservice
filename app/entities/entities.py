from dataclasses import dataclass, field
from datetime import datetime
from uuid import UUID, uuid4


@dataclass
class Customer:
    customer_id: UUID = field(default_factory=uuid4)
    dob: datetime | None = None
    first_name: str | None = None
    last_name: str | None = None
    street_addr: str | None = None
    country: str | None = None
    phone_number: str | None = None
