import datetime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, ForeignKey, Date
from .base import Base


class Event(Base):

    __tablename__ = "events"

    id: Mapped[int] = mapped_column(
        primary_key=True, unique=True, autoincrement=True)
    event_name: Mapped[str] = mapped_column(String(150))

    # Relation with contracts:
    contract_id: Mapped[int] = mapped_column(ForeignKey("contracts.id"))
    contract: Mapped["Contract"] = relationship(back_populates="event_map")
    customer_name: Mapped[str] = mapped_column(String(150))
    customer_contact: Mapped[str] = mapped_column(String(150))

    start_date: Mapped[datetime.date] = mapped_column(
        Date())
    end_date: Mapped[datetime.date] = mapped_column(
        Date())
    location: Mapped[str] = mapped_column(String(150), nullable=False)

    # Relation with user:
    support_contact: Mapped[int] = mapped_column(
        ForeignKey("users.id"), nullable=True)
    user: Mapped["User"] = relationship(back_populates="events_map")

    attendees: Mapped[int] = mapped_column(nullable=False)
    notes: Mapped[str] = mapped_column(String(250), nullable=False)

    def __init__(self, id, event_name, contract_id, customer_name,
                 customer_contact, start_date, end_date, support_contact,
                 location, attendees, notes):
        self.id = id
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
        return f"Event(event_name={self.event_name!r},\
                  contract_id={self.contract_id!r},\
                  customer_name={self.customer_name!r},\
                  customer_contact={self.customer_contact!r},\
                  start_date={self.start_date!r},\
                  end_date={self.end_date!r},\
                  support_contact={self.support_contact!r},\
                  location={self.location!r},\
                  attendees={self.attendees!r},\
                  notes={self.notes!r})"
