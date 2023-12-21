import os
# from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import LargeBinary, ForeignKey
from sqlalchemy.dialects.mysql import LONGTEXT
import datetime

from typing import Optional
from typing import List
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import create_engine, Column, Integer, String, Date, Text

from sqlalchemy import DateTime
from sqlalchemy.sql import func
from sqlalchemy_utils.types.choice import ChoiceType
import jwt

# from abc import ABC, abstractmethod
# abc est un module python intégré, nous importons ABC et abstractmethod





class Base(DeclarativeBase):
    pass


class Collaborator(Base):


    __tablename__ = "collaborators"

    ROLE = [
        ("Departement Gestion", "Departement Gestion"),
        ("Departement Commercial", "Departement Commercial"),
        ("Departement Support", "Departement Support")
        ]

    id: Mapped[int] = mapped_column(primary_key=True, unique=True, autoincrement=True)  # Ou ssn self security number
    ident: Mapped[int] = mapped_column(nullable=False, unique=True)
    username: Mapped[str] = mapped_column(String(50))
    password : Mapped[str] = mapped_column(String(120))
    # salt: Mapped[str] = mapped_column(String(60))
    hashed_pass: Mapped[str] = mapped_column(String(60))
    email: Mapped[str] = mapped_column(String(150), nullable=False, unique=True)
    role: Mapped[str] = mapped_column(String(50), ChoiceType(ROLE))

    def __init__(self, ident, username, password, hashed_pass, email, role):
        self.ident = ident
        self.username = username
        self.password = password
        # self.salt = salt
        self.hashed_pass = hashed_pass
        self.email = email
        self.role = role

    """def serialize_collaborator(self):
       return {
            'ident' : self.ident,
            'username' : self.username,
            'password' : self.password,
            'hashed_pass' : self.hashed_pass,
            'email' : self.email,
            'role': self.role,
       }"""

    def __repr__(self):
        return f"({self.ident} {self.username} {self.password} {self.hashed_pass} {self.email} {self.role})"



class Customer(Base):
    
    __tablename__ = "customers"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    ident: Mapped[int] = mapped_column(nullable=False, unique=True)
    full_name: Mapped[str] = mapped_column(String(150), nullable=False)
    email: Mapped[str] = mapped_column(String(150), nullable=False, unique=True)
    tel: Mapped[str] = mapped_column(String(150), nullable=False, unique=True)
    company_name: Mapped[str] = mapped_column(String(150), nullable=False, unique=True)
    first_date: Mapped[datetime.datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    last_date:  Mapped[datetime.datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    contact: Mapped[str] = mapped_column(String(150), nullable=False)

    def __init__(self, ident, full_name, email, tel, company_name, first_date, last_date, contact):
        self.ident = ident
        self.full_name = full_name
        self.email = email
        self.tel = tel
        self.company_name = company_name
        self.first_date = first_date
        self.last_date = last_date
        self.contact = contact

    def __repr__(self):
        return f"({self.ident} {self.full_name} {self.email} {self.tel} {self.company_name} {self.first_date} {self.last_date} {self.contact})"


class Contracts(Base):
    
    __tablename__ = "contracts"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    contract_id: Mapped[int] = mapped_column(nullable=False, unique=True) 
    customer_info: Mapped[int] = mapped_column(ForeignKey("customers.ident"))
    commercial_contact: Mapped[str] = mapped_column(String(150), nullable=False)
    total_amount: Mapped[int] = mapped_column(String(150), nullable=False)
    balance_payable: Mapped[int] = mapped_column(String(150), nullable=False)
    start_date: Mapped[datetime.datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())    
    contract_status: Mapped[str] = mapped_column(String(150), nullable=False)

    def __init__(self, contract_id, customer_info, commercial_contact, total_amount, balance_payable, start_date, contract_status):
        self.contract_id = contract_id
        self.customer_info = customer_info
        self.commercial_contact = commercial_contact
        self.total_amount = total_amount
        self.balance_payable = balance_payable
        self.start_date = start_date
        self.contract_status = contract_status

    def __repr__(self):
        return f"({self.contract_id} {self.customer_info} {self.commercial_contact} {self.total_amount} {self.balance_payable} {self.start_date} {self.contract_status})"


class Events(Base):

    __tablename__ = "events"

    id: Mapped[int] = mapped_column(primary_key=True, unique=True, autoincrement=True)  # Ou ssn self security number
    contract_name: Mapped[str] = mapped_column(String(50), nullable=False)
    event_id: Mapped[int] = mapped_column(nullable=False, unique=True)
    contract_id: Mapped[int] = mapped_column()
    customer_name: Mapped[str] = mapped_column(String(100), nullable=False)
    customer_contact: Mapped[str] = mapped_column(String(150), nullable=False)
    start_date: Mapped[datetime.datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    end_date: Mapped[datetime.datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    support_contact: Mapped[str] = mapped_column(String(50), nullable=False)
    location: Mapped[str] = mapped_column(String(150), nullable=False)
    attendees: Mapped[str] = mapped_column(String(50), nullable=False)
    notes: Mapped[str] = mapped_column(String(250), nullable=False)


    def __init__(self, contract_name, event_id, contract_id, customer_name, customer_contact, start_date, end_date, support_contact, location, attendees, notes):
        self.contract_name = contract_name
        self.event_id = event_id
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
        return f"({self.contract_name} {self.event_id} {self.contract_id} {self.customer_name} {customer_contact} {self.start_date} {self.end_date} {self.support_contact} {self.location} {self.attendees} {self.notes} )"

    
    """class role(str, enum.Enum):
            Departement Gestion, "Departement Gestion",
            Departement Commercial, "Departement Commercial",
            Departement Support, "Departement Support"
    """
        

