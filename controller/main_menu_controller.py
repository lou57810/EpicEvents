import os

from view.main_menu_view import MainMenuView
from view.user_menu_view import UserMenuView
from view.admin_menu_view import AdminMenuView
from model.users_model import Base  # , engine
# from .admin_controller import AdminController
from .user_controller import UserController
from .engine_controller import EngineController
from .engine_controller import engine
import sqlalchemy
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import URL
from sqlalchemy import create_engine, text
from sqlalchemy_utils import database_exists, create_database, drop_database
import mysql.connector



class MainMenuController:
    def __init__(self):
        pass


    def run_db(self):           # Administration, Sign in
        self.display_databases()
        main_app = MainMenuView()
        choice = main_app.main_menu_view()

        if choice == "1":
            self.start_administration()

        if choice == "2":
            self.display_tables()
            print('\n')
            user_app = UserController()
            user_app.sign_in()

        elif choice == "3":
            print("\n Bye!")
            raise SystemExit


    def start_administration(self):
        
        dbApp = AdminMenuView()
        choice, db_name = dbApp.admin_menu_db()  # From admin_menu_view

        if choice == 1:
            self.add_database(db_name)

        elif choice == 2:
            self.delete_db(db_name)

        elif choice == 3:
            print("\n Bye!")
            raise SystemExit


    def add_database(self, db_name):
        engine_app = EngineController()
        engine = engine_app.start_engine(db_name)

        if not database_exists(engine.url):
            create_database(engine.url)
            Base.metadata.create_all(bind=engine)
            self.display_databases()

        else:
            print('Database exist:', db_name)
            self.display_databases()

        self.start_administration()


    """
    def update_db(self, db_name):
        engine_app = EngineController()
        engine = engine_app.start_engine(db_name)
        Base.metadata.create_all(bind=engine)
        with engine.connect() as connection:
            result = connection.execute(text('select "Update done"'))
            print('result:', result.all())
            print('You are connected with: ', db_name)
        self.start_administration()
    """


    def delete_db(self, db_name):
        engine_app = EngineController()
        engine = engine_app.start_engine(db_name)

        with engine.connect() as connection:
            result = connection.execute(text('DROP DATABASE' + ' ' + db_name))
            self.display_databases()
            connection.close()
        self.start_administration()


    def display_databases(self):
        print('Mysql is starting ! \n')
        print('DATABASES:')
        
        with engine.connect() as connection:
            result = connection.execute(text("SHOW DATABASES"))
            for x in result:
                print(x)


    def display_tables(self):
        print('Connexion à dbepic ! \n')
        print('TABLES:')
        
        with engine.connect() as connection:
            result = connection.execute(text("SHOW TABLES"))
            for x in result:
                print(x)
