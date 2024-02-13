import os
import datetime


import bcrypt
import requests
import jwt
from .engine_controller import EngineController
from .gestion_controller import GestionController
# from .main_controller import MainController
from .commercial_controller import CommercialController
from .support_controller import SupportController
from mysql.connector import connect, Error
# from view.user_menu_view import UserMenuView
from view.start_menu_view import StartMenuView
import sqlalchemy 
from sqlalchemy import URL, insert, create_engine, ForeignKey, text, inspect, select
from sqlalchemy_utils import database_exists, create_database, drop_database
import mysql.connector
from mysql.connector import connect, Error
from model.users_model import Base, User, Customer
from sqlalchemy.orm import Session, sessionmaker
import pymysql.cursors
import pymysql
from .engine_controller import engine, session
from view.start_menu_view import StartMenuView




class UserController:
    def __init__(self):
        pass


    def sign_in(self):
        # user_app = UserMenuView()
        start_app = StartMenuView()
        input_email, input_password = start_app.user_sign_in()
        all_users = session.query(User).all()

        user_row = session.query(User).filter_by(email=input_email).one_or_none()
        # print('user_row:', user_row)
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
                self.department_redirect(user_row.id, user_row.role.value)
            else:
                print('Pass incorrect ! retry.')
                self.sign_in()
        

    # Redirection en fonction de l'id collaborateur, et du rôle
    def department_redirect(self, id, role):
        if role == 'gestion':
            gestion_app = GestionController()
            gestion_app.gestion_menu_controller(id, role)
        elif role == 'support':
            support_app = SupportController()
            support_app.support_menu_controller(id, role)
        elif role == 'commercial':
            commercial_app = CommercialController()
            commercial_app.commercial_menu_controller(id, role)
