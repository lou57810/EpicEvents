from model.user import User
from model.event import Event
from model.contract import Contract
from model.customer import Customer
from controller.engine_controller import session
from model.user import Permissions_roles, RoleEnum
import logging


class GestionMenuView:
    def __init__(self):
        pass

    def get_permission(self, role, role_fct):
        for elt in Permissions_roles:
            if elt == role:
                result = Permissions_roles[role]
        for elt in result:
            if elt == role_fct:
                return True

    def test_integer_entry(self, var):
        # Vérifie si l'entrée est un entier
        if not var.isdigit():
            print("Veuillez entrer un nombre entier.")
            number = input("Select N° Menu: ")
            user_number = int(number)
            return user_number
        else:
            return int(var)

    def gestion_menu_view(self):
        answer = {
                "1": "Create user.",
                "2": "Update user.",
                "3": "Delete user.",
                "4": "Display users.",
                "5": "Create contract.",
                "6": "Update contract.",
                "7": "Display contracts",
                "8": "Display filtered events",
                "9": "Update events.",
                "10": "Display customers.",
                "11": "Display Events.",
                "0": "Quit"
        }
        print('\n')
        while True:
            print("\n".join(f"{key}. {value}" for key, value in answer.items()))
            selection = input("Select N° Menu: ")

            if selection in answer:
                print('selection:', selection)
                return selection
            else:
                logging.error("Invalid entry !", extra=dict(bar=43))
                print("Invalid selection. Please enter a valid number.")

    def menu_role(self):
        """
            Prints all menu items and the corresponding number.
        """
        print("\n=========== MENU ===========")
        print("1 - GESTION")
        print("2 - COMMERCIAL")
        print("3 - SUPPORT")
        print("============================\n")

    def get_role(self):
        self.menu_role()
        i = 1
        val = list()
        for role in RoleEnum:
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
        username = input('Nom du nouveau collaborateur: ')
        password = str(input('Password: '))
        email = input("collaborator email : ")
        role = self.get_role()
        return username, password, email, role

    def display_ordered_users(self):
        users = session.query(User).all()
        i = 0
        for elt in users:
            print('N°', i, '\n',
                  'username:', elt.username, '\n',
                  'password:', elt.password, '\n',
                  'email:', elt.email, '\n',
                  'role:', elt.role.name)
            i = i + 1
        print('\n')
        return users

    def get_num_update_user(self):
        number = input("Choisir un N° user:")
        return number

    def get_user_key_to_update(self, user_id):
        print('id:', user_id)
        user = session.get(User, user_id)
        print('user_values:', user)
        query = session.query(User)

        column_names = query.statement.columns.keys()
        print('\n')
        print('##### User selected #####\n')
        print('username:', user.username, "\n",
              'password:', user.password, "\n",
              'email:', user.email, "\n",
              'Role:', user.role.name, "\n")
        print('Choose one key :', '\n',
              '1:', column_names[1], '\n',
              '2:', column_names[2], '\n',
              '3:', column_names[4], '\n',
              '4:', column_names[5], '\n')
        key_to_update = input('Attribut à modifier: ')
        return key_to_update, column_names

    def update_user_account(self, key_to_update, column_names):
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
            print('key_to_update', key_to_update)
        return key_to_update, value_to_update

    def delete_user_account(self, user_role):
        user_to_delete = self.display_ordered_update_users()
        return user_to_delete.id    # key/value_to_delete

    def display_users(self):
        users = session.query(User).all()
        i = 0
        for elt in users:
            print('N°', i, '. User:', elt.username, elt.email, elt.role.name)
            i = i + 1

    def display_customers(self):
        customers = session.query(Customer).all()
        i = 0
        print('#-------------- Customers ---------------#')
        for elt in customers:
            user = session.query(User).filter(User.id == elt.contact).first()
            print('N°', i, "\n",
                  "id:", elt.id, "\n",
                  "full_name:", elt.full_name, "\n",
                  "customer_email:", elt.customer_email, "\n",
                  "tel:", elt.tel, "\n",
                  "company_name:", elt.company_name, "\n",
                  "first_date:", elt.first_date, "\n",
                  "last_date:", elt.last_date, "\n",
                  "contact:", user.username)
            i = i + 1
        choix = input("Choisir un N° customer:")
        customer = customers[int(choix)]
        return customer.id

    def display_ordered_contracts(self):
        contracts = session.query(Contract).all()
        i = 0
        print('#------------- Contracts --------------#\n')
        for elt in contracts:
            user = session.query(User).filter(
                User.id == elt.commercial_contact).first()
            customer = session.query(Customer).filter(
                Customer.id == elt.customer_info).first()
            print('N°', i, "\n",
                  'Contract_id:', customer.id, "\n",
                  'customer_info:', customer.full_name,
                  customer.customer_email, "\n",
                  'tel:', customer.tel, "\n",
                  'commercial_contact:', user.username, "\n",
                  'total_amount:', elt.total_amount, "\n",
                  'balance_payable:', elt.balance_payable, "\n",
                  'start_date:', elt.start_date, "\n",
                  'commercial_status:', elt.contract_status.value)
            i = i + 1

    def display_one_customer(self, customer, user):
        print('#---- customer_info ----#\n')
        print(' id:', customer.id, "\n",
              'Name:', customer.full_name, "\n",
              'email:', customer.customer_email, "\n",
              'Tel:', customer.tel, "\n",
              'First date:', customer.first_date, "\n",
              'Last date:', customer.last_date, "\n",
              'Contact:', user.username)

    def create_contract(self, user_role):
        customer_info = self.display_customers()
        customer = session.get(Customer, customer_info)
        user = session.get(User, customer.contact)
        self.display_one_customer(customer, user)

        total_amount = input('Montant total du contrat: ')
        balance_payable = input('Montant restant à payer: ')
        start_date = input('Date création: YYYY-MM-DD format\n')
        contract_status = input(
                        'Contrat status: (1: SIGNED or 2: UNSIGNED)')
        return customer_info, total_amount, \
            balance_payable, start_date, contract_status

    def display_ordered_update_contracts(self):
        contracts = session.query(Contract).all()
        i = 0
        print('#----------- Contracts -----------#\n')
        for elt in contracts:
            user = session.query(User).filter(
                   User.id == elt.commercial_contact).first()
            customer = session.query(Customer).filter(
                       Customer.id == elt.customer_info).first()

            print('N°', i, "\n",
                  'customer_info:', customer.full_name,
                  customer.customer_email, "\n",
                  'tel:', customer.tel, "\n",
                  'commercial_contact:', user.username, "\n",
                  'total_amount:', elt.total_amount, "\n",
                  'balance_payable:', elt.balance_payable, "\n",
                  'start_date:', elt.start_date, "\n",
                  'contract_status:', elt.contract_status.value)
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
        print('#---- Contract selected ----#\n')
        print('customer_info:', customer.full_name,
              customer.customer_email, "\n",
              'tel:', customer.tel, "\n",
              'commercial_contact:', user.username, "\n",
              'total_amount:', contract.total_amount, "\n",
              'balance_payable:', contract.balance_payable, "\n",
              'start_date:', contract.start_date, "\n",
              'contract_status:', contract.contract_status)
        query = session.query(Contract)
        column_names = query.statement.columns.keys()
        print('Choose one key :', '\n',
              '1:', column_names[3], '\n',
              '2:', column_names[4], '\n',
              '3:', column_names[5], '\n',
              '4:', column_names[6], '\n')

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

    # affiche tous les événements qui n’ont pas de « support » associé
    def display_filtered_events(self, user_role):
        event_no_contact = session.query(Event).filter(Event.support_contact.is_(None)).all()

        i = 0
        if event_no_contact:
            for elt in event_no_contact:
                print('N°', i, "\n",
                      'Id:', elt.id, '\n',
                      'Event Name:', elt.event_name, '\n',
                      'Start Date:', elt.start_date, '\n',
                      'End Date:', elt.end_date, '\n',
                      'Location:', elt.location, '\n',
                      'Support Contact:', elt.support_contact, '\n',
                      'Attendees:', elt.attendees, '\n',
                      'Notes:', elt.notes, '\n')
                i = i + 1
            return event_no_contact
        else:
            print('No event without support_contact.')

    def select_filtered_events(self, user_role):
        events = self.display_filtered_events(user_role)
        choix = input("Choisir un N° Event:")
        event = events[int(choix)]
        return event

    def update_events(self, user_role):
        event_to_update = self.select_filtered_events(user_role)

        query = session.query(Event)
        column_names = query.statement.columns.keys()

        print('Choose one key :', '\n',
              '1:', column_names[1], '\n',
              '2:', column_names[5], '\n',
              '3:', column_names[6], '\n',
              '4:', column_names[7], '\n',
              '5:', column_names[8], '\n',
              '6:', column_names[9], '\n',
              '7:', column_names[10], '\n')

        key_to_update = input('N° Clé à modifier: ')
        if key_to_update == "1":
            key_to_update = column_names[1]
            value_to_update = input('Nouvelle valeur: ')
        elif key_to_update == "2":
            key_to_update = column_names[5]
            value_to_update = input('Nouvelle valeur: ')
        elif key_to_update == "3":
            key_to_update = column_names[6]
            value_to_update = input('Nouvelle valeur: ')
        elif key_to_update == "4":
            key_to_update = column_names[7]
            value_to_update = input('Nouvelle valeur: ')
        elif key_to_update == "5":
            # Requête pour récupérer les utilisateurs avec le rôle "support"
            users_support = session.query(
                User).filter(User.role == RoleEnum.SUPPORT.value).all()
            i = 0
            while i < len(users_support):
                print('Username:', users_support[i].username,
                      ', Id:', users_support[i].id)
                i = i + 1
            key_to_update = column_names[8]
            value_to_update = input('Nouvelle valeur (id): ')
        elif key_to_update == "6":
            key_to_update = column_names[9]
            value_to_update = input('Nouvelle valeur: ')
        elif key_to_update == "7":
            key_to_update = column_names[10]
            value_to_update = input('Nouvelle valeur: ')
        return event_to_update.id, key_to_update, value_to_update

    def display_events(self):
        events = session.query(Event).all()
        i = 0
        for event in events:
            print('N°', i, "\n",
                  'event_name:', event.event_name, "\n",
                  'contract_id:', event.contract_id, "\n",
                  'customer_name:', event.customer_name, "\n",
                  'customer_contact:', event.customer_contact, "\n",
                  'start_date:', event.start_date, "\n",
                  'end_date:', event.end_date, "\n",
                  'support_contact:', self.get_username_from_id(
                      event.support_contact), "\n",
                  'location:', event.location, "\n",
                  'attendees:', event.attendees, "\n",
                  'notes:', event.notes)
            i = i + 1
        return events

    # Fonction pour récupérer le username à partir de l'ID
    def get_username_from_id(self, user_id):
        user = session.query(User).filter(User.id == user_id).first()
        if user:
            return user.username
        else:
            return None
