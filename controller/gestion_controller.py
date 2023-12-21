import bcrypt
from sqlalchemy import text, update
from sqlalchemy.orm import Session, sessionmaker
from view.gestion_menu_view import GestionMenuView
from .engine_controller import EngineController
from model.users_model import Collaborator, Contracts
from .engine_controller import engine




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
            self.display_filtered_events()
        elif choice == 7:
            self.update_events()
        elif choice == 8:
            print("\n Bye!")
            raise SystemExit


    def create_collaborator(self, values):
        # crypt_app = CryptoController()
        ident, username, password, email, role = values

        # Création Collaborator = Input mot de passe: password =>bd
        bytes = password.encode('utf-8')
        salt = bcrypt.gensalt()
        print('salt:', salt)
        hashed_password = bcrypt.hashpw(bytes, salt)
        print('hashed_password:', bcrypt.hashpw(bytes, salt))
        
        Session = sessionmaker(bind=engine)
        session = Session()

        user = Collaborator(ident, username, password, hashed_password, email, role)
        
        session.add(user)   # stage
        session.commit()    # push
        
        with engine.connect() as conn:
            result = conn.execute(text("select * from collaborators"))
            for rows in result:
                print("Collaborators:", rows)
        self.gestion_menu_controller()     # Retour menu gestion"""


    def update_collaborator(self, values):
        ident, new_username, new_password, new_email, new_role = values

        bytes = new_password.encode('utf-8')
        salt = bcrypt.gensalt()
        
        hashed_password = bcrypt.hashpw(bytes, salt)
        print('hashed_password:', bcrypt.hashpw(bytes, salt))

        Session = sessionmaker(bind=engine)
        session = Session()
        collaborator = session.query(Collaborator).filter_by(ident=ident).one_or_none()

        collaborator.ident = ident
        collaborator.username = new_username
        collaborator.password = new_password
        collaborator.salt = salt
        # self.encrypt_passwd(new_password)
        collaborator.email = new_email
        collaborator.role = new_role
        session.commit()

        self.gestion_menu_controller()


    def delete_collaborator(self, values):
        ident = values
        Session = sessionmaker(bind=engine)
        session = Session()

        collaborator = session.query(Collaborator).filter_by(ident=ident).one_or_none()

        session.delete(collaborator)
        session.commit()

        menu_app = GestionMenuView()
        menu_app.display_gestion_table(engine)

        self.gestion_menu_controller()


    def create_contract(self, values):
        contract_id, customer_info, commercial_contact, total_amount, balance_payable, start_date, contract_status = values

        Session = sessionmaker(bind=engine)
        session = Session()

        contract = Contracts(contract_id, customer_info, commercial_contact, total_amount, balance_payable, start_date, contract_status)
        # contract = Contracts(values)
        
        session.add(contract)   # stage
        session.commit()    # push

        with engine.connect() as conn:
            result = conn.execute(text("select * from contracts"))
            for rows in result:
                print("Contracts:", rows)
        self.gestion_menu_controller()     # Retour menu gestion"""


    def update_contract(self, values):
        contract_id, customer_info, commercial_contact, total_amount, balance_payable, start_date, contract_status = values
        

        Session = sessionmaker(bind=engine)
        session = Session()
        contract = session.query(Contracts).filter_by(contract_id=contract_id).one_or_none()

        contract.contract_id = contract_id
        contract.customer_info = customer_info
        contract.commercial_contact = commercial_contact
        contract.total_amount = total_amount
        contract.balance_payable = balance_payable
        contract.start_date = start_date
        contract.contract_status = contract_status

        session.commit()
        self.gestion_menu_controller()


    def display_filtered_events(self):
        pass


    def update_events(self):
        pass