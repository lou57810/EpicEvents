import datetime
from typing import List

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, String, Date
from sqlalchemy.sql import func
from .base import Base
# from .user import User
# from .contract import Contract


class Customer(Base):

    __tablename__ = "customers"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    full_name: Mapped[str] = mapped_column(String(150), nullable=False)
    customer_email: Mapped[str] = mapped_column(
        String(150), nullable=False, unique=True)
    tel: Mapped[str] = mapped_column(String(150), nullable=False, unique=True)
    company_name: Mapped[str] = mapped_column(String(150), nullable=False)
    # first_date: Mapped[datetime.date] = mapped_column(Date(), server_default=func.now())
    # last_date: Mapped[datetime.date] = mapped_column(Date(), server_default=func.now())
    first_date: Mapped[datetime.date] = mapped_column(Date())
    last_date: Mapped[datetime.date] = mapped_column(Date())
    # default=datetime.datetime.utcnow
    # Relation with collaborator:
    contact: Mapped[int] = mapped_column(ForeignKey("users.id"))
    user: Mapped["User"] = relationship(back_populates="customers_map")

    # Relation contract
    contracts_maps: Mapped[List["Contract"]] = relationship(
        back_populates='customer', cascade="all, delete-orphan")

    def __init__(self, id, full_name,
                 customer_email, tel, company_name,
                 first_date, last_date, contact):
        self.id = id
        self.full_name = full_name
        self.customer_email = customer_email
        self.tel = tel
        self.company_name = company_name
        self.first_date = first_date
        self.last_date = last_date
        self.contact = contact

    def __repr__(self):
        return f"Customer(full_name={self.full_name!r},\
                customer_email={self.customer_email!r},\
                tel={self.tel!r},\
                company_name={self.company_name!r},\
                first_date={self.first_date!r},\
                last_date={self.last_date!r},\
                contact={self.contact!r})"
