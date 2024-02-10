import bcrypt
from sqlalchemy import text, update, select
from sqlalchemy.orm import Session, sessionmaker
from view.gestion_menu_view import GestionMenuView
from view.start_menu_view import StartMenuView
from .engine_controller import EngineController
from model.users_model import User, Contract, Event, Customer
from .engine_controller import engine, session




class GestionController:
    def __init__(self):
        pass


    def gestion_menu_controller(self, id, role):           # Administration, Sign in
        menu_app = GestionMenuView()
        choice, values = menu_app.gestion_menu_view(id, role)
        
        if choice == 1:
            self.create_user(values)
        elif choice == 2:
            self.update_user(id, role, values)
        elif choice == 3:
            self.delete_user(id, role, values)
        elif choice == 4:
            self.create_contract(id, role, values)
        elif choice == 5:
            self.update_contract(id, role, values)
        elif choice == 6:
            pass
        elif choice == 7:
            self.update_events(id, role, values)
        # elif choice == 8:
            # menu_app = StartMenuView()
            # menu_app.start_menu_view()
            


    def create_user(self, values):
        username, password, email, role = values

        bytes = password.encode('utf-8')
        hashed_password = bcrypt.hashpw(bytes, bcrypt.gensalt())

        user = User(username, password, hashed_password, email, role)
        session.add(user)   # stage
        session.commit()    # push
        
        users = session.query(User).all()
        for user in users:
            print(f"id: {user.id}, username: {user.username}," "\n",\
                    "password: {user.password}," "\n",\
                    "email: {user.email}," "\n",\
                    "role: {user.role}")
        self.gestion_menu_controller(id, role)     # Retour menu gestion


    def update_user(self, id, role, values):
        if values:
            id, key_to_update, value_to_update = values
            user = session.query(User).filter_by(id=id).one_or_none()

            query = session.query(User)
            column_names = query.statement.columns.keys()
        
            for elt in column_names:
                if elt == key_to_update:
                    # if key_to_update == 'id': # clé non modifiable
                        # user.id = value_to_update
                    if key_to_update == 'username':
                        user.username = value_to_update
                    elif key_to_update == 'password':
                        bytes = value_to_update.encode('utf-8')
                        salt = bcrypt.gensalt()
                        hashed_password = bcrypt.hashpw(bytes, salt)
                        # print('hashed_password:', bcrypt.hashpw(bytes, salt))
                        user.password = value_to_update
                        user.hashed_pass = hashed_password
                    elif key_to_update == 'email':
                        user.email = value_to_update
                    elif key_to_update == 'role':
                        print('role_sortie:', user.role)
                        user.role = value_to_update
            session.commit()
            print('Updated:', user.id, user.username, user.email, user.role.value)
        else:
            print('no_values!')
            self.gestion_menu_controller(id, user_role)
        self.gestion_menu_controller(id, role)


    def delete_user(self, id, user_role, values):
        if values:
            id = values
            user = session.query(User).filter_by(id=id).one_or_none()
            session.delete(user)
            session.commit()
            print('After update:')
            menu_app = GestionMenuView()
            menu_app.display_users()
        else:
            print('no_values!')
            self.gestion_menu_controller(id, user_role)
        self.gestion_menu_controller(id, user_role)


    def create_contract(self, id, role, values):
        customer_info, total_amount, balance_payable, start_date, contract_status = values
        print('values:', values)
        id_commercial = session.query(Customer).where(Customer.id == customer_info).all()
        commercial_contact = id_commercial[0].contact
        contract = Contract(customer_info, commercial_contact, total_amount, balance_payable, start_date, contract_status)
        
        session.add(contract)   # stage
        session.commit()    # push

        self.gestion_menu_controller(id, role)     # Retour menu gestion


    def update_contract(self, id, role, values):
        if values:
            contract_id, key_to_update, value_to_update = values

            contract = session.query(Contract).filter_by(id=contract_id).one_or_none()
            print('contract_to_update:', contract)

            # print('contrac.attribut:', contract.attribut_to_update) # ==>  'Contract' object has no attribute 'attribut_to_update'
            print('attribut: ', key_to_update)
            query = session.query(Contract)
            column_names = query.statement.columns.keys()
            # print('Choose one key :', column_names)
            for elt in column_names:
                if elt == key_to_update:
                    # if key_to_update == 'id':
                        # contract.id = value_to_update
                    if key_to_update == 'customer_info':
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

            print('new session:', session.commit())
            session.commit()
            menu_app = GestionMenuView()
            menu_app.display_ordered_contracts()
            self.gestion_menu_controller(id, role)      # Retour au menu
        else:
            print('No values:')
            self.gestion_menu_controller(id, role)      # Retour au menu


    def update_events(self, id, role, values):
        id, key_to_update, new_attribut_value = values
        if values:

            event = session.query(Event).filter_by(id=id).one_or_none()
            print('event_to_update:', event)

            print('attribut: ', key_to_update)
            query = session.query(Event)
            column_names = query.statement.columns.keys()
            print('col:', column_names)
            for elt in column_names:
                if elt == key_to_update:
                    if key_to_update == 'id':
                        event.event_id = new_attribut_value
                    elif key_to_update == 'event_name':
                        event.event_name = new_attribut_value
                    elif key_to_update == 'contract_id':
                        event.contract_id = new_attribut_value
                    elif key_to_update == 'customer_name':
                        event.customer_name = new_attribut_value
                    elif key_to_update == 'customer_contact':
                        event.customer_contact = new_attribut_value
                    elif key_to_update == 'start_date':
                        event.start_date = new_attribut_value
                    elif key_to_update == 'end_date':
                        event.end_date = new_attribut_value
                    elif key_to_update == 'support_contact':
                        event.support_contact = new_attribut_value
                    elif key_to_update == 'location':
                        event.location = new_attribut_value
                    elif key_to_update == 'attendees':
                        event.attendees = new_attribut_value
                    elif key_to_update == 'notes':
                        event.notes = new_attribut_value

            print('new session:', session.commit())
            session.commit()

            menu_app = GestionMenuView()        # Affichage update
            menu_app.display_events()
        
            self.gestion_menu_controller(id, role)      # Retour au menu
        print('No values')
