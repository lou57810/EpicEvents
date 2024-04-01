from typing import List
import datetime
from enum import Enum as PyEnum

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, String, DateTime, Column, types
from sqlalchemy.sql import func
from .base import Base
from .user import User
from .customer import Customer
# from .event import Event


class SignEnum(PyEnum):
    SIGNED = "SIGNED"
    UNSIGNED = "UNSIGNED"


class Contract(Base):

    __tablename__ = "contracts"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    customer_info: Mapped[int] = mapped_column(ForeignKey("customers.id"))

    # Relation with collaborator:
    commercial_contact: Mapped[int] = mapped_column(ForeignKey("users.id"))
    user: Mapped["User"] = relationship(back_populates="contracts_map")

    # Relation with customer:
    customer: Mapped["Customer"] = relationship(
        back_populates="contracts_maps")
    # Relation with event:
    event_map: Mapped[List["Event"]] = relationship(back_populates='contract')
    #events = relationship("Event",
    #           back_populates='contract', cascade="all, delete-orphan")

    total_amount: Mapped[int] = mapped_column(String(150), nullable=False)
    balance_payable: Mapped[int] = mapped_column(String(150), nullable=False)
    start_date: Mapped[datetime.date] = mapped_column(
        DateTime(timezone=True), server_default=func.now())
    contract_status = Column(types.Enum(SignEnum,
                             values_callable=lambda obj:
                             [e.value for e in obj]))

    def __init__(self, customer_info,
                 commercial_contact, total_amount,
                 balance_payable, start_date, contract_status):
        self.customer_info = customer_info
        self.commercial_contact = commercial_contact
        self.total_amount = total_amount
        self.balance_payable = balance_payable
        self.start_date = start_date
        self.contract_status = contract_status

    def __repr__(self):
        return f"({self.customer_info} {self.commercial_contact}\
                  {self.total_amount} {self.balance_payable}\
                  {self.start_date} {self.contract_status})"
