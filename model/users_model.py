from sqlalchemy.ext.declarative import declarative_base

# from abc import ABC, abstractmethod
# abc est un module python intégré, nous importons ABC et abstractmethod

# Base = declarative_base()

class Collaborator():
    pass
    """
    __tablename__ = "collaborator"

    
    id = Column('id', Integer, primary_key=True)
    fullname = Column('full_name', String)
    email = Column('email', String)
    tel = Column('tel', String)
    role = Column('Rôle', String)

    def __init__(self, ssn, fullname, email, tel, role):
        self.ssn = ssn
        self.fullname = fullname
        self.email = email
        self.tel = tel
        self.role = role

    def __repr__(self):
        return f"({self.id} {self.fullname} {self.email} {self.tel} {self.role})"
    """



class Customer():
    """
    __tablename__ = "customer"

    
    def __init__(self):
        pass
    """
    pass
