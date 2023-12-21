from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy import text, update
from view.commercial_menu_view import CommercialMenuView
from .engine_controller import EngineController
from .engine_controller import engine
from model.users_model import Customer, Events


	
class CommercialController:
    def __init__(self):
        pass


    def commercial_menu_controller(self):
        menu_app = CommercialMenuView()
        choice, value = menu_app.commercial_menu_view()

        if choice == 1:
            self.create_customer(value)
            
        elif choice == 2:
            self.update_customer(value)
        
        elif choice == 3:
            self.valid_contract(value)

        elif choice == 4:
            self.display_filtered_contract(value)

        elif choice == 5:
            self.create_event(value)
            
        elif choice == 6:
            print("\n Bye!")
            raise SystemExit
        

    def create_customer(self, value):
        print('values:', value)
        ident, full_name, email, tel, company_name, first_date, last_date, contact = value

        Session = sessionmaker(bind=engine)
        session = Session()
        # customer = session.query(Customer).filter_by(ident=ident).one_or_none()
        customer = Customer(ident, full_name, email, tel, company_name, first_date, last_date, contact)
        customer.ident = ident
        customer.full_name = full_name
        customer.email = email
        customer.tel = tel
        customer.company_name = company_name
        customer.first_date = first_date
        customer.last_date = last_date
        customer.contact = contact
        
        session.add(customer)   # stage
        session.commit()    # push

        with engine.connect() as conn:
            result = conn.execute(text("select * from customers"))
            for rows in result:
                print("Customers:", rows)
        self.commercial_menu_controller()     # Retour menu

    def update_customer(self, value):
        print('values:', value)
        ident, full_name, email, tel, company_name, first_date, last_date, contact = value

        Session = sessionmaker(bind=engine)
        session = Session()
        customer = session.query(Customer).filter_by(ident=ident).one_or_none()
        # customer = Customer(ident, full_name, email, tel, company_name, first_date, last_date, contact)
        customer.ident = ident
        customer.full_name = full_name
        customer.email = email
        customer.tel = tel
        customer.company_name = company_name
        customer.first_date = first_date
        customer.last_date = last_date
        customer.contact = contact
        
        # session.add(customer)   # stage
        session.commit()    # push

        with engine.connect() as conn:
            result = conn.execute(text("select * from customers"))
            for rows in result:
                print("Customers:", rows)
        self.commercial_menu_controller()     # Retour menu


    def valid_contract(self, value):
        pass


    def display_filtered_contract(self, value):
        pass


    def create_event(self, value):
        contract_name, event_id, contract_id, customer_name, customer_contact, start_date, end_date, support_contact, location, attendees, notes = value

        Session = sessionmaker(bind=engine)
        session = Session()

        event = Events(contract_name, event_id, contract_id, customer_name, customer_contact, start_date, end_date, support_contact, location, attendees, notes)
        
        session.add(event)   # stage
        session.commit()    # push

        with engine.connect() as conn:
            result = conn.execute(text("select * from events"))
            for rows in result:
                print("Events:", rows)
        self.commercial_menu_controller()     # Retour menu gestion"""
	
	