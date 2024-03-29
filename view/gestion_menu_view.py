import maskpass
# from sqlalchemy import text
# from sqlalchemy.orm import Session, sessionmaker
from model.users_model import User, Event, Contract, Customer # , RoleEnum
from controller.engine_controller import session # engine, 
# from .start_menu_view import StartMenuView
from model.users_model import Permissions_roles, RoleEnum
from model.users_model import ADD_USER, UPDATE_USER, DELETE_USER, ADD_CONTRACT, UPDATE_CONTRACT, DISPLAY_FILTERED_EVENTS, UPDATE_EVENT




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


    def gestion_menu_view(self):
        print("Choose options")
        answer = True
        while answer:
            print("""
            1. Create user.
            2. Update user.
            3. Delete user.
            4. Display users.
            5. Create contract.
            6. Update contract.
            7. Display contracts.
            8. Display filtered events.
            9. Update events.
            0. Deconnection.
            """)
            answer = input("Make your choice ! \n")
            return answer


    def get_role(self):
        print("Role list : ")
        i = 1
        val = list()
        for role in RoleEnum:
            print(f"{i} : {role.value}")
            val.append(role.value)
            i = i + 1
        role_num = input("N° of role : ")
        role = val[int(role_num) - 1]
        return role


    def create_user_account(self, user_role):
        print('\n')
        print('#### Collaborators registered ####\n')
        self.display_users()
        print('\n')
        if self.get_permission(user_role, ADD_USER):
            username = input('Nom du nouveau collaborateur: ')
            password = str(input('Password: '))
            email = input("collaborator email : ")
            role = self.get_role()
            return username, password, email, role
        else:
            print("Operation only allowed for Gestion departement !")
            self.gestion_menu_view()  # Retour menu


    def display_ordered_users(self):
        users = session.query(User).all()
        i = 0
        for elt in users:
            print('N°', i,
            '\n', 'username:', elt.username,
            '\n', 'password:', elt.password,
            '\n', 'email:', elt.email,
            '\n', 'role:', elt.role.name)
            i = i + 1
        print('\n')
        # self.gestion_menu_view()  # Retour menu


    def display_ordered_update_users(self):
        users = session.query(User).all()
        i = 0
        for elt in users:
            print('N°', i,
            '\n', 'username:', elt.username,
            '\n', 'password:', elt.password,
            '\n', 'email:', elt.email,
            '\n', 'role:', elt.role.name)
            i = i + 1
        choix = input("Choisir un id user:")
        user = users[int(choix)]
        print('\n')
        return user


    def update_user_account(self, user_role):
        user_to_update = self.display_ordered_update_users()
        user = session.get(User, user_to_update.id)
        
        query = session.query(User)
        column_names = query.statement.columns.keys()
        # print('Choose one key :', column_names[1], column_names[2], column_names[4], column_names[5])
        print('\n')
        print('##### User selected #####\n')
        print('user:', user.username,
                "\n", 'password:',user.password,
                "\n", 'email:', user.email,
                "\n", 'Role:', user.role.name,
                '\n')
        query = session.query(User)
        column_names = query.statement.columns.keys()
        print('Choose one key :',
        '\n', '1:', column_names[1],
        '\n', '2:', column_names[2],
        '\n', '3:', column_names[4],
        '\n', '4:', column_names[5], "\n")
        
        if self.get_permission(user_role, UPDATE_USER):
            key_to_update = input('Attribut à modifier: ')
            if key_to_update == "1":
                key_to_update = column_names[1]
                value_to_update = input('Nouvelle valeur: ')
            elif key_to_update == "2":
                key_to_update = column_names[2]
                value_to_update = input('Nouvelle valeur: ')
            elif key_to_update == "3":
                key_to_update = column_names[4]
                value_to_update = input('Nouvelle valeur: ')
            elif key_to_update == "4":
                key_to_update = column_names[5]
                value_to_update = self.get_role()
            
            return user_to_update.id, key_to_update, value_to_update
            
        else:
            print('user_role:', user_role)
            print("Operation only allowed for Gestion departement !")
            self.gestion_menu_view()


    def delete_user_account(self, user_role):
        user_to_delete = self.display_ordered_update_users()
        if self.get_permission(user_role, DELETE_USER):
            return user_to_delete.id    # key/value_to_delete
        else:
            print("Operation only allowed for Gestion departement !")
            self.gestion_menu_view()


    def display_users(self):
        users = session.query(User).all()
        i = 0
        for elt in users:
            print('N°',i, '. User:', elt.username, elt.email, elt.role.name)
            i = i + 1


    def display_customers(self):
        customers = session.query(Customer).all()
        i = 0
        print('############# Customers ##############')
        for elt in customers:
            user = session.query(User).filter(User.id == elt.contact).first()
            print('N°', i,
            "\n", "full_name:", elt.full_name,
            "\n", "customer_email:", elt.customer_email,
            "\n", "tel:", elt.tel,
            "\n", "company_name:", elt.company_name,
            "\n", "first_date:", elt.first_date,
            "\n" "last_date:", elt.last_date,
            "\n", "contact:", user.username)
            i = i + 1
        choix = input("Choisir un N° customer:")
        customer = customers[int(choix)]
        return customer.id


    def display_ordered_contracts(self):
        contracts = session.query(Contract).all()
        i = 0
        print('############# Contracts ##############\n')
        for elt in contracts:
            user = session.query(User).filter(User.id == elt.commercial_contact).first()
            customer = session.query(Customer).filter(Customer.id == elt.customer_info).first()
            
            print('N°',i,'. Contract_id:', customer.id,
                    "\n", 'customer_info:', customer.full_name, customer.customer_email,
                    "\n", 'tel:',customer.tel,
                    "\n", 'commercial_contact:', user.username,
                    "\n", 'total_amount:', elt.total_amount,
                    "\n", 'balance_payable:', elt.balance_payable,
                    "\n", 'start_date:', elt.start_date,
                    "\n", 'commercial_status:', elt.contract_status.value, "\n")
            i = i + 1


    def create_contract(self, user_role):
        if self.get_permission(user_role, ADD_CONTRACT):
            customer_info = self.display_customers()
            customer = session.get(Customer, customer_info)
            user = session.get(User, customer.contact)
            
            print('#### customer_info ####:\n')
            print('Name:', customer.full_name,
                "\n", 'email:', customer.customer_email,
                "\n", 'Tel:', customer.tel,
                "\n", 'First date:', customer.first_date,
                "\n", 'Last date:', customer.last_date,
                "\n", 'Contact:', user.username)
            
            total_amount = input('Montant total du contrat: ')
            balance_payable = input('Montant restant à payer: ')
            start_date = input('Date de création du contrat: (format: year-month-day xxxx-xx-xx)')
            contract_status = input('Contrat status: (1: SIGNED or 2: UNSIGNED)')
            return customer_info, total_amount, balance_payable, start_date, contract_status
        else:
            print("Operation only allowed for Gestion departement !")
            self.gestion_menu_view(user_role)
        self.display_ordered_contracts()


    def display_ordered_update_contracts(self):
        contracts = session.query(Contract).all()
        i = 0
        print('############# Contracts ##############\n')
        for elt in contracts:
            user = session.query(User).filter(User.id == elt.commercial_contact).first()
            customer = session.query(Customer).filter(Customer.id == elt.customer_info).first()
            
            print('N°', i,
                    "\n", 'customer_info:', customer.full_name, customer.customer_email,
                    "\n", 'tel:',customer.tel, "\n", 'commercial_contact:', user.username,
                    "\n", 'total_amount:', elt.total_amount,
                    "\n", 'balance_payable:', elt.balance_payable,
                    "\n", 'start_date:', elt.start_date,
                    "\n", 'contract_status:', elt.contract_status.value)
            i = i + 1
        print('\n')
        choix = input("Choisir un id contrat:\n")
        contract = contracts[int(choix)]
        return contract

    def update_contract(self, user_role):
        contract_to_update = self.display_ordered_update_contracts()
        contract = session.get(Contract, contract_to_update.id)
        
        customer = session.get(Customer, contract.customer_info)
        user = session.get(User, contract.commercial_contact)
        print('\n')
        print('##### Contract selected #####\n')
        print('customer_info:', customer.full_name, customer.customer_email,
                    "\n", 'tel:',customer.tel, "\n", 'commercial_contact:', user.username,
                    "\n", 'total_amount:', contract.total_amount,
                    "\n", 'balance_payable:', contract.balance_payable,
                    "\n", 'start_date:', contract.start_date,
                    "\n", 'contract_status:', contract.contract_status, '\n')
        query = session.query(Contract)
        column_names = query.statement.columns.keys()
        print('Choose one key :'
            '\n', '1:', column_names[3],
            '\n', '2:', column_names[4],
            '\n', '3:', column_names[5],
            '\n', '4:', column_names[6], "\n")
        
        if self.get_permission(user_role, UPDATE_CONTRACT):
            key_to_update = input('Attribut à modifier: ')
            if key_to_update == "1":
                key_to_update = column_names[3]
            elif key_to_update == "2":
                key_to_update = column_names[4]
            elif key_to_update == "3":
                key_to_update = column_names[5]
            elif key_to_update == "4":
                key_to_update = column_names[6]
            value_to_update = input('Nouvelle valeur: ')
            return contract_to_update.id, key_to_update, value_to_update
        else:
            print("Operation only allowed for Gestion departement !")
            self.gestion_menu_view()


    def display_filtered_events(self):   # affiche tous les événements qui n’ont pas de « support » associé.        
        event_no_contact = session.query(Event).filter(Event.support_contact == None).all()
        if event_no_contact:
            print('event with no contact support:', event_no_contact)
        else:
            print('No event without support_contact.')


    def update_events(self,user_role):
        event_to_update = self.display_update_events()
        query = session.query(Event)
        column_names = query.statement.columns.keys()
        print('col:', column_names[1], column_names[5], column_names[6],
                column_names[7], column_names[8], column_names[9], column_names[10])

        if self.get_permission(user_role, UPDATE_EVENT):
            key_to_update = input('Clé à modifier: ')
            value_to_update = input('Nouvelle valeur:' )
            return event_to_update.id, key_to_update, value_to_update
        else:
            print("Operation only allowed for Gestion departement !")
        self.gestion_menu_view()


    def display_update_events(self):
        events = session.query(Event).all()
        i = 0
        for event in events:
            print('N°',i,'event_name:', event.event_name,
                    # "\n", 'id:', event.id,
                    "\n", 'contract_id:', event.contract_id,
                    "\n", 'customer_name:', event.customer_name,
                    "\n", 'customer_contact:', event.customer_contact,
                    "\n", 'start_date:', event.start_date,
                    "\n", 'end_date:', event.end_date,
                    "\n", 'support_contact:', event.support_contact,
                    "\n", 'location:', event.location,
                    "\n", 'attendees:', event.attendees,
                    "\n", 'notes:', event.notes)
            i = i + 1
        choix = input("Choisir un id Event:")
        event = events[int(choix)]
        return event


    def display_events(self):
        events = session.query(Event).all()
        i = 0
        for event in events:
            print('N°',i,'event_name:', event.event_name,
                # "\n", 'id:', event.id,
                "\n", 'contract_id:', event.contract_id,
                "\n", 'customer_name:', event.customer_name,
                "\n", 'customer_contact:', event.customer_contact,
                "\n", 'start_date:', event.start_date,
                "\n", 'end_date:', event.end_date,
                "\n", 'support_contact:', event.support_contact,
                "\n", 'location:', event.location,
                "\n", 'attendees:', event.attendees,
                "\n", 'notes:', event.notes)
            i = i + 1







