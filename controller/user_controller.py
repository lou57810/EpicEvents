import bcrypt
# import requests
# import jwt

# from .engine_controller import EngineController
from .gestion_controller import GestionController
# from .main_controller import MainController
from .commercial_controller import CommercialController
from .support_controller import SupportController
# from mysql.connector import connect, Error
# from view.user_menu_view import UserMenuView
# from view.start_menu_view import StartMenuView
# import sqlalchemy 
# from sqlalchemy import text, inspect, select        # ForeignKey, URL, create_engine, insert, 
# from sqlalchemy_utils import database_exists, create_database, drop_database
# import mysql.connector
# from mysql.connector import connect, Error
from model.users_model import User  # , Customer, Base, 
# from sqlalchemy.orm import Session, sessionmaker
# import pymysql.cursors
# import pymysql
from .engine_controller import session   # engine,
from view.start_menu_view import StartMenuView


class UserController:

    current_user = None
    def __init__(self):
        pass


    def sign_in(self):
        start_app = StartMenuView()
        input_email, input_password = start_app.user_sign_in()
        user_row = session.query(User).filter_by(email=input_email).one_or_none() 
        if user_row == None:
            print('Bad email!')
            self.sign_in()

        else:
            check = input_password.encode('utf-8')

            db_hash = user_row.hashed_pass  # valeur hashed & salted dans la base de données
            db_hash = db_hash.encode('utf-8')

            if bcrypt.checkpw(check, db_hash):
                print('You are logged in dbepic as id :', user_row.id,\
                        'email: ', user_row.email,\
                        'departement: ', user_row.role.value)

                # Redirection en fonction du rôle
                # self.department_redirect(user_row.id, user_row.role.value)
                UserController.current_user = user_row  # A substituer as id
                self.department_redirect()
            else:
                print('Pass incorrect ! retry.')
                self.sign_in()


    # Redirection en fonction de l'id collaborateur, et du rôle
    def department_redirect(self):
        if UserController.current_user.role.value == "1":     # user_controller
            gestion_app = GestionController()
            gestion_app.gestion_menu_controller()
        elif UserController.current_user.role.value == "2":
            commercial_app = CommercialController()
            commercial_app.commercial_menu_controller()
        elif UserController.current_user.role.value == "3":
            support_app = SupportController()
            support_app.support_menu_controller()
