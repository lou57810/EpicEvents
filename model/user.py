from enum import Enum as PyEnum
# import datetime
from typing import List
from sqlalchemy import Column, String, types  # DateTime ForeignKey
# from sqlalchemy.dialects.mysql import LONGTEXT
from sqlalchemy.orm import Mapped, mapped_column, relationship
# relationship  DeclarativeBase
# from sqlalchemy.sql import func
from .base import Base


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


# Department role.
class RoleEnum(PyEnum):
    GESTION = "GESTION"
    COMMERCIAL = "COMMERCIAL"
    SUPPORT = "SUPPORT"


class SignEnum(PyEnum):
    SIGNED = "SIGNED"
    UNSIGNED = "UNSIGNED"


Permissions_roles = {"GESTION": [ADD_USER, UPDATE_USER, DELETE_USER,
                                 ADD_CONTRACT, UPDATE_CONTRACT,
                                 UPDATE_EVENT, DISPLAY_FILTERED_EVENTS],
                     "COMMERCIAL": [ADD_CUSTOMER, UPDATE_OWN_CUSTOMER,
                                    UPDATE_OWN_CONTRACT,
                                    CREATE_SIGNED_OWN_EVENT],
                     "SUPPORT": [UPDATE_OWN_EVENT]}


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True,
                                    unique=True, autoincrement=True)
    username: Mapped[str] = mapped_column(String(120))
    password: Mapped[str] = mapped_column(String(120))
    hashed_pass: Mapped[str] = mapped_column(String(120))
    email: Mapped[str] = mapped_column(String(120),
                                       nullable=False, unique=True)
    role = Column(types.Enum(RoleEnum,
                  values_callable=lambda obj: [e.value for e in obj]))

    customers_map: Mapped[List["Customer"]] = relationship(
        back_populates='user', cascade="all, delete-orphan")
    contracts_map: Mapped[List["Contract"]] = relationship(
        back_populates='user', cascade="all, delete-orphan")
    events_map: Mapped[List["Event"]] = relationship(
        back_populates='user', cascade="all, delete-orphan")

    def __init__(self, username, password, hashed_pass, email, role):
        self.username = username
        self.password = password
        self.hashed_pass = hashed_pass
        self.email = email
        self.role = role

    def __repr__(self) -> str:
        return f"({self.username} {self.password}\
                {self.hashed_pass} {self.email} {self.role})"
