from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy import text, update
from view.commercial_menu_view import CommercialMenuView
from .engine_controller import EngineController
from .engine_controller import engine, session
from model.users_model import Customer, Events, Contracts


	
class CommercialController:
    def __init__(self):
        pass


    def commercial_menu_controller(self):
        menu_app = CommercialMenuView()
        choice, values = menu_app.commercial_menu_view()

        if choice == 1:
            self.create_customer(values)
            
        elif choice == 2:
            self.update_customer(values)
        
        elif choice == 3:
            self.update_contract(values)

        elif choice == 4:
            self.display_filtered_contract(values)

        elif choice == 5:
            self.create_event(values)
            
        elif choice == 6:
            print("\n Bye!")
            raise SystemExit
        

    def create_customer(self, values):
        print('values:', values)
        ident, full_name, email, tel, company_name, first_date, last_date, contact = values
        
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


    def update_customer(self, values):
        print('values:', values)
        ident, key_to_update, value_to_update = values

        customer = session.query(Customer).filter_by(ident=ident).one_or_none()
        print('customer_to_update:', customer)

        query = session.query(Customer)
        column_names = query.statement.columns.keys()

        for elt in column_names:
            if elt == key_to_update:
                if key_to_update == 'ident':
                    customer.ident = value_to_update
                elif key_to_update == 'full_name':
                    customer.full_name = value_to_update
                elif key_to_update == 'email':
                    customer.email = value_to_update
                elif key_to_update == 'tel':
                    customer.tel = value_to_update
                elif key_to_update == 'company_name':
                    customer.company_name = value_to_update
                elif key_to_update == 'first_date':
                    customer.first_date = value_to_update
                elif key_to_update == 'last_date':
                    customer.last_date = value_to_update
                elif key_to_update == 'contact':
                    customer.contact = value_to_update

        session.commit()    # push
        print('customer_updated:', customer)


    def update_contract(self, values):
        print('values:', values)
        contract_to_update, key_to_update, value_to_update = values

        contract = session.query(Contracts).filter_by(contract_id=contract_to_update).one_or_none()
        print('contract_to_update:', contract)

        query = session.query(Contracts)
        column_names = query.statement.columns.keys()

        for elt in column_names:
            if elt == key_to_update:
                if key_to_update == 'contract_id':
                    contract.contract_id = value_to_update
                elif key_to_update == 'customer_info':
                    contract.customer_info = value_to_update
                elif key_to_update == 'commercial_contact':
                    contract.commercial_contact = value_to_update
                elif key_to_update == 'total_amount':
                    contract.total_amount = value_to_update
                elif key_to_update == 'balance_payable':
                    contract.balance_payable = value_to_update
                elif key_to_update == 'start_date':
                    contract.start_date = value_to_update
                elif key_to_update == 'contract_status':
                    contract.contract_status = value_to_update

        session.commit()    # push
        print('customer_updated:', contract)
        
        
    def valid_contract(self, value):
        pass


    def display_filtered_contract(self, value):
        pass


    def create_event(self, value):
        contract_name, event_id, contract_id, customer_name, customer_contact, start_date, end_date, support_contact, location, attendees, notes = value

        event = Events(contract_name, event_id, contract_id, customer_name, customer_contact, start_date, end_date, support_contact, location, attendees, notes)
        
        session.add(event)   # stage
        session.commit()    # push

        with engine.connect() as conn:
            result = conn.execute(text("select * from events"))
            for rows in result:
                print("Events:", rows)
        self.commercial_menu_controller()     # Retour menu gestion"""
	
	