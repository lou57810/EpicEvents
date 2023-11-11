# from sqlalchemy.ext.declarative import declarative_base
import datetime

from typing import Optional
from typing import List
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy import DateTime
from sqlalchemy.sql import func

# from abc import ABC, abstractmethod
# abc est un module python intégré, nous importons ABC et abstractmethod

class Base(DeclarativeBase):
    pass


class Collaborator(Base):
    
    __tablename__ = "collaborators"
    
    
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    email: Mapped[str] = mapped_column(String(150), nullable=False, unique=True)
    password: Mapped[str] = mapped_column(String(50))
    role: Mapped[str] = mapped_column(String(50))

    def __init__(self, id, email, role):
        self.id = id
        self.email = email
        self.role = role

    def __repr__(self):
        return f"({self.email} {self.role})"



class Customer(Base):
    
    __tablename__ = "customers"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    full_name: Mapped[str] = mapped_column(String(150), nullable=False)
    email: Mapped[str] = mapped_column(String(150), nullable=False, unique=True)
    tel: Mapped[str] = mapped_column(String(150), nullable=False, unique=True)
    company_name: Mapped[str] = mapped_column(String(150), nullable=False, unique=True)    
    first_date: Mapped[datetime.datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    last_date:  Mapped[datetime.datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    contact: Mapped[str] = mapped_column(String(150), nullable=False)

    def __init__(self, id, full_name, email, tel, company_name, first_date, last_date, contact):
        self.id = id
        self.full_name = full_name
        self.email = email
        self.tel = tel
        self.company_name = company_name
        self.first_date = first_date
        self.last_date = last_date
        self.contact = contact

    def __repr__(self):
        return f"({self.full_name} {self.email} {self.tel} {self.company_name} {self.first_date} {self.last_date} {self.contact})"


 
