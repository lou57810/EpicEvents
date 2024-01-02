import bcrypt
from sqlalchemy import text, update, select
from sqlalchemy.orm import Session, sessionmaker
from view.gestion_menu_view import GestionMenuView
from .engine_controller import EngineController
from model.users_model import Collaborator, Contracts, Events
from .engine_controller import engine, session




class GestionController:
    def __init__(self):
        pass


    def gestion_menu_controller(self):           # Administration, Sign in
        menu_app = GestionMenuView()
        choice, values = menu_app.gestion_menu_view()
        
        if choice == 1:
            self.create_collaborator(values)
        elif choice == 2:
            self.update_collaborator(values)
        elif choice == 3:
            self.delete_collaborator(values)
        elif choice == 4:
            self.create_contract(values)
        elif choice == 5:
            self.update_contract(values)
        elif choice == 6:
            pass
        elif choice == 7:
            self.update_events(values)
        elif choice == 8:
            print("\n Bye!")
            raise SystemExit


    def create_collaborator(self, values):
        ident, username, password, email, role = values

        # Création Collaborator = Input mot de passe: password =>bd
        bytes = password.encode('utf-8')
        salt = bcrypt.gensalt()
        # print('salt:', salt)
        hashed_password = bcrypt.hashpw(bytes, salt)
        
        user = Collaborator(ident, username, password, hashed_password, email, role)
        
        session.add(user)   # stage
        session.commit()    # push
        
        collaborators = session.query(Collaborator).all()
        for collaborator in collaborators:
            print(f"id: {collaborator.id}, ident: {collaborator.ident}, username: {collaborator.username}, email: {collaborator.email}, role: {collaborator.role}")
        self.gestion_menu_controller()     # Retour menu gestion"""


    def update_collaborator(self, values):
        ident, new_username, new_password, new_email, new_role = values

        bytes = new_password.encode('utf-8')
        salt = bcrypt.gensalt()
        
        hashed_password = bcrypt.hashpw(bytes, salt)
        print('hashed_password:', bcrypt.hashpw(bytes, salt))
        
        collaborator = session.query(Collaborator).filter_by(ident=ident).one_or_none()

        collaborator.ident = ident
        collaborator.username = new_username
        collaborator.password = new_password
        collaborator.salt = salt
        collaborator.email = new_email
        collaborator.role = new_role
        session.commit()

        self.gestion_menu_controller()


    def delete_collaborator(self, values):
        ident = values

        collaborator = session.query(Collaborator).filter_by(ident=ident).one_or_none()

        session.delete(collaborator)
        session.commit()

        menu_app = GestionMenuView()
        menu_app.display_gestion_table(engine)

        self.gestion_menu_controller()


    def create_contract(self, values):
        contract_id, customer_info, commercial_contact, total_amount, balance_payable, start_date, contract_status = values

        contract = Contracts(contract_id, customer_info, commercial_contact, total_amount, balance_payable, start_date, contract_status)
        
        session.add(contract)   # stage
        session.commit()    # push

        with engine.connect() as conn:
            result = conn.execute(text("select * from contracts"))
            for rows in result:
                print("Contracts:", rows)
        self.gestion_menu_controller()     # Retour menu gestion


    """def update_contract(self, values):
        contract_id, customer_info, commercial_contact, total_amount, balance_payable, start_date, contract_status = values
        
        contract = session.query(Contracts).filter_by(contract_id=contract_id).one_or_none()

        contract.contract_id = contract_id
        contract.customer_info = customer_info
        contract.commercial_contact = commercial_contact
        contract.total_amount = total_amount
        contract.balance_payable = balance_payable
        contract.start_date = start_date
        contract.contract_status = contract_status

        session.commit()
        self.gestion_menu_controller()"""


    def update_contract(self, values):
        contract_id, attribut_to_update, new_attribut_value = values

        contract = session.query(Contracts).filter_by(contract_id=contract_id).one_or_none()
        print('contract_to_update:', contract)
        # print('contrac.attribut:', contract.attribut_to_update) # ==>  'Contract' object has no attribute 'attribut_to_update'
        print('attribut: ', attribut_to_update)
        query = session.query(Contracts)
        column_names = query.statement.columns.keys()
        print('col:', column_names)
        for elt in column_names:

            if elt == attribut_to_update:
                if attribut_to_update == 'contract_id':
                    contract.contract_id = new_attribut_value
                elif attribut_to_update == 'customer_info':
                    contract.customer_info = new_attribut_value
                elif attribut_to_update == 'commercial_contact':
                    contract.commercial_contact = new_attribut_value
                elif attribut_to_update == 'total_amount':
                    contract.total_amount = new_attribut_value
                elif attribut_to_update == 'balance_payable':
                    contract.balance_payable = new_attribut_value
                elif attribut_to_update == 'start_date':
                    contract.start_date = new_attribut_value
                elif attribut_to_update == 'contract_status':
                    contract.contract_status = new_attribut_value

        print('new session:', session.commit())
        session.commit()
        

        # menu_app = GestionMenuView()        # Affichage update
        # menu_app.display_contracts()
        
        self.gestion_menu_controller()      # Retour au menu
                



    def update_events(self, values):
        event_id, attribut_to_update, new_attribut_value = values

        event = session.query(Events).filter_by(event_id=event_id).one_or_none()
        print('event_to_update:', event)
        # print('event.attribut:', event.attribut_to_update) # ==>  'Events' object has no attribute 'attribut_to_update'
        print('attribut: ', attribut_to_update)
        query = session.query(Events)
        column_names = query.statement.columns.keys()
        print('col:', column_names)
        for elt in column_names:
            
            if elt == attribut_to_update:
                if attribut_to_update == 'event_name':
                    event.event_name = new_attribut_value
                elif attribut_to_update == 'event_id':
                    event.event_id = new_attribut_value
                elif attribut_to_update == 'contract_id':
                    event.contract_id = new_attribut_value
                elif attribut_to_update == 'customer_name':
                    event.customer_name = new_attribut_value
                elif attribut_to_update == 'customer_contact':
                    event.customer_contact = new_attribut_value
                elif attribut_to_update == 'start_date':
                    event.start_date = new_attribut_value
                elif attribut_to_update == 'end_date':
                    event.end_date = new_attribut_value
                elif attribut_to_update == 'support_contact':
                    event.support_contact = new_attribut_value
                elif attribut_to_update == 'location':
                    event.location = new_attribut_value
                elif attribut_to_update == 'attendees':
                    event.attendees = new_attribut_value
                elif attribut_to_update == 'notes':
                    event.notes = new_attribut_value
        
                    
                    
                    #, customer_name, customer_contact, start_date, end_date, support_contact, location, attendees, notes
                # attribut_to_update = elt
                # event.insert(1, new_attribut_value)
                # print('elt:', elt)
                # event. = new_attribut_value
                
        # event.contract_name = new_attribut_value
        # print('event.attrib:', attribut_to_update, event.attribut_to_update)
        print('new session:', session.commit())
        session.commit()
        

        menu_app = GestionMenuView()        # Affichage update
        menu_app.display_events()
        
        self.gestion_menu_controller()      # Retour au menu
