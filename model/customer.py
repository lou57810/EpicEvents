import datetime
from typing import List

from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, String, DateTime
from sqlalchemy.sql import func
from .link import Link


class Base(DeclarativeBase):
    pass


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
    
    # contact: Mapped[int] = mapped_column(ForeignKey("users.id"))
    # user: Mapped["User"] = relationship(back_populates="customers_map")
    # user: Mapped["User"] = relationship(back_populates="user")

    # Relation contract
    # contrats_maps: Mapped[List["Contract"]] = relationship(back_populates='customer', cascade="all, delete-orphan")

    # links: List[Link] = relationship("Link", back_populates="customer")



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