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
import jwt

# from abc import ABC, abstractmethod
# abc est un module python intégré, nous importons ABC et abstractmethod

class Base(DeclarativeBase):
    pass


class Collaborator(Base):
    
    __tablename__ = "collaborators"

    id: Mapped[int] = mapped_column(primary_key=True, unique=True, autoincrement=True)  # Ou ssn self security number
    ident: Mapped[int] = mapped_column()
    username: Mapped[str] = mapped_column(String(50))
    password: Mapped[str] = mapped_column(String(50))
    email: Mapped[str] = mapped_column(String(150), nullable=False, unique=True)    
    role: Mapped[str] = mapped_column(String(50))   # choices=[("Deparement Gestion", "Deparement Gestion"),
                                                    # ("Deparement Commercial, "Deparement Commercial"),
                                                    # (Deparement Support", "Deparement Support")])

    def __init__(self, ident, username, password, email, role):        
        self.ident = ident
        self.username = username
        self.password = password
        self.email = email
        self.role = role

    """def serialize_collaborator(self):
       return {
            'ident' : self.ident,
            'username' : self.username,
            'password' : self.password,
            'email' : self.email,
            'role': self.role,
       }"""

    def __repr__(self):
        return f"({self.ident} {self.username} {self.password} {self.email} {self.role})"


    """
    @app.route("user/login", methods=["POST"])
    def user_login_controller():
        # request.form()
        return obj.user_login_model(request.form)

    def collaborator_login_model(self, data):
        self.cur.execute(f"SELECT ident, username, password, email, role FROM WHERE email='{data['email']}':")
        result = self.cur.fetchall()
        userdata = result[0]
        exp_date = datetime.now() + timedelta(minutes=60)
        exp_epoch_time = int(exp_time.timestamp())
        payload = {
            "payload": userdata,
            "exp": exp_epoch_time,
        }
        jwtoken = jwt.encode(payload, "secret", algorithm="HS256")
        return make_response({"token": jwtoken, 200})
    """
    # head = {'Authorization': 'Bearer {}'.format(myToken)}

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

    def __init__(self, full_name, email, tel, company_name, first_date, last_date, contact):
        
        self.full_name = full_name
        self.email = email
        self.tel = tel
        self.company_name = company_name
        self.first_date = first_date
        self.last_date = last_date
        self.contact = contact

    def __repr__(self):
        return f"( {self.full_name} {self.email} {self.tel} {self.company_name} {self.first_date} {self.last_date} {self.contact})"

"""
class Contracts(Base):
    
    __tablename__ = "events"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    customer_info: Mapped[str] = mapped_column(String(150), nullable=False)
    commercial_contact: Mapped[str] = mapped_column(String(150), nullable=False, unique=True)
    total_amount: Mapped[int] = mapped_column(String(150), nullable=False, unique=True)
    balance_payable: Mapped[int] = mapped_column(String(150), nullable=False, unique=True)    
    start_date: Mapped[datetime.datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())    
    contract_status: Mapped[str] = mapped_column(String(150), nullable=False)


class Events(Base):

    __tablename__ = "contracts"
    pass
"""
 
# class Posts(Base):

    # __tablename__ = "posts"

