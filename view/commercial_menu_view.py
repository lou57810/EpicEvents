from controller.engine_controller import session

from model.user import User
from model.contract import Contract
from model.customer import Customer
from model.event import Event
from model.user import Permissions_roles
from model.user import ADD_CUSTOMER, UPDATE_OWN_CUSTOMER, \
            UPDATE_OWN_CONTRACT, CREATE_SIGNED_OWN_EVENT


class CommercialMenuView:

    def __init__(self, user_controller):
        self.user_controller = user_controller

    def get_permission(self, role, role_fct):
        for elt in Permissions_roles:
            if elt == role:
                result = Permissions_roles[role]
        for elt in result:
            if elt == role_fct:
                # print('elt')
                return True

    def commercial_menu_view(self):
        print("Choose options")
        answer = True
        while answer:
            print("""
            1. Create customer.
            2. Update customer.
            3. Display customers.
            4. Display contracts.
            5. Update own contract.
            6. Display filtered contract.
            7. Create event for contract.
            0. Deconnection.
            """)

            answer = input("Faites votre choix ! \n")
            return answer

    # Création client
    def create_customer_account(self, user_role):
        self.display_customers()
        print('\n')
        if self.get_permission(user_role, ADD_CUSTOMER):
            full_name = input('Nom prénom du Client: ')
            customer_email = input('Email du client: ')
            tel = input('Tel: ')
            company_name = input('Entreprise: ')
            first_date = input('Date création: YYYY-MM-DD format\n')
            last_date = input('Date dernier contact: YYYY-MM-DD format\n')
            # Contact: Affectation automatique de l'id contact commercial.
            return full_name, customer_email, tel, \
                company_name, first_date, last_date
        else:
            print("Operation only allowed for Commercial departement !")
            self.commercial_menu_view()

    # Maj client
    def update_own_customer(self, user_role, current_user):
        customer_to_update = self.display_customers_to_update()
        print('\n')
        customer = session.query(Customer).filter_by(
                   id=customer_to_update.id).one_or_none()
        user = session.get(User, current_user)
        print('#### customer to update ####\n\n', customer.full_name)

        if self.get_permission(user_role, UPDATE_OWN_CUSTOMER):
            if customer.contact != current_user:
                print('\n')
                print('#### Forbidden', customer.full_name,
                      'is not your customer. Retry! ####\n')
                self.update_own_customer(user_role, current_user)

            else:
                print('##### Customer selected #####\n')
                print('Customer full name:', customer.full_name, "\n",
                      'Email:', customer.customer_email, "\n",
                      'Tel:', customer.tel, "\n",
                      'Company name:', customer.company_name, "\n",
                      'First date contact:', customer.first_date, "\n",
                      'Last date contact:', customer.last_date, "\n",
                      'Contact:', user.username, "\n")
                print('\n')
                query = session.query(Customer)
                column_names = query.statement.columns.keys()

                print('Choose one key :',
                      '\n', '1:', column_names[1],
                      '\n', '2:', column_names[2],
                      '\n', '3:', column_names[3],
                      '\n', '4:', column_names[4],
                      '\n', '5:', column_names[5],
                      '\n', '6:', column_names[6],
                      '\n', '7:', column_names[7],
                      '\n')

            key_to_update = input('N° Clé à modifier: ')
            if key_to_update == "1":
                key_to_update = column_names[1]
                value_to_update = input('Nouvelle valeur entrée: ')
            elif key_to_update == "2":
                key_to_update = column_names[2]
                value_to_update = input('Nouvelle valeur entrée: ')
            elif key_to_update == "3":
                key_to_update = column_names[3]
                value_to_update = input('Nouvelle valeur entrée: ')
            elif key_to_update == "4":
                key_to_update = column_names[4]
                value_to_update = input('Nouvelle valeur entrée: ')
            elif key_to_update == "5":
                key_to_update = column_names[5]
                value_to_update = input('Nouvelle valeur entrée: ')
            elif key_to_update == "6":
                key_to_update = column_names[6]
                value_to_update = input('Nouvelle valeur entrée: ')
            elif key_to_update == "7":
                key_to_update = column_names[7]
                value_to_update = input('Nouvelle valeur entrée: ')
            return user, customer_to_update.id, key_to_update, value_to_update
        else:
            print("Operation only allowed for Commercial departement !")
            self.commercial_menu_view()

    def display_customers_to_update(self):
        customers = self.display_customers()
        choix = input("Choisir un N° client:")
        customer = customers[int(choix)]
        return customer

    def display_customers(self):
        customers = session.query(Customer).all()
        i = 0
        for elt in customers:
            # Get username from id: (elt.contact)
            user = session.query(User).filter(User.id == elt.contact).first()
            print('N°:', i, "\n",
                  'full_name:', elt.full_name, "\n",
                  'email:', elt.customer_email, "\n",
                  'tel:', elt.tel, "\n",
                  'company_name:', elt.company_name, "\n",
                  'first_date:', elt.first_date, "\n",
                  'last_date:', elt.last_date, "\n",
                  'contact:', user.username)
            i = i + 1
        print('\n')
        return customers

    def update_own_contract(self, user_role, current_user):
        contract_to_update = self.display_contracts_to_update()
        print('\n')
        contract = session.query(Contract).filter_by(
            id=contract_to_update.id).one_or_none()
        if self.get_permission(user_role, UPDATE_OWN_CONTRACT):
            if contract.commercial_contact != current_user:
                print('Forbidden, this contract is not one of your owns!')
                self.user_controller.commercial_controller\
                    .commercial_menu_controller()
            else:
                query = session.query(Contract)
                column_names = query.statement.columns.keys()
                print('Choose one key :', column_names[3],
                      column_names[4], column_names[5], column_names[6])
                key_to_update = input("Clé à modifier :")
                value_to_update = input("Nouvelle valeur :")
                return contract_to_update.id, key_to_update, value_to_update
        else:
            print("Operation only allowed for Commercial departement !")
            self.user_controller.commercial_controller\
                .commercial_menu_controller()
        self.commercial_menu_view()

    def display_contracts_to_update(self):
        contracts = self.display_contracts()
        print('\n')

        choix = input("Choisir un N° de contrat:")
        contract = contracts[int(choix)]
        return contract

    def display_filtered_contracts(self, user_role):
        contracts = session.query(Contract).filter((
            Contract.balance_payable > '0') | (
            Contract.contract_status == 'UNSIGNED')).all()
        i = 0
        for elt in contracts:
            print('N°', i, '\n',
                  'Total amount:', elt.total_amount, '\n',
                  'Balance_payable:', elt.balance_payable, "\n",
                  'status:', elt.contract_status.value)
            i = i + 1

    def display_contracts(self):
        contracts = session.query(Contract).all()
        if contracts:
            i = 0
            z = len(contracts)

            # Get username from id: (contracts[i].contact)
            # Get info customer from customer_id: (contracts[i].customer_id)
            print('\n')
            while i < z:
                user = session.query(User).filter(
                        User.id == contracts[i].commercial_contact).first()
                customer = session.query(Customer).filter(
                    Customer.id == contracts[i].customer_info).first()
                print('N°', i, "\n",
                      'customer_info:', customer.full_name,
                      customer.customer_email, "\n",
                      'tel:', customer.tel, "\n",
                      'commercial_contact:', user.username, "\n",
                      # 'total_amount:', elt.total_amount, "\n",
                      'total_amount:', contracts[i].total_amount, "\n",
                      # 'balance_payable:', elt.balance_payable, "\n",
                      'balance_payable:', contracts[i].balance_payable, "\n",
                      # 'start_date:', elt.start_date, "\n",
                      'start_date:', contracts[i].start_date, "\n",
                      # 'contract_status:', elt.contract_status.value)
                      'contract_status:', contracts[i].contract_status.value)
                i = i + 1
        return contracts

    def get_user(self):
        users = session.query(User).filter(User.role == "SUPPORT")
        i = 0
        num_list = []
        for elt in users:
            num_list.append(elt.id)
            print('N°', i,
                  '\n', 'username:', elt.username,
                  '\n', 'role:', elt.role.name)
            i = i + 1
        support_contact = input("N° Support Contact:")
        return num_list[int(support_contact)]

    # Contract must be signed and belong to commercial connected collaborator.
    def create_validated_contract_event(self, user_role, current_user):
        print('#------- Contrats -------#\n')
        # contract = self.display_ordered_update_own_contracts()
        contract = self.display_contracts_to_update()
        contract_id = contract.id
        customers = session.query(Customer).all()

        # Must be commercial.
        if self.get_permission(user_role, CREATE_SIGNED_OWN_EVENT):
            user = session.query(User).filter(User.id == current_user).first()
            print(user.username, 'Collaborator from Commercial Department.')
            # Owner must be current user.
            if contract.commercial_contact != current_user:
                print('Forbidden, this contract is not one of yours!')
                self.user_controller.commercial_controller.\
                    commercial_menu_controller()
            else:
                print('contract_status:', contract.contract_status.value)
                # Contract must be signed.
                if contract.contract_status.value != 'SIGNED':
                    print('Operation not allowed,\
                          because contract_status is not signed!')
                    self.user_controller.commercial_controller.\
                        commercial_menu_controller()
                # All conditions verified.
                else:
                    for val in customers:  # Coords customer.
                        val = session.query(Customer).filter(
                            Customer.id == contract.customer_info).first()
                        customer_name = val.full_name
                        customer_contact = val.id
                    event_name = input("Nom de l'evenement: ")
                    print('Choose N° Support contact collaborator:')
                    support_contact = None
                    start_date = input("Début de l'évènement:")
                    end_date = input("Fin de l'évènement'")
                    location = input("Lieu de l'evenement: ")
                    attendees = input("Nombre de participants: ")
                    notes = input("Notes/ deroulement de l'evenement: ")
                    print('event:', event_name, contract_id,
                          customer_name, customer_contact,
                          start_date, end_date,
                          support_contact, location,
                          attendees, notes)
                    return event_name, contract_id, \
                        customer_name, customer_contact, \
                        start_date, end_date, \
                        support_contact, location, \
                        attendees, notes
        else:
            print("Operation only allowed for Commercial departement !")
            self.user_controller.commercial_controller\
                .commercial_menu_controller()

    def display_events(self):
        events = session.query(Event).all()
        # customer = session.query(Customer).all()
        i = 0
        for elt in events:
            user = session.get(User, elt.support_contact)
            customer = session.get(Customer, elt.customer_contact)
            print('########## Events #########\n')
            print('N°', i, '. Event_id:', elt.id, "\n",
                  'Event name:', elt.event_name, "\n",
                  'Customer contact:', customer.full_name,
                  customer.customer_email, "\n",
                  'Tel:', customer.tel, "\n",
                  'start_date:', elt.start_date, "\n",
                  'end_date:', elt.end_date, "\n",
                  'support contact:', user.username, "\n",
                  'location:', elt.location, "\n",
                  'attendees:', elt.attendees, "\n",
                  'notes:', elt.notes)
            i = i + 1
