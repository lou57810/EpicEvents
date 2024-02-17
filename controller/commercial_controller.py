from sqlalchemy.orm import sessionmaker
from sqlalchemy import text, update
from view.commercial_menu_view import CommercialMenuView
# from .engine_controller import EngineController
from .engine_controller import engine, session
from model.users_model import Customer, Event, Contract



class CommercialController:
    def __init__(self):
        pass


    def commercial_menu_controller(self, id, role):   # Récupération de l'id du commercial
        menu_app = CommercialMenuView()
        choice, values = menu_app.commercial_menu_view(id, role)

        if choice == 1:
            self.create_customer(values, id, role)
        elif choice == 2:
            self.update_customer(values, id, role)
        elif choice == 3:
            self.update_own_contract(values, id, role)
        elif choice == 4:
            menu_app.display_filtered_contracts(id, role)
        elif choice == 5:
            menu_app.display_events()
            self.create_event(values, id, role)
            menu_app.display_events()


    def create_customer(self, values, contact_id, role):   # Récupération valeurs renseignée, et foreign key: contact_id
        # print('values:', values)
        full_name, customer_email, tel, company_name, first_date, last_date = values

        customer = Customer(full_name, customer_email, tel, company_name, first_date, last_date, contact_id)    # Association automatique du commercial

        session.add(customer)   # stage
        session.commit()    # push

        with engine.connect() as conn:
            result = conn.execute(text("select * from customers"))
            for rows in result:
                print("Customers:", rows)
        self.commercial_menu_controller(contact_id, role)     # Retour menu


    def update_customer(self, values, contact_id, role):
        # print('values:', values)
        if values:
            id, key_to_update, value_to_update = values

            customer = session.query(Customer).filter_by(id=id).one_or_none()

            query = session.query(Customer)
            column_names = query.statement.columns.keys()

            for elt in column_names:
                if elt == key_to_update:
                    if key_to_update == 'id':
                        customer.id = value_to_update
                    elif key_to_update == 'full_name':
                        customer.full_name = value_to_update
                    elif key_to_update == 'customer_email':
                        customer.customer_email = value_to_update
                    elif key_to_update == 'tel':
                        customer.tel = value_to_update
                    elif key_to_update == 'company_name':
                        customer.company_name = value_to_update
                    elif key_to_update == 'first_date':
                        customer.first_date = value_to_update
                    elif key_to_update == 'last_date':
                        customer.last_date = value_to_update
                    # contact est associé au commercial donc chgt interdit.

            session.commit()    # push

            print('Customers_after_update:', customer.full_name,\
                    "Key:", key_to_update, "Value", value_to_update)
        else:
            print('no values!')
        self.commercial_menu_controller(contact_id, role)


    def update_own_contract(self, values, contact_id, role):
        if values:
            contract_to_update, key_to_update, value_to_update = values
            contract = session.query(Contract).filter_by(id=contract_to_update).one_or_none()
            # print('email, contract_to_update:', contact_id, contract)

            query = session.query(Contract)
            column_names = query.statement.columns.keys()

            # value_to_update = Valeur de la clé selectionnée à modifier
            for elt in column_names:
                if elt == key_to_update:
                    if key_to_update == 'id':
                        contract.id = value_to_update
                    elif key_to_update == 'customer_info':
                        contract.customer_info = value_to_update
                    # elif key_to_update == 'commercial_contact':   Ne doit pas être modifiable
                        # contract.commercial_contact = value_to_update
                    elif key_to_update == 'total_amount':
                        contract.total_amount = value_to_update
                    elif key_to_update == 'balance_payable':
                        contract.balance_payable = value_to_update
                    elif key_to_update == 'start_date':
                        contract.start_date = value_to_update
                    elif key_to_update == 'contract_status':
                        contract.contract_status = value_to_update

            session.commit()    # push
            menu_app = CommercialMenuView()
            menu_app.display_ordered_contracts()

        else:
            print('no values!')
        self.commercial_menu_controller(contact_id, role)


    def create_event(self, values, contact_id, role):
        if values:
            event_name, contract_id, customer_name, customer_contact, start_date, end_date, support_contact, location, attendees, notes = values
            print('values:', values)
 
            event = Event(event_name, contract_id, customer_name,\
            customer_contact, start_date, end_date, support_contact,\
            location, attendees, notes)
            print('event:', event)
            session.add(event)   # stage
            session.commit()    # push
        else: 
            print('Contract is not signed, event can\'t be created!')

            """with engine.connect() as conn:
                result = conn.execute(text("select * from events"))
                for rows in result:
                    print("Events:", rows)"""

            self.commercial_menu_controller(contact_id, role)     # Retour menu gestion
