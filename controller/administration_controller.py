import os
import bcrypt
# import mysql.connector
from sqlalchemy_utils import create_database, database_exists
from model.user import User
from model.base import Base
from sqlalchemy import text  # inspecttext
from sqlalchemy.orm import sessionmaker  # Session
from view.administration_menu_view import AdministrationMenuView
from .engine_controller import EngineController


class AdministrationController:
    def __init__(self, start_controller):
        self.start_controller = start_controller
        self.admin_menu = AdministrationMenuView()

    def start_administration(self):
        choice, dbName = self.admin_menu.administration_menu_view()

        if choice == 1:
            self.add_database(dbName)
        elif choice == 2:
            self.create_admin_user(dbName)
        elif choice == 3:
            self.delete_db(dbName)
        elif choice == 4:
            self.admin_menu.display_databases()
            self.start_administration()
        elif choice == 0:
            self.start_controller.start_dbepic_app()

    def add_database(self, dbName):
        engine_app = EngineController()
        Engine = engine_app.start_engine(dbName)
        if database_exists(Engine.url):
            print('Database existing, choose another name !')
            self.start_administration()
        else:
            create_database(Engine.url)     # Fct from alchemy_utils
            Base.metadata.create_all(bind=Engine)
            test_list = self.admin_menu.display_databases()
            print('test:', test_list)
            for elt in test_list:
                if elt[0] == dbName:
                    print('Database is created')
                    self.admin_menu.display_databases()
                    self.start_administration()

    def delete_db(self, dbName):
        engine_app = EngineController()
        Engine = engine_app.start_engine(dbName)
        if database_exists(Engine.url):
            with Engine.connect() as connection:
                connection.execute(text('DROP DATABASE' + ' ' + dbName))
                connection.close()
            print('Database is suppressed.')
            self.admin_menu.display_databases()
            self.start_administration()
        else:
            print("This database doesn't exist !")
            self.start_administration()

    def create_admin_user(self, dbName):
        app = EngineController()
        Engine = app.start_engine(dbName)
        Session = sessionmaker(bind=Engine)
        Session = Session()
        user_name = Session.query(
            User).filter(User.username == "admin").one_or_none()
        print('Test apres Session, username')
        print('username:', user_name)

        if user_name:
            print('\n')
            print('SuperUser déjà créé:\n')
            self.start_administration()
        else:
            # Values from .env
            username = os.getenv("DB_ADMIN")
            password = os.getenv("DB_ADMIN_PASS")
            email = os.getenv("DB_ADMIN_MAIL")
            role = os.getenv("ROLE")

            bytes = password.encode('utf-8')
            hashed_password = bcrypt.hashpw(bytes, bcrypt.gensalt())
            user = User(username, password, hashed_password, email, role)
            print('user:', user)
            Session.add(user)   # stage
            Session.commit()    # push

            print('Email:', email, 'Password:', password, 'Role:', role)
            self.start_administration()
