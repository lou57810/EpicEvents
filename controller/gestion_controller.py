import bcrypt
import logging

from view.gestion_menu_view import GestionMenuView
from view.commercial_menu_view import CommercialMenuView
from model.user import User
from model.contract import Contract
from model.event import Event
from model.customer import Customer
from .engine_controller import session
from model.user import (ADD_USER, UPDATE_USER, DELETE_USER,
                        ADD_CONTRACT, UPDATE_CONTRACT, UPDATE_EVENT,
                        DISPLAY_FILTERED_EVENTS)
from model.user import Permissions_roles  # RoleEnum


class GestionController:
    def __init__(self, user_controller):
        self.user_controller = user_controller
        self.gestion_views = GestionMenuView()
        self.commercial_views = CommercialMenuView()

    def gestion_menu_controller(self):           # Administration, Sign in
        choice = self.gestion_views.gestion_menu_view()
        role = self.user_controller.current_user.role.value

        if choice == "1":
            self.create_user(role)
        elif choice == "2":
            self.update_user(role)
        elif choice == "3":
            self.delete_user(role)
        elif choice == "4":
            self.gestion_views.display_ordered_users()
            self.gestion_menu_controller()
        elif choice == "5":
            self.create_contract(role)
        elif choice == "6":
            self.update_contract(role)
        elif choice == "7":
            self.gestion_views.display_ordered_contracts()
            self.gestion_menu_controller()
        elif choice == "8":
            self.gestion_views.display_filtered_events(role)
            self.gestion_menu_controller()
        elif choice == "9":
            self.update_events(role)
            self.gestion_menu_controller()
        elif choice == "10":
            self.commercial_views.display_customers()
            self.gestion_menu_controller()
        elif choice == "11":
            self.commercial_views.display_events()
            self.gestion_menu_controller()
        elif choice == "0":
            current_user = self.user_controller.current_user.username
            print('current_user:', current_user)
            self.user_controller.report_user_logout(current_user)
            self.user_controller.start_controller.start_dbepic_app()
            # self.start_controller()

    def get_permission(self, role, role_fct):
        for elt in Permissions_roles:
            if elt == role:
                result = Permissions_roles[role]
        for elt in result:
            if elt == role_fct:
                # print('elt')
                return True

    def create_user(self, role):
        if self.get_permission(role, ADD_USER):
            logging.info("This is a creation test message")
            (username, password,
                email, role) = self.gestion_views.create_user_account(role)

            bytes = password.encode('utf-8')
            hashed_password = bcrypt.hashpw(bytes, bcrypt.gensalt())

            user = User(username, password, hashed_password, email, role)
            session.add(user)   # stage
            session.commit()    # push

            print('\n')
            print('Created:', user.username, user.email, user.role.name)
            self.gestion_menu_controller()     # Retour menu gestion
        else:
            print("Operation only allowed for Gestion departement !")
            self.gestion_menu_controller()  # Retour menu

    def update_user(self, role):
        if self.get_permission(role, UPDATE_USER):
            user_number = self.gestion_views.get_num_update_user()
            choice = self.gestion_views.test_integer_entry(user_number)
            users = session.query(User).all()
            user = users[choice]

            key_to_update, column_names = self.gestion_views.get_user_key_to_update(user.id)
            key_to_update, value_to_update = self.gestion_views.update_user_account(
                key_to_update, column_names)

            if key_to_update == 'username':
                user.username = value_to_update
                print('user.username:', user.username)
            elif key_to_update == 'password':
                bytes = value_to_update.encode('utf-8')
                salt = bcrypt.gensalt()
                hashed_password = bcrypt.hashpw(bytes, salt)
                user.password = value_to_update
                user.hashed_pass = hashed_password
            elif key_to_update == 'email':
                user.email = value_to_update
            elif key_to_update == 'role':
                user.role = value_to_update
                print('user.role:', user.role)
            session.commit()
            print('\n')
            print('Updated - user:', user.username,
                  'pass:', user.password, 'email:', user.email,
                  'role:', user.role.name)
            self.gestion_menu_controller()
        else:
            print("Operation only allowed for Gestion departement !")
            self.gestion_menu_controller()  # Retour menu

    def delete_user(self, role):
        if self.get_permission(role, DELETE_USER):
            id_user_connected = self.user_controller.current_user.id
            id = self.gestion_views.delete_user_account(role)
            if id:
                if id == id_user_connected:
                    # Si l'utilisateur se supprime, la session reste ouverte et
                    # les droits Gestion subsistent. Donc choix à exclure.
                    print('WARNING: You can\'t delete yourself! \n')
                    self.gestion_menu_controller()
                else:
                    user = session.query(User).filter_by(id=id).one_or_none()
                    session.delete(user)
                    session.commit()
                    print('After update:')
                    self.gestion_views.display_users()
            else:
                print('no_values!')
                self.gestion_menu_controller()
            self.gestion_menu_controller()
        else:
            print("Operation only allowed for Gestion departement !")
            self.gestion_menu_controller()

    def create_contract(self, role):
        if self.get_permission(role, ADD_CONTRACT):
            (customer_info, total_amount,
                balance_payable, start_date,
                contract_status) = self.gestion_views.create_contract(role)
            id_commercial = session.query(
                Customer).where(Customer.id == customer_info).all()
            commercial_contact = id_commercial[0].contact
            contract = Contract(customer_info, commercial_contact,
                                total_amount, balance_payable,
                                start_date, contract_status)

            session.add(contract)   # stage
            session.commit()    # push
            self.gestion_views.display_ordered_contracts()
            self.gestion_menu_controller()     # Retour menu gestion
        else:
            print("Operation only allowed for Gestion departement !")
            self.gestion_menu_controller()

    def update_contract(self, role):
        if self.get_permission(role, UPDATE_CONTRACT):
            (contract_id, key_to_update,
                value_to_update) = self.gestion_views.update_contract(role)
            contract = session.query(
                Contract).filter_by(id=contract_id).one_or_none()
            query = session.query(Contract)
            column_names = query.statement.columns.keys()

            for elt in column_names:
                if elt == key_to_update:
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
            session.commit()
            self.gestion_views.display_ordered_contracts()
            self.gestion_menu_controller()      # Retour au menu
        else:
            print("Operation only allowed for Gestion departement !")
            self.gestion_menu_controller()

    def update_events(self, role):
        if self.get_permission(role, UPDATE_EVENT):
            (event_id, key_to_update,
                value_to_update) = self.gestion_views.update_events(role)
            event = session.query(Event).filter_by(id=event_id).one_or_none()
            query = session.query(Event)
            column_names = query.statement.columns.keys()
            for elt in column_names:
                if elt == key_to_update:
                    if key_to_update == 'event_name':
                        event.event_name = value_to_update
                    elif key_to_update == 'start_date':
                        event.start_date = value_to_update
                    elif key_to_update == 'end_date':
                        event.end_date = value_to_update
                    elif key_to_update == 'location':
                        event.location = value_to_update
                    elif key_to_update == 'support_contact':
                        event.support_contact = value_to_update
                    elif key_to_update == 'attendees':
                        event.attendees = value_to_update
                    elif key_to_update == 'notes':
                        event.notes = value_to_update
            session.commit()
            print('\n')
            self.gestion_views.display_events()
            self.gestion_menu_controller()      # Retour au menu
        else:
            print("Operation only allowed for Gestion departement !")
            self.gestion_menu_controller()

    def display_filtered_events(self, role):
        if self.get_permission(role, DISPLAY_FILTERED_EVENTS):
            self.gestion_views.display_filtered_events()
        else:
            print("Operation only allowed for Gestion departement !")
            self.gestion_menu_controller()
