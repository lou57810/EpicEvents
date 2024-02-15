import os

from view.start_menu_view import StartMenuView
from view.user_menu_view import UserMenuView
from view.database_menu_view import DatabaseMenuView
from model.users_model import Base  # , engine
# from .admin_controller import AdminController
from .user_controller import UserController
from .engine_controller import EngineController
from .engine_controller import engine, session
import sqlalchemy
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import URL
from sqlalchemy import create_engine, text, inspect
from sqlalchemy_utils import database_exists, create_database, drop_database
import mysql.connector
from dotenv import load_dotenv, dotenv_values

load_dotenv()
db_name = os.getenv('DB_NAME')
print('engine3:', engine)

class StartMenuController:
    def __init__(self):
        pass


    def run_db(self):           # Administration, Sign in
        
        # self.display_databases()
        main_app = StartMenuView()
        choice = main_app.start_menu_view()

        if choice == "1":
            self.start_administration()

        if choice == "2":
            self.display_tables()
            print('\n')
            print('Email & password: ')
            user_app = UserController()
            user_app.sign_in()

        elif choice == "3":
            print("\n Bye!")
            raise SystemExit


    def start_administration(self):
        dbApp = DatabaseMenuView()
        choice, dbName = dbApp.menu_db()  # From admin_menu_view

        if choice == 1:
            self.add_database(dbName)

        elif choice == 2:
            pass # dbApp.menu_db()

        elif choice == 3:
            self.delete_db(dbName)

        elif choice == 4:
            print("\n Bye!")
            raise SystemExit


    def add_database(self, dbName):
        # self.display_databases(dbName)
        engine_app = EngineController()
        Engine = engine_app.start_engine(dbName)
        if database_exists(Engine.url):
            print('Database exist:', dbName)
        else:
            create_database(Engine.url)
            Base.metadata.create_all(bind=Engine)
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


    def delete_db(self, dbName):        
        print('engine_url:', engine.url)
        if database_exists(engine.url):
            with engine.connect() as connection:
                result = connection.execute(text('DROP DATABASE' + ' ' + dbName))
                connection.close()
            self.start_administration()
        else:
            print("This database doesn't exist !")
            self.start_administration()

    def display_tables(self):
        # print('Connexion à dbepic ! \n')
        print('TABLES:')
        insp = inspect(engine)
        print(insp.get_table_names())
        
