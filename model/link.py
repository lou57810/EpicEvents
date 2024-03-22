from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from .user import User
from .customer import Customer
from .contract import Contract
from .event import Event
from sqlalchemy.orm import Mapped, DeclarativeBase
from sqlalchemy.orm.decl_api import mapped_column
from typing import List

class Base(DeclarativeBase):
    pass


class Link(Base):
    __tablename__ = 'links'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey('users.id'))
    customer_id: Mapped[int] = mapped_column(Integer, ForeignKey('customers.id'))
    contract_id: Mapped[int] = mapped_column(Integer, ForeignKey('contracts.id'))
    event_id: Mapped[int] = mapped_column(Integer, ForeignKey('events.id'))

    user: Mapped[User] = relationship("User")
    customer: Mapped[Customer] = relationship("Customer", back_populates="links")
    contract: Mapped[Contract] = relationship("Contract")
    event: Mapped[Event] = relationship("Event")