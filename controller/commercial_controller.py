# from sqlalchemy.orm import sessionmaker
# from sqlalchemy import text  # update
from view.commercial_menu_view import CommercialMenuView
# from .engine_controller import EngineController
from .engine_controller import session  # engine
from model.user import User
from model.customer import Customer
from model.event import Event
from model.contract import Contract
from model.user import Permissions_roles
from model.user import ADD_CUSTOMER, UPDATE_OWN_CUSTOMER, \
            UPDATE_OWN_CONTRACT, CREATE_SIGNED_OWN_EVENT


class CommercialController:
    def __init__(self, user_controller):
        self.user_controller = user_controller
        self.commercial_views = CommercialMenuView()

    def get_permission(self, role, role_fct):
        for elt in Permissions_roles:
            if elt == role:
                result = Permissions_roles[role]
        for elt in result:
            if elt == role_fct:
                # print('elt')
                return True

    def commercial_menu_controller(self):
        current_user = self.user_controller.current_user.id
        choice = self.commercial_views.commercial_menu_view()
        role = self.user_controller.current_user.role.value

        if choice == "1":
            self.create_customer(role)
        elif choice == "2":
            self.update_customer(role, current_user)
            self.commercial_menu_controller()
        elif choice == "3":
            self.commercial_views.display_customers()
            self.commercial_menu_controller()
        elif choice == "4":
            self.commercial_views.display_contracts()
            print('\n')
            self.commercial_menu_controller()
        elif choice == "5":
            self.update_own_contract(role, current_user)
        elif choice == "6":
            self.commercial_views.display_filtered_contracts(role)
            self.commercial_menu_controller()
        elif choice == "7":
            self.create_event(role, current_user)
        elif choice == "0":
            current_user = self.user_controller.current_user.username
            print('current_user:', current_user)
            self.user_controller.report_user_logout(current_user)
            self.user_controller.start_controller.start_dbepic_app()

    def check_current_user():
        pass

    def create_customer(self, role):
        (full_name, customer_email,
            tel, company_name, first_date,
            last_date) = self.commercial_views.create_customer_account(role)
        # Association automatique du commercial
        customer = Customer(full_name, customer_email,
                            tel, company_name, first_date,
                            last_date, self.user_controller.current_user.id)
        session.add(customer)   # stage
        session.commit()    # push
        self.commercial_views.display_customers()
        self.commercial_menu_controller()     # Retour menu

    def update_customer(self, role, current_user):
        customer_to_update = self.commercial_views.display_customers_to_update()
        print('\n')
        customer = session.query(Customer).filter_by(
                   id=customer_to_update.id).one_or_none()
        user = session.get(User, current_user)
        if self.get_permission(role, UPDATE_OWN_CUSTOMER):
            if customer.contact != current_user:
                print('\n')
                print('#### Forbidden', customer.full_name,
                      'is not your customer. Retry! ####\n')
                self.commercial_menu_controller()
            else:
                (id, key_to_update,
                    value_to_update) = self.commercial_views.update_own_customer(
                        role, current_user, customer)
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
                        elif key_to_update == 'contact':
                            customer.contact = value_to_update
                session.commit()    # push
                print('Sortie nouvelle val de', key_to_update, ':', value_to_update)
                self.commercial_menu_controller()
        else:
            print("Operation only allowed for Commercial departement !")
            self.commercial_menu_controller()

    def update_own_contract(self, role, current_user):
        print('verif current_user:', current_user, '\n')
        contract_to_update = self.commercial_views.display_contracts_to_update()
        if self.get_permission(role, UPDATE_OWN_CONTRACT):
            contract = session.query(Contract).filter_by(
                id=contract_to_update.id).one_or_none()
            if contract.commercial_contact != current_user:
                print('Forbidden, this contract is not one of your owns!')
                self.commercial_menu_controller()
            else:
                key_to_update, value_to_update = self.commercial_views.update_own_contract(role, current_user, contract)
                query = session.query(Contract)
                column_names = query.statement.columns.keys()

                for elt in column_names:
                    if elt == key_to_update:
                        if key_to_update == 'id':
                            contract.id = value_to_update
                        elif key_to_update == 'customer_info':
                            contract.customer_info = value_to_update
                        elif key_to_update == 'total_amount':
                            contract.total_amount = value_to_update
                        elif key_to_update == 'balance_payable':
                            contract.balance_payable = value_to_update
                        elif key_to_update == 'start_date':
                            contract.start_date = value_to_update
                        elif key_to_update == 'contract_status':
                            contract.contract_status = value_to_update

                session.commit()    # push
                self.commercial_views.display_contracts()
                self.commercial_menu_controller()
        else:
            print("Operation only allowed for Commercial departement !")
            self.commercial_menu_controller()

    def create_event(self, role, current_user):
        (event_name, contract_id, customer_name,
            customer_contact, start_date, end_date,
            support_contact, location, attendees,
            notes) = self.commercial_views.create_validated_contract_event(
                role, current_user)
        event = Event(event_name, contract_id,
                      customer_name, customer_contact,
                      start_date, end_date, support_contact,
                      location, attendees, notes)
        print('event:', event)
        session.add(event)   # stage
        session.commit()    # push
