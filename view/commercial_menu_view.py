from controller.engine_controller import session

from model.users_model import Contract, Customer, User, Event
from model.users_model import Permissions_roles
from model.users_model import ADD_CUSTOMER, UPDATE_OWN_CUSTOMER, UPDATE_OWN_CONTRACT, CREATE_SIGNED_OWN_EVENT



class CommercialMenuView:

    def __init__(self):
        pass

    def get_permission(self, role, role_fct):
        for elt in Permissions_roles:
            if elt == role:
                result = Permissions_roles[role]
        for elt in result:
            if elt == role_fct:
                print('elt')
                return True

    def commercial_menu_view(self):
        print("Choose options")
        answer = True
        while answer:
            print("""
            1. Create customer.
            2. Update customer.
            3. Display customers.
            4. Update own contract.
            5. Display filtered contract.
            6. Create event for contract.
            7. Quit.
            """)

            answer = input("Faites votre choix ! \n")
            return answer


    # Création client
    def create_customer_account(self, user_role):
        self.display_customers()
        if self.get_permission(user_role, ADD_CUSTOMER):
            full_name = input('Nom du Client: ')
            customer_email = input('Email du client: ')
            tel = input('Tel: ')
            company_name = input('Entreprise: ')
            first_date = input('Date création: (format: year-month-day xxxx-xx-xx)')
            last_date = input('Dernier contact: (format: year-month-day xxxx-xx-xx)')
            # Contact: Affectation automatique de l'id contact commercial.
            return full_name, customer_email, tel, company_name, first_date, last_date
        else:
            print("Operation only allowed for Commercial departement !")
            self.commercial_menu_view()


    # Maj client
    def update_own_customer(self, user_role, current_user):
        customer_to_update = self.display_ordered_id_customers()
        print('current_user:', current_user, customer_to_update.id)
        
        customer = session.query(Customer).filter_by(id=customer_to_update.id).one_or_none()
        print('customer:', customer)
         
        if self.get_permission(user_role, UPDATE_OWN_CUSTOMER):
            print('current_user, customer.contact:', current_user, customer.contact)
            if customer.contact != current_user:
                print('Forbidden, this customer is not one of your own customers!')
            else:
                query = session.query(Customer)
                column_names = query.statement.columns.keys()
                print('Choose one key :', column_names[1], column_names[2], column_names[3], column_names[4], column_names[5], column_names[6])
                key_to_update = input('Clé à modifier: ')
                value_to_update = input('Nouvelle valeur:' )
                return customer_to_update.id, key_to_update, value_to_update
        else:
            print("Operation only allowed for Commercial departement !")
        self.commercial_menu_view(current_user, user_role)


    def display_ordered_id_customers(self):
        customers = session.query(Customer).all()
        i = 0
        for elt in customers:
            # Get username from id: (elt.contact)
            user = session.query(User).filter(User.id == elt.contact).first()
            print('N°',i,'. full_name:', elt.full_name,\
            "\n", 'email:', elt.customer_email,\
            "\n", 'tel:', elt.tel,\
            "\n", 'company_name:', elt.company_name,\
            "\n", 'first_date:', elt.first_date,\
            "\n", 'last_date:', elt.last_date,\
            "\n", 'contact:', user.username)
            i = i + 1
        choix = input("Choisir un id customer:")
        customer = customers[int(choix)]
        return customer


    def display_customers(self):
        customers = session.query(Customer).all()
        i = 0
        for elt in customers:
            user = session.query(User).filter(User.id == elt.contact).first()
            print('N°',i,'. Customer:', elt.full_name, elt.customer_email,
                elt.tel, elt.company_name, elt.first_date, elt.last_date, user.username)
            i = i + 1


    def update_own_contract(self, user_role, current_user):
        contract_to_update = self.display_ordered_update_own_contracts()
        # print('Contract_to_update:', contract_to_update, contract_to_update.id)
        contract = session.query(Contract).filter_by(id=contract_to_update.id).one_or_none()
        if self.get_permission(user_role, UPDATE_OWN_CONTRACT):
            if contract.commercial_contact != current_user:
                print('Forbidden, this contract is not one of your own contracts!')
            else:
                query = session.query(Contract)
                column_names = query.statement.columns.keys()
                print('Choose one key :', column_names[3], column_names[4], column_names[5], column_names[6])
                key_to_update = input("Clé à modifier :")
                value_to_update = input("Nouvelle valeur :")
                return contract_to_update.id, key_to_update, value_to_update
        else:
            print("Operation only allowed for Commercial departement !")
        self.commercial_menu_view(user_)

    def display_ordered_update_own_contracts(self):
        contracts = session.query(Contract).all()
        i = 0
        for elt in contracts:
            # Get username from id: (elt.contact)
            user = session.query(User).filter(User.id == elt.commercial_contact).first()
            # Get info customer from customer_id: (elt.customer_id)
            customer = session.query(Customer).filter(Customer.id == elt.customer_info).first()
            print('N°',i,'. Contract_id:', elt.id,\
            "\n", 'customer_info:', customer.full_name, customer.customer_email,\
            "\n", 'tel:',customer.tel,\
            "\n", 'commercial_contact:', user.username,\
            "\n", 'total_amount:', elt.total_amount,\
            "\n", 'balance_payable:', elt.balance_payable,\
            "\n", 'start_date:', elt.start_date,\
            "\n", 'contract_status:', elt.contract_status.value)
            i = i + 1
        choix = input("Choisir un id contrat:")
        contract = contracts[int(choix)]
        return contract


    def display_filtered_contracts(self, user_role):
        contracts = session.query(Contract).filter((Contract.balance_payable > '0') | (Contract.contract_status == 'UNSIGNED')).all()
        i = 0
        for elt in contracts:
            print('N°', i,'. Balance_payable:', elt.balance_payable,
                    "\n", 'status:', elt.contract_status.value)
            i = i + 1
        self.commercial_menu_view()

    def display_ordered_contracts(self):
        contracts = session.query(Contract).all()
        i = 0
        for elt in contracts:
            # Get username from id: (elt.contact)
            user = session.query(User).filter(User.id == elt.commercial_contact).first()
            # Get info customer from customer_id: (elt.customer_id)
            customer = session.query(Customer).filter(Customer.id == elt.customer_info).first()
            print('N°',i,'. Contract_id:', elt.id,\
                    "\n", 'customer_info:', customer.full_name, customer.customer_email,\
                    "\n", 'tel:',customer.tel,\
                    "\n", 'commercial_contact:', user.username,\
                    "\n", 'total_amount:', elt.total_amount,\
                    "\n", 'balance_payable:', elt.balance_payable,\
                    "\n", 'start_date:', elt.start_date,\
                    "\n", 'contract_status:', elt.contract_status.value)
            i = i + 1

    def create_validated_contract_event(self, user_role, current_user):
        contract = self.display_ordered_update_own_contracts()

        print('elt1:', contract)
        contract_id = contract.id
        status = contract.contract_status
        com = contract.commercial_contact
        customer_info = contract.customer_info
        print('status:', contract_id, status, com, customer_info)
        customers = session.query(Customer).all()

        if self.get_permission(user_role, CREATE_SIGNED_OWN_EVENT):
            event_name = input("Nom de l'evenement: ")
            # contract = session.query(Contract).filter_by(id=contract_id).one_or_none()
            # print('contract:', contract)
            # print('contract_id', contract.commercial_contact, user_id)
            if contract.commercial_contact != current_user:
                print('Forbidden, this contract is not one of your own contracts!')
            else:
                if contract.contract_status.value != '1':
                    print('contract_status not signed!')
                    self.commercial_menu_view()
                else:
                    for val in customers:
                        val = session.query(Customer).filter(Customer.id == contract.customer_info).first()
                        customer_name = val.full_name
                        customer_contact = val.id
                        start_date = val.first_date
                        end_date = val.last_date
                        print('vals:', customer_name, customer_contact, start_date, end_date)
                    
                    support_contact = input("Support Contact: id departement support")
                    location = input("Lieu de l'évenement: ")
                    attendees = input("Nombre de participants: ")
                    notes = input("Précisions sur le déroulement de l'évenement: ")
                return event_name, contract_id, customer_name, customer_contact, start_date, end_date, support_contact, location, attendees, notes
        else:
            print("Operation only allowed for Commercial departement !")
        self.commercial_menu_view()



    def display_events(self):
        events = session.query(Event).all()
        i = 0
        for elt in events:
            customer = session.query(Customer).all()
            user = session.query(User).filter(User.id == elt.support_contact).first()
            # Get info customer from customer_id: (elt.customer_id)
            customer = session.query(Customer).filter(Customer.id == elt.customer_contact).first()
            print('N°',i,'. Event_id:', elt.id,\
                        "\n", 'Event name:', elt.event_name,\
                        "\n", 'Customer contact:', customer.full_name, customer.customer_email,\
                        "\n", 'Tel:', customer.tel,\
                        "\n", 'start_date:', elt.start_date,\
                        "\n", 'end_date:', elt.end_date,\
                        "\n", 'support contact:', user.username,\
                        "\n", 'location:', elt.location,\
                        "\n", 'attendees:', elt.attendees,\
                        "\n",  'notes:', elt.notes)
            i = i + 1
