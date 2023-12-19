import os
import datetime

import bcrypt
import requests
import jwt
from .engine_controller import EngineController
from .gestion_controller import GestionController
from .commercial_controller import CommercialController
from .support_controller import SupportController
from mysql.connector import connect, Error
from view.user_menu_view import UserMenuView
import sqlalchemy 
from sqlalchemy import URL, insert, create_engine, ForeignKey, text, inspect, select
from sqlalchemy_utils import database_exists, create_database, drop_database
import mysql.connector
from mysql.connector import connect, Error
from model.users_model import Base, Collaborator, Customer
from sqlalchemy.orm import Session, sessionmaker
import pymysql.cursors
import pymysql
from .engine_controller import engine




class UserController:
    def __init__(self):
        pass


    def sign_in(self):
        user_app = UserMenuView()
        login_email, login_password = user_app.user_sign_in()
        
        # Login: input = password
        password = b"login_password"
        hashed = bcrypt.hashpw(password, bcrypt.gensalt())

        with engine.connect() as conn:
            result = conn.execute(text("select * from collaborators"))
            logged = False
            for row in result:
                if (row[5] == login_email) & (bcrypt.checkpw(password, hashed) == True):
                    print('You are logged in dbepic as :', login_email, ', departement: ', row[6])
                    print('logged_row:', row)
                    self.departement_redirect(row[6])
                    logged = True
            if logged == False:
                print('User or Pass incorrect ! retry.')



    def departement_redirect(self, departement):
        if departement == 'gestion':
            gestion_app = GestionController()
            gestion_app.gestion_menu_controller()
        elif departement == 'support':
            support_app = SupportController()
            support_app.support_menu_controller()
        elif departement == 'commercial':
            commercial_app = CommercialController()
            commercial_app.commercial_menu_controller()