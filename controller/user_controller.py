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
from model.users_model import User # , Customer, Base, 
# from sqlalchemy.orm import Session, sessionmaker
# import pymysql.cursors
# import pymysql
from .engine_controller import session   # engine,
from view.start_menu_view import StartMenuView


class UserController:

    current_user = None
    def __init__(self, start_controller):
        self.start_controller = start_controller
        self.gestion_controller = GestionController(self)
        self.commercial_controller = CommercialController(self)
        self.support_controller = SupportController(self)



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
                print('\n')
                print('Signed in dbepic as user:', user_row.username, ', email:', user_row.email, '\n')

                # Redirection en fonction du rôle
                # self.department_redirect(user_row.id, user_row.role.value)
                self.current_user = user_row  # A substituer as id
                self.department_redirect()
            else:
                print('Pass incorrect ! retry.')
                self.sign_in()


    # Redirection en fonction de l'id collaborateur, et du rôle
    def department_redirect(self):
        print('#### DEPARTMENT', self.current_user.role.name, '####\n')
        if self.current_user.role.value == "1":     # user_controller
        # if self.current_user.role == "1":     # user_controller
            self.gestion_controller.gestion_menu_controller()
        elif self.current_user.role.value == "2":
        # elif self.current_user.role == "2":
            self.commercial_controller.commercial_menu_controller()
        elif self.current_user.role.value == "3":
        # elif self.current_user.role == "3":
            self.support_controller.support_menu_controller()
