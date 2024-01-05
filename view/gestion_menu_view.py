
from sqlalchemy import text
from sqlalchemy.orm import Session, sessionmaker
from model.users_model import Collaborator, Events, Contracts
from controller.engine_controller import engine, session


class GestionMenuView:
    def __init__(self):
        pass


    def gestion_menu_view(self):
        print("Choose options")
        answer = True
        while answer:
            print("""
            1. Create collaborator.
            2. Update collaborator.
            3. Delete collaborator.
            4. Create contract.
            5. Update contract.
            6. Display filtered events: No associated support.
            7. Update events.
            8. Quit.
            """)

            answer = input("Faites votre choix ! \n")
            if answer == "1":
                value = self.set_collaborator_account()
                return 1, value
            elif answer == "2":
                value = self.update_collaborator_account()
                return 2, value
            elif answer == "3":
                value = self.get_collaborator_ident()
                return 3, value
            elif answer == "4":
                self.display_contracts()
                value = self.create_contract_data()
                return 4, value
            elif answer == "5":
                self.display_contracts()
                value = self.update_contract_data()
                return 5, value
            elif answer == "6":
                self.display_filtered_events()
            elif answer == "7":
                self.display_events()
                value = self.update_events()
                return 7, value
            elif answer == "8":
                return 8, None

    def get_collaborator_data(self):
        self.display_gestion_table()
        ident = input('Identifiant numérique: ')
        print('/n')
        username = input('Nom du collaborateur: ')
        password = str(input ('Password: '))
        email = input("collaborator email : ")
        role = input('A quel departement est affecte le nouveau collaborateur ?: ')
        return ident, username, password, email, role
        

    def set_collaborator_account(self):
        # self.display_gestion_table(engine)
        value = self.get_collaborator_data()
        return value


    def update_collaborator_account(self):
        self.display_gestion_table()
        value = self.get_collaborator_data()
        return value



    def get_collaborator_ident(self):
        self.display_gestion_table()
        ident = input('Identifiant numérique:' )
        return ident


    def display_gestion_table(self):
       
        collaborators = session.query(Collaborator).all()
        for collaborator in collaborators:
            print(f"id: {collaborator.id}, ident: {collaborator.ident}, username: {collaborator.username}, mail: {collaborator.email}, role: {collaborator.role}")


    """def get_or_update_contract_data(self):
        contract_id = input('Idenfifiant numérique: ')
        customer_info = input('Informations sur le client: ')
        commercial_contact = input('Contact commercial associé au client: ')
        total_amount = input('Montant total du contrat: ')
        balance_payable = input('Montant restant à payer: ')
        start_date = input('Date de création du contrat: ')
        contract_status = input('Contrat signé ou non ? ')
        return contract_id, customer_info, commercial_contact, total_amount, balance_payable, start_date, contract_status"""

    def create_contract_data(self):
        contract_id = input('Idenfifiant numérique: ')
        customer_info = input('Informations sur le client: ')
        commercial_contact = input('Contact commercial associé au client: ')
        total_amount = input('Montant total du contrat: ')
        balance_payable = input('Montant restant à payer: ')
        start_date = input('Date de création du contrat: ')
        contract_status = input('Contrat signé ou non ? ')
        return contract_id, customer_info, commercial_contact, total_amount, balance_payable, start_date, contract_status


    def update_contract_data(self):
        contract_to_update = input('N° du contrat: ')
        attribut_to_update = input('Attribut à modifier: ')
        new_attribut_value = input('Nouvelle valeur: ')
        return contract_to_update, attribut_to_update, new_attribut_value


    def display_filtered_events(self):   # affiche tous les événements qui n’ont pas de « support » associé.
        event = session.query(Events).filter_by(support_contact="").all()
        print('event:', event)


    def update_events(self):
        event_to_update = input('N° de l\'evenement :')
        attribut_to_update = input("Attribut à modifier :")
        new_attribut_value = input("Nouvelle valeur :")
        return event_to_update, attribut_to_update, new_attribut_value


    def display_events(self):
        events = session.query(Events).all()
        for event in events:
            print(f"event_name: {event.event_name}, event_id: {event.event_id}, contract_id: {event.contract_id}, customer_name: {event.customer_name}, customer_contact: {event.customer_contact}, start_date: {event.start_date}, end_date: {event.end_date}, support_contact: {event.support_contact}, location: {event.location}, attendees: {event.attendees}, notes: {event.notes}, \n")


    def display_contracts(self):
        contracts = session.query(Contracts).all()
        for contract in contracts:
            print(f"contract_id: {contract.contract_id}, customer_info: {contract.customer_info}, commercial_contact: {contract.commercial_contact}, total_amount: {contract.total_amount}, balance_payable: {contract.balance_payable}, start_date: {contract.start_date}, contract_status: {contract.contract_status}, \n")



