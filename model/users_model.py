# import os
import enum
from enum import Enum as PyEnum 
# from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import ForeignKey # LargeBinary, 
from sqlalchemy.dialects.mysql import LONGTEXT
import datetime

from typing import List  # Optional    , Literal
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import Column, String, types  # Date, Text,Integer, create_engine, 

from sqlalchemy import DateTime
from sqlalchemy.sql import func
# from sqlalchemy_utils.types.choice import ChoiceType
# import jwt

from typing import List
# GESTION
ADD_USER = "ADD_USER"
UPDATE_USER = "UPDATE_USER"
DELETE_USER = "DELETE_USER"
ADD_CONTRACT = "ADD_CONTRACT"
UPDATE_CONTRACT = "UPDATE_CONTRACT"
DISPLAY_FILTERED_EVENTS = "DISPLAY_FILTERED_EVENTS"
UPDATE_EVENT = "UPDATE_EVENT"
# COMMERCIAL
###########################################
ADD_CUSTOMER = "ADD_CUSTOMER"
UPDATE_OWN_CUSTOMER = "UPDATE_OWN_CUSTOMER"
UPDATE_OWN_CONTRACT = "CREATE_OWN_CONTRACT"
CREATE_SIGNED_OWN_EVENT = "CREATE_SIGNED_OWN_EVENT"
# SUPPORT
###################################################
UPDATE_OWN_EVENT = "UPDATE_OWN_EVENT"
###################################################


class RoleEnum(PyEnum):
    GESTION = "1"
    COMMERCIAL = "2"
    SUPPORT = "3"


class SignEnum(PyEnum):
    SIGNED = "1"
    UNSIGNED = "2"

#  Changer Signed True or False



Permissions_roles = {"1": [ADD_USER, UPDATE_USER, DELETE_USER, ADD_CONTRACT, UPDATE_CONTRACT, DISPLAY_FILTERED_EVENTS, UPDATE_EVENT],
                    "2": [ADD_CUSTOMER, UPDATE_OWN_CUSTOMER, UPDATE_OWN_CONTRACT, CREATE_SIGNED_OWN_EVENT],
                    "3": [UPDATE_OWN_EVENT]
                    }



class Base(DeclarativeBase):
    pass


class User(Base):

    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, unique=True, autoincrement=True)
    username: Mapped[str] = mapped_column(String(120))
    password : Mapped[str] = mapped_column(String(120))
    hashed_pass: Mapped[str] = mapped_column(String(120))
    email: Mapped[str] = mapped_column(String(120), nullable=False, unique=True)
    role = Column(types.Enum(RoleEnum, values_callable=lambda obj: [e.value for e in obj]))

    # Relation: customer, contract, event
    customers_map: Mapped[List["Customer"]] = relationship(back_populates='user', cascade="all, delete-orphan")
    contracts_map: Mapped[List["Contract"]] = relationship(back_populates='user', cascade="all, delete-orphan")
    events_map: Mapped[List["Event"]] = relationship(back_populates='user', cascade="all, delete-orphan")


    def __init__(self, username, password, hashed_pass, email, role):
        self.username = username
        self.password = password
        self.hashed_pass = hashed_pass
        self.email = email
        self.role = role


    def __repr__(self) -> str:
        # return f"({self.username} {self.password} {self.hashed_pass} {self.email} {self.role.value})"
        return f"({self.username} {self.password} {self.hashed_pass} {self.email} {self.role})"



class Customer(Base):
    
    __tablename__ = "customers"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    full_name: Mapped[str] = mapped_column(String(150), nullable=False)
    customer_email: Mapped[str] = mapped_column(String(150), nullable=False, unique=True)
    tel: Mapped[str] = mapped_column(String(150), nullable=False, unique=True)
    company_name: Mapped[str] = mapped_column(String(150), nullable=False)
    first_date: Mapped[datetime.date] = mapped_column(DateTime(timezone=True), server_default=func.now())
    last_date: Mapped[datetime.date] = mapped_column(DateTime(timezone=True), server_default=func.now())

    # Relation with collaborator:
    contact: Mapped[int] = mapped_column(ForeignKey("users.id"))
    user: Mapped["User"] = relationship(back_populates="customers_map")

    # Relation contract
    # contrats_maps: Mapped[List["Customer"]] = relationship(back_populates='customer', cascade="all, delete-orphan")
    contrats_maps: Mapped[List["Contract"]] = relationship(back_populates='customer', cascade="all, delete-orphan")



    def __init__(self, full_name,\
        customer_email, tel, company_name,\
        first_date, last_date, contact):
        
        self.full_name = full_name
        self.customer_email = customer_email
        self.tel = tel
        self.company_name = company_name
        self.first_date = first_date
        self.last_date = last_date
        self.contact = contact

    def __repr__(self):
        return f"({self.full_name} {self.customer_email}\
                {self.tel} {self.company_name} {self.first_date}\
                {self.last_date} {self.contact})"


class Contract(Base):
    
    __tablename__ = "contracts"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    customer_info: Mapped[int] = mapped_column(ForeignKey("customers.id"))  # (ForeignKey("customers.id"))
    # Relation with collaborator:
    commercial_contact: Mapped[int] = mapped_column(ForeignKey("users.id"))

    user: Mapped["User"] = relationship(back_populates="contracts_map")
    # Relation with customer:
    customer: Mapped["Customer"] = relationship(back_populates="contrats_maps")
    # Relation with event:
    # event_id: Mapped[int] = mapped_column(ForeignKey("events.id"))
    # event: Mapped["Event"] = relationship(back_populates="contrat")
    event_map: Mapped[List["Event"]] = relationship(back_populates='contract')
    # events_map: Mapped[List["Event"]] = relationship(back_populates='user', cascade="all, delete-orphan")

    total_amount: Mapped[int] = mapped_column(String(150), nullable=False)
    balance_payable: Mapped[int] = mapped_column(String(150), nullable=False)
    start_date: Mapped[datetime.date] = mapped_column(DateTime(timezone=True), server_default=func.now())
    contract_status = Column(types.Enum(SignEnum, values_callable=lambda obj: [e.value for e in obj]))


    def __init__(self, customer_info,\
        commercial_contact, total_amount,\
        balance_payable, start_date, contract_status):
        self.customer_info = customer_info
        self.commercial_contact = commercial_contact
        self.total_amount = total_amount
        self.balance_payable = balance_payable
        self.start_date = start_date
        self.contract_status = contract_status

    def __repr__(self):
        return f"({self.customer_info} {self.commercial_contact} {self.total_amount} {self.balance_payable} {self.start_date} {self.contract_status})"


class Event(Base):

    __tablename__ = "events"

    id: Mapped[int] = mapped_column(primary_key=True, unique=True, autoincrement=True)  # Ou ssn self security number
    event_name: Mapped[str] = mapped_column(String(150))

    # Relation with contracts:
    # contract_id: Mapped[int] = mapped_column(ForeignKey("contracts.id"), nullable=False)
    
    contract_id: Mapped[int] = mapped_column(ForeignKey("contracts.id"))
    contract: Mapped["Contract"] = relationship(back_populates="event_map")
    customer_name: Mapped[str] = mapped_column(String(150))
    customer_contact: Mapped[str] = mapped_column(String(150))

    start_date: Mapped[datetime.date] = mapped_column(DateTime(timezone=True), server_default=func.now())
    end_date: Mapped[datetime.date] = mapped_column(DateTime(timezone=True), server_default=func.now())
    location: Mapped[str] = mapped_column(String(150), nullable=False)

    # Relation with user:
    support_contact: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=True)
    user: Mapped["User"] = relationship(back_populates="events_map")

    attendees: Mapped[int] = mapped_column(nullable=False)
    notes: Mapped[str] = mapped_column(String(250), nullable=False)


    def __init__(self, event_name, contract_id, customer_name,\
        customer_contact, start_date, end_date, support_contact,\
        location, attendees, notes):
        self.event_name = event_name
        self.contract_id = contract_id
        self.customer_name = customer_name
        self.customer_contact = customer_contact
        self.start_date = start_date
        self.end_date = end_date
        self.support_contact = support_contact
        self.location = location
        self.attendees = attendees
        self.notes = notes

    def __repr__(self):
        return f"({self.event_name} {self.contract_id}\n" + f" {self.customer_name} {self.customer_contact} {self.start_date}\n" + f"{self.end_date} {self.support_contact} {self.location}\n" + f"{self.attendees} {self.notes} )"


