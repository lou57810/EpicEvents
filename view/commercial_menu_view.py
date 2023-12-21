



class CommercialMenuView:

    def __init__(self):
        pass


    def commercial_menu_view(self):
        print("Choose options")
        answer = True
        while answer:
            print("""
            1. Create customer.
            2. Update customer.
            3. Validate realized contract.
            4. Display filtered contract.
            5. Create event for contract.
            6. Quit.
            """)

            answer = input("Faites votre choix ! \n")
            if answer == "1":
                value = self.set_customer_account()
                return 1, value
            elif answer == "2":
                value = self.update_own_customer()
                return 2, value
            elif answer == "3":
                value = self.update_own_contract()
                return 3, value
            elif answer == "4":
                value = self.display_filtered_contracts()
                return 4, value
            elif answer == "5":
                value = self.create_validated_contract_event()
                return 5, value
            elif answer == "6":
                return 8, None


    def get_customer_data(self):
        ident = input('N° du Client: ')
        full_name = input('Nom du Client: ')
        email = input('Email: ')
        tel = input('Tel: ')
        company_name = input('Entreprise: ')
        first_date = input('Date création: ')
        last_date = input('Dernier contact: ')
        contact = input('Contact commercial chez EpicEvents: ')
        return ident, full_name, email, tel, company_name, first_date, last_date, contact


    def set_customer_account(self):
        # self.display_customer_table(engine)
        value = self.get_customer_data()
        return value



    def update_own_customer(self):
        value = self.get_customer_data()
        return value


    def update_own_contract(self):
        pass


    def display_filtered_contracts(self):
        pass


    def create_validated_contract_event(self):
        contract_name = input("Nom du contrat: ")
        event_id = input("N° de l'évenement: ")
        contract_id = input("N° du contrat: ")
        customer_name = input("Nom du client: ")
        customer_contact = input("Contact nom client, mail et tél: ")
        start_date = input("Date du début de l'évenement': ")
        end_date = input("Date de fin de l'évenement: ")
        support_contact = input("Nom du contact: ")
        location = input("Lieu de l'évenement: ")
        attendees = input("Nombre de participants: ")
        notes = input("Précisions sur le déroulement de l'évenement: ")
        return contract_name, event_id, contract_id, customer_name, customer_contact, start_date, end_date, support_contact, location, attendees, notes
