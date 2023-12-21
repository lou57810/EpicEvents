
from sqlalchemy import text
from sqlalchemy.orm import Session, sessionmaker
from model.users_model import Collaborator
from controller.engine_controller import engine


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
            6. Display events.
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
                value = self.get_or_update_contract_data()
                return 4, value
            elif answer == "5":
                value = self.get_or_update_contract_data()
                return 5, value
            elif answer == "6":
                value = self.display_filtered_events()
                return 6, value
            elif answer == "7":
                value = self.update_events(self)
                return 7, value
            elif answer == "8":
                return 8, None

    def get_collaborator_data(self):
        self.display_gestion_table(engine)
        ident = input('Identifiant numérique: ')
        print('/n')
        username = input('Nom du collaborateur: ')
        password = input ('Password: ')
        email = input("collaborator email : ")
        role = input('A quel departement est affecte le nouveau collaborateur ?: ')
        return ident, username, password, email, role
        

    def set_collaborator_account(self):
        # self.display_gestion_table(engine)
        value = self.get_collaborator_data()
        return value


    def update_collaborator_account(self):
        self.display_gestion_table(engine)
        value = self.get_collaborator_data()
        return value



    def get_collaborator_ident(self):
        self.display_gestion_table(engine)
        ident = input('Identifiant numérique:' )
        return ident


    def display_gestion_table(self, engine):
        with engine.connect() as conn:
            result = conn.execute(text("select * from collaborators"))
            for row in result:
                print('Collaborators:', row)


    def get_or_update_contract_data(self):
        contract_id = input('Idenfifiant numérique: ')
        customer_info = input('Informations sur le client: ')
        commercial_contact = input('Contact commercial associé au client: ')
        total_amount = input('Montant total du contrat: ')
        balance_payable = input('Montant restant à payer: ')
        start_date = input('Date de création du contrat: ')
        contract_status = input('Contrat signé ou non ? ')
        return contract_id, customer_info, commercial_contact, total_amount, balance_payable, start_date, contract_status


    def display_filtered_events(self):   # afficher tous les événements qui n’ont pas de « support » associé.
        pass


    def update_events(self):    # pour associer un collaborateur support à l’événement)
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
    

