import bcrypt
# from sqlalchemy import text, update, select
# from sqlalchemy.orm import Session, sessionmaker
from view.gestion_menu_view import GestionMenuView
# from view.start_menu_view import StartMenuView
# from .engine_controller import EngineController
from model.users_model import User, Contract, Event, Customer
from .engine_controller import session  # engine,
#  cannot import name 'StartMenuController'(most likely due to a circular import)
# from .start_menu_controller import StartMenuController



class GestionController:
    def __init__(self, user_controller):
        self.user_controller = user_controller
        self.gestion_views = GestionMenuView()


    def gestion_menu_controller(self):           # Administration, Sign in
        
        # choice = self.menu_app.gestion_menu_view()
        choice = self.gestion_views.gestion_menu_view()
        role = self.user_controller.current_user.role.value

        if choice == "1":
            self.create_user(role)
        elif choice == "2":
            self.update_user(role)
        elif choice == "3":
            self.delete_user(role)
        elif choice == "4":
            self.create_contract(role)
        elif choice == "5":
            self.update_contract(role)
        elif choice == "6":
            self.gestion_views.display_filtered_events()
            self.gestion_menu_controller()
        elif choice == "7":
            self.update_events(role)
        elif choice == "8":
            self.user_controller.start_controller.run_db()
            # self.start_controller()


    def create_user(self, role):
        print('create_user')
        # username, password, email, role = self.menu_app.create_user(UserController.current_user.role.value)
        print('role:', role)
        username, password, email, role = self.gestion_views.create_user_account(role)

        bytes = password.encode('utf-8')
        hashed_password = bcrypt.hashpw(bytes, bcrypt.gensalt())

        user = User(username, password, hashed_password, email, role)
        print('user:', user)
        session.add(user)   # stage
        session.commit()    # push

        users = session.query(User).all()
        for user in users:
            print(f"id: {user.id}, username: {user.username}," "\n",\
                    "password: {user.password}," "\n",\
                    "email: {user.email}," "\n",\
                    "role: {user.role}")
        self.gestion_menu_controller()     # Retour menu gestion


    def update_user(self, role):
        id, key_to_update, value_to_update = self.gestion_views.update_user_account(role)
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
                    user.role = value_to_update
        session.commit()
        print('Updated:', user.username, user.email, user.role.value)
        self.gestion_menu_controller()


    def delete_user(self, role):
        id = self.gestion_views.delete_user_account(role)
        if id:
            user = session.query(User).filter_by(id=id).one_or_none()
            session.delete(user)
            session.commit()
            print('After update:')            
            self.gestion_views.display_users()
        else:
            print('no_values!')
            self.gestion_menu_controller()
        self.gestion_menu_controller()


    def create_contract(self, role):
        customer_info, total_amount, balance_payable, start_date, contract_status = self.gestion_views.create_contract(role)
        id_commercial = session.query(Customer).where(Customer.id == customer_info).all()
        print('id_commercial:')
        commercial_contact = id_commercial[0].contact
        contract = Contract(customer_info, commercial_contact, total_amount, balance_payable, start_date, contract_status)

        session.add(contract)   # stage
        session.commit()    # push
        self.gestion_menu_controller()     # Retour menu gestion


    def update_contract(self, role):
        contract_id, key_to_update, value_to_update = self.gestion_views.update_contract(role)
        contract = session.query(Contract).filter_by(id=contract_id).one_or_none()
        query = session.query(Contract)
        column_names = query.statement.columns.keys()
        
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
        self.gestion_views.display_ordered_contracts()
        self.gestion_menu_controller()      # Retour au menu


    def update_events(self, role):
        event_id, key_to_update, new_attribut_value = self.gestion_views.update_events(role)
        event = session.query(Event).filter_by(id=event_id).one_or_none()
        query = session.query(Event)
        column_names = query.statement.columns.keys()
        print('attribut: ', key_to_update)
        for elt in column_names:
            if elt == key_to_update:
                if key_to_update == 'event_name':
                    event.event_name = new_attribut_value
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
        session.commit()
        self.gestion_views.display_events()
        self.gestion_menu_controller()      # Retour au menu
