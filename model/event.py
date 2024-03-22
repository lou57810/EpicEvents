import datetime

from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import String, ForeignKey , DateTime# , types# , Column,
from sqlalchemy.sql import func

from .link import Link

class Base(DeclarativeBase):
    pass


class Event(Base):

    __tablename__ = "events"

    id: Mapped[int] = mapped_column(primary_key=True, unique=True, autoincrement=True)  # Ou ssn self security number
    event_name: Mapped[str] = mapped_column(String(150))

    # Relation with contracts:    
    # contract_id: Mapped[int] = mapped_column(ForeignKey("contracts.id"))
    # contract: Mapped["Contract"] = relationship(back_populates="event_map")
    # customer_name: Mapped[str] = mapped_column(String(150))
    # customer_contact: Mapped[str] = mapped_column(String(150))

    start_date: Mapped[datetime.date] = mapped_column(DateTime(timezone=True), server_default=func.now())
    end_date: Mapped[datetime.date] = mapped_column(DateTime(timezone=True), server_default=func.now())
    location: Mapped[str] = mapped_column(String(150), nullable=False)

    # Relation with user:
    # support_contact: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=True)
    # user: Mapped["User"] = relationship(back_populates="events_map")
    # user: Mapped["User"] = relationship(back_populates="user")


    attendees: Mapped[int] = mapped_column(nullable=False)
    notes: Mapped[str] = mapped_column(String(250), nullable=False)
    # links: List[Link] = relationship("Link", back_populates="event")


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
