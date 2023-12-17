import bcrypt
from sqlalchemy import text, update
from sqlalchemy.orm import Session, sessionmaker
from view.gestion_menu_view import GestionMenuView
from .engine_controller import EngineController
from model.users_model import Collaborator
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
            print("\n Bye!")
            raise SystemExit


    def create_collaborator(self, values):
        # crypt_app = CryptoController()
        ident, username, password, email, role = values

        # Création Collaborator = Input mot de passe: password =>bd
        bytes = password.encode('utf-8')
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(bytes, salt)
        print('hashed_password:', bcrypt.hashpw(bytes, salt))
        
        Session = sessionmaker(bind=engine)
        session = Session()

        user = Collaborator(ident, username, password, salt, email, role)
        
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


    


    
        

