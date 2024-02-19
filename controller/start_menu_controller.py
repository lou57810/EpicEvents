# import os

from view.start_menu_view import StartMenuView
# from view.user_menu_view import UserMenuView
# from view.administration_menu_view import AdministrationMenuView
from .administration_controller import AdministrationController
# from view.start_menu_view import StartMenuView
# from model.users_model import Base  # , engine
# from .admin_controller import AdminController
from .user_controller import UserController
# from .engine_controller import EngineController
# from .engine_controller import engine, session
# import sqlalchemy
# from sqlalchemy.orm import DeclarativeBase
# from sqlalchemy import URL
# from sqlalchemy import create_engine, text, inspect
# from sqlalchemy_utils import database_exists, create_database, drop_database
# import mysql.connector
# from dotenv import load_dotenv, dotenv_values

# load_dotenv()
# db_name = os.getenv('DB_NAME')


class StartMenuController:
    def __init__(self):
        pass


    def run_db(self):           # Administration, Sign in
        main_app = StartMenuView()
        choice = main_app.start_menu_view()

        if choice == "1":
            admin_app = AdministrationController()
            admin_app.start_administration()

        if choice == "2":
            main_app.display_tables()
            print('\n')
            print('Enter Email and then, password: ')
            user_app = UserController()
            user_app.sign_in()


        elif choice == "3":
            print("\n Bye!")
            raise SystemExit
