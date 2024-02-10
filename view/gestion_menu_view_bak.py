
from sqlalchemy import text
from sqlalchemy.orm import Session, sessionmaker
from model.users_model import User, Event, Contract, Customer
from controller.engine_controller import engine, session
<<<<<<< HEAD:view/gestion_menu_view.py
from .start_menu_view import StartMenuView
from model.users_model import Permissions_roles
from model.users_model import ADD_USER, UPDATE_USER, DELETE_USER, ADD_CONTRACT, UPDATE_CONTRACT, DISPLAY_FILTERED_EVENTS, UPDATE_EVENT
=======
from model.users_model import Permissions_roles
>>>>>>> a891adf09afd0adf79f7d2288e7efd794b789e8f:view/gestion_menu_view_bak.py


class GestionMenuView:
    def __init__(self):
        pass


    def get_permission(self, role, role_fct):
        for elt in Permissions_roles:
            if elt == role:
                result = Permissions_roles[role]
        for elt in result:
            if elt == role_fct:
                # print('elt')
                return True


    def gestion_menu_view(self, id, role):
        print("Choose options")
        answer = True
        while answer:
            print("""
            1. Create user.
<<<<<<< HEAD:view/gestion_menu_view.py
            2. Update user: GESTION, COMMERCIAL, or SUPPORT.
=======
            2. Update user.
>>>>>>> a891adf09afd0adf79f7d2288e7efd794b789e8f:view/gestion_menu_view_bak.py
            3. Delete user.
            4. Create contract.
            5. Update contract.
            6. Display filtered events: No associated support.
            7. Update events.
<<<<<<< HEAD:view/gestion_menu_view.py
            8. Quit.
            """)

            answer = input("Faites votre choix ! \n")
            if answer == "1":
                value = self.create_user_account(id, role)
                return 1, value
            elif answer == "2":
                value = self.update_user_account(id, role)
                return 2, value
            elif answer == "3":
                value = self.delete_user_account(id, role)
=======
            8. Display users.
            9. Display customers.
            10. Display contracts.
            11. Display events.
            12. Quit.
            """)

            answer = input("Faites votre choix ! \n")
            if answer == "1":                
                for elt in Permissions_roles.values():
                    print('elt:', elt)
                value = self.create_user_account()
                return 1, value
            elif answer == "2":
                value = self.update_user_account()
                return 2, value
            elif answer == "3":
                value = self.get_user_ident()
>>>>>>> a891adf09afd0adf79f7d2288e7efd794b789e8f:view/gestion_menu_view_bak.py
                return 3, value
            elif answer == "4":
                self.display_customers()
                value = self.create_contract(id, role)
                # self.display_ordered_contracts()
                return 4, value
            elif answer == "5":
                # self.display_ordered_contracts()
                value = self.update_contract(id, role)
                return 5, value
            elif answer == "6":
                self.display_filtered_events()
                return 6, None
            elif answer == "7":
                value = self.update_events(id, role)
                return 7, value
            elif answer == "8":
<<<<<<< HEAD:view/gestion_menu_view.py
                print("\n Bye!")
                raise SystemExit


    def create_user_account(self, user_id, user_role):
        self.display_users()
        if self.get_permission(user_role, ADD_USER):
            username = input('Nom du nouveau collaborateur: ')
            password = str(input('Password: '))
            email = input("collaborator email : ")
            role = input('A quel departement est affecte le nouveau collaborateur ?: ')
            return username, password, email, role
        else:
            print("Operation only allowed for Gestion departement !")
            self.gestion_menu_view(user_id, user_role)  # Retour menu


    def display_ordered_update_users(self):
        users = session.query(User).all()
        i = 0
        for elt in users:
            print(i, '. username:', elt.username, 'password:', elt.password,\
            'email:', elt.email, 'role:', elt.role.value)
            i = i + 1
        choix = input("Choisir un id user:")
        user = users[int(choix)]
        return user


    def update_user_account(self, user_id, user_role):
        user_to_update = self.display_ordered_update_users()

        if self.get_permission(user_role, UPDATE_USER):
            key_to_update = input('Clé à modifier: ')
            value_to_update = input('Nouvelle valeur:' )
            return user_to_update.id, key_to_update, value_to_update
        else:
            print('user_role2:', user_role)
            print("Operation only allowed for Gestion departement !")
            
        self.gestion_menu_view(user_id, user_role)


    def delete_user_account(self, user_id, user_role):
        user_to_delete = self.display_ordered_update_users()
        if self.get_permission(user_role, DELETE_USER):
            return user_to_delete.id    # key/value_to_delete
        else:
            print("Operation only allowed for Gestion departement !")
        self.main_menu_view(user_id, user_role)
=======
                return 8, None
            elif answer == "9":
                return 9, None
            elif answer == "10":
                return 10, None
            elif answer == "11":
                return 11, None
            elif answer == "12":
                return 12, None

    def get_user_data(self):
        self.display_users()
        # ident = input('Identifiant numérique: ')
        print('\n')
        username = input('User name: ')
        password = input ('Password: ')
        email = input("User email : ")
        role = input('Departement: Gestion(1), Commercial(2), Support(3): ')
        return ident, username, password, email, role
        

    def create_user_account(self):
        # self.display_gestion_table()
        # id = input('Identifiant numérique: ')
        # print('\n')
        username = input('User name: ')
        password = str(input('Password: '))
        email = input("User email : ")
        role = input('A quel departement est affecte le nouvel utilisateur ?: ')
        # return ident, username, password, email, role
        return username, password, email, role


    def update_user_account(self):
        self.display_users()
        id = input('Identifiant numérique: ')
        print('\n')        
        key_to_update = input('Clé à modifier: ')
        value_to_update = input('Nouvelle valeur: ')
        return id, key_to_update, value_to_update


    def get_user_ident(self):
        self.display_users()
        ident = input('Identifiant numérique:' )
        return ident


    def display_users(self):
        users = session.query(User).all()
        
        """for user in users:
            print(f"id: {user.id}, username: {user.username}, password: {user.password}, email: {user.email}, role: {user.role}")"""

    def display_customers(self):
        customers = session.query(Customer).all()
        """for customer in customers:
            print("id:", {customer.id}, "full_name:", {customer.full_name}, "customer_email:", {customer.customer_email},
            "tel:", {customer.tel}, "company_name:", {customer.company_name}, "first_date:", {customer.first_date},
            "last_date:", {customer.last_date}, "contact:", {customer.contact})"""


    def display_contracts(self):
        contracts = session.query(Contract).all()
        """for contract in contracts:
            print("id:", {contract.id})"""


    def display_events(self):
        events = session.query(Event).all()
        #for event in events:
            # print("id", {event.id})


    def create_contract_data(self):
        id = input('Idenfifiant numérique: ')
        customer_info = input('N° du client (id): ')
        # commercial_contact = input('Email contact commercial associé au client: ')
        total_amount = input('Montant total du contrat: ')
        balance_payable = input('Montant restant à payer: ')
        start_date = input('Date de création du contrat: ')
        contract_status = input('Contrat values: SIGNED or UNSIGNED: ')
        # return id, customer_info, commercial_contact, total_amount, balance_payable, start_date, contract_status
        return id, customer_info, total_amount, balance_payable, start_date, contract_status
>>>>>>> a891adf09afd0adf79f7d2288e7efd794b789e8f:view/gestion_menu_view_bak.py


    def display_users(self):
        users = session.query(User).all()
        i = 0
        for elt in users:
            print(i, '. User:', elt.username, elt.email, elt.role.value)
            i = i + 1
    


    def display_customers(self):
        customers = session.query(Customer).all()
        i = 0
        print('############# Customers ##############')
        for elt in customers:
            user = session.query(User).filter(User.id == elt.contact).first()
            print(i,'. Customer_id:',elt.id, "\n", "full_name:", elt.full_name,\
            "\n", "customer_email:", elt.customer_email, "\n",
            "tel:", elt.tel, "\n", "company_name:", elt.company_name,\
            "\n",  "first_date:", elt.first_date, "\n"
            "last_date:", elt.last_date, "\n", "contact:", user.username)
            i = i + 1


    def display_ordered_contracts(self):
        contracts = session.query(Contract).all()
        i = 0
        print('############# Contracts ##############\n')
        for elt in contracts:
            user = session.query(User).filter(User.id == elt.commercial_contact).first()
            customer = session.query(Customer).filter(Customer.id == elt.customer_info).first()
            
            print(i,'. Contract_id:', customer.id,\
                    "\n", 'customer_info:', customer.full_name, customer.customer_email,\
                    "\n", 'tel:',customer.tel,\
                    "\n", 'commercial_contact:', user.username,\
                    "\n", 'total_amount:', elt.total_amount,\
                    "\n", 'balance_payable:', elt.balance_payable,\
                    "\n", 'start_date:', elt.start_date,\
                    "\n", 'commercial_status:', elt.contract_status.value, "\n")
            i = i + 1


    def create_contract(self, user_id, user_role):
        if self.get_permission(user_role, ADD_CONTRACT):
            customer_info = input('N° du client (id): ')
            # commercial_contact = input('Email contact commercial associé au client: ')
            total_amount = input('Montant total du contrat: ')
            balance_payable = input('Montant restant à payer: ')
            start_date = input('Date de création du contrat: ')
            contract_status = input('Contrat values: SIGNED or UNSIGNED: ')
            # return id, customer_info, commercial_contact, total_amount, balance_payable, start_date, contract_status
            return customer_info, total_amount, balance_payable, start_date, contract_status
        else:
            print("Operation only allowed for Gestion departement !")
            self.gestion_menu_view(user_id, user_role)
        self.display_ordered_contracts()

    
    def display_ordered_update_contracts(self):
        contracts = session.query(Contract).all()
        i = 0
        print('############# Contracts ##############\n')
        for elt in contracts:
            user = session.query(User).filter(User.id == elt.commercial_contact).first()
            customer = session.query(Customer).filter(Customer.id == elt.customer_info).first()
            
            print(i,'. Contract_id:', elt.id,\
                    "\n", 'customer_info:', customer.full_name, customer.customer_email,\
                    "\n", 'tel:',customer.tel, "\n", 'commercial_contact:', user.username,\
                    "\n", 'total_amount:', elt.total_amount,\
                    "\n", 'balance_payable:', elt.balance_payable,\
                    "\n", 'start_date:', elt.start_date,\
                    "\n", 'commercial_status:', elt.contract_status.value)
            i = i + 1
        choix = input("Choisir un id contrat:")
        contract = contracts[int(choix)]
        return contract

    def update_contract(self, user_id, user_role):
        contract_to_update = self.display_ordered_update_contracts()
        query = session.query(Contract)
        column_names = query.statement.columns.keys()
        print('Choose one key :', column_names)
        print('contract_to_update:', contract_to_update, contract_to_update.id)
        if self.get_permission(user_role, UPDATE_CONTRACT):
            key_to_update = input('Attribut à modifier: ')
            value_to_update = input('Nouvelle valeur: ')
            return contract_to_update.id, key_to_update, value_to_update
        else:
            print("Operation only allowed for Gestion departement !")
            self.gestion_menu_view(user_id, user_role)



    def display_filtered_events(self):   # affiche tous les événements qui n’ont pas de « support » associé.        
        event = session.query(Event).filter_by(support_contact="").all()
        print('event with no contact support:', event)
<<<<<<< HEAD:view/gestion_menu_view.py
=======
        
>>>>>>> a891adf09afd0adf79f7d2288e7efd794b789e8f:view/gestion_menu_view_bak.py
        print('event with support contact:')
        self.display_events()


    def update_events(self, user_id, user_role):
        event_to_update = self.display_update_events()

        if self.get_permission(user_role, UPDATE_EVENT):
            key_to_update = input('Clé à modifier: ')
            value_to_update = input('Nouvelle valeur:' )
            return event_to_update.id, key_to_update, value_to_update
        else:
            print("Operation only allowed for Gestion departement !")
        self.gestion_menu_view(user_id, user_role)


    def display_update_events(self):
        events = session.query(Event).all()
        i = 0
        for event in events:
            print(i,'event_name:', event.event_name,\
                    "\n", 'id:', event.id,\
                    "\n", 'contract_id:', event.contract_id,\
                    "\n", 'customer_name:', event.customer_name,\
                    "\n", 'customer_contact:', event.customer_contact,\
                    "\n", 'start_date:', event.start_date,\
                    "\n", 'end_date:', event.end_date,\
                    "\n", 'support_contact:', event.support_contact,\
                    "\n", 'location:', event.location,\
                    "\n", 'attendees:', event.attendees,\
                    "\n", 'notes:', event.notes)
            i = i + 1
        choix = input("Choisir un id Event:")
        event = events[int(choix)]
        return event


    def display_events(self):
        events = session.query(Event).all()
        i = 0
        for event in events:
            print(i,'event_name:', event.event_name,\
                "\n", 'id:', event.id,\
                "\n", 'contract_id:', event.contract_id,\
                "\n", 'customer_name:', event.customer_name,\
                "\n", 'customer_contact:', event.customer_contact,\
                "\n", 'start_date:', event.start_date,\
                "\n", 'end_date:', event.end_date,\
                "\n", 'support_contact:', event.support_contact,\
                "\n", 'location:', event.location,\
                "\n", 'attendees:', event.attendees,\
                "\n", 'notes:', event.notes)
            i = i + 1
    





