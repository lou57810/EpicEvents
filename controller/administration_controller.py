import os
import bcrypt
# import mysql.connector
from sqlalchemy_utils import create_database, database_exists   # , drop_database
from sqlalchemy import text # , inspecttext
from sqlalchemy.orm import sessionmaker # Session,
from model.users_model import Base, User
from view.administration_menu_view import AdministrationMenuView
from .engine_controller import EngineController



class AdministrationController:
    def __init__(self, start_controller):
        self.start_controller = start_controller
         

    def start_administration(self):
        dbApp = AdministrationMenuView()
        dbApp.display_databases()
        choice, dbName = dbApp.administration_menu_view()  # From admin_menu_view
            
        if choice == 1:
            self.add_database(dbName)
        elif choice == 2:
            self.create_admin_user(dbName)
        elif choice == 3:
            self.delete_db(dbName)
        elif choice == 4:
            self.return_menu()
        elif choice == 5:
            self.start_controller.run_db()


    def add_database(self, dbName):
        engine_app = EngineController()
        Engine = engine_app.start_engine(dbName)
        if database_exists(Engine.url):
            print('Database exist:', dbName)
        else:
            create_database(Engine.url)
            Base.metadata.create_all(bind=Engine)
            dbApp = AdministrationMenuView()
            dbApp.display_tables()
        self.start_administration()


    def delete_db(self, dbName):
        
        engine_app = EngineController()
        Engine = engine_app.start_engine(dbName)
        print('engine_url:', Engine.url)
        if database_exists(Engine.url):
            with Engine.connect() as connection:
                connection.execute(text('DROP DATABASE' + ' ' + dbName))
                connection.close()
            self.start_administration()
        else:
            print("This database doesn't exist !")
            self.start_administration()


    def create_admin_user(self, dbName):
        app = EngineController()
        Engine = app.start_engine(dbName)
        Session = sessionmaker(bind=Engine)
        Session = Session()
        user_id = Session.query(User).filter_by(id=1).one_or_none()
        # print('user_id:', user_id)
        if user_id:
            print('\n')
            print('SuperUser déjà créé:')
            print('email:', user_id.email, 'password:', user_id.password, 'role:', user_id.role, '\n')
            self.start_administration()
        else:
            # Values from .env
            username = os.getenv("DB_ADMIN")
            password = os.getenv("DB_ADMIN_PASS")
            email = os.getenv("DB_ADMIN_MAIL")
            role = os.getenv("DB_DEPARTMENT")

            bytes = password.encode('utf-8')
            hashed_password = bcrypt.hashpw(bytes, bcrypt.gensalt())
            user = User(username, password, hashed_password, email, role)
            Session.add(user)   # stage
            Session.commit()    # push

            print('Email:', email, 'Password:', password, 'Role:', role)
            self.start_administration()

    def return_menu(self):
        self.start_administration()