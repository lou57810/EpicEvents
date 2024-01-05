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
from .engine_controller import engine, session




class UserController:
    def __init__(self):
        pass


    def sign_in(self):
        user_app = UserMenuView()
        email, check = user_app.user_sign_in()
        check = check.encode('utf-8')
        print('check:', check)

        user_row = session.query(Collaborator).filter_by(email=email).one_or_none()
        print('user_row:', user_row, user_row.email)
        db_hash = user_row.hashed_pass  # valeur hashed & salted dans la base de données
        db_hash = db_hash.encode('utf-8')
        print('db_hash:', db_hash)

        if bcrypt.checkpw(check, db_hash):
                    
            print('You are logged in dbepic as :', user_row.email, ', departement: ', user_row.role)
            print('logged_row:', user_row)
            # Redirection en fonction du rôle
            self.departement_redirect(user_row.email, user_row.role)
        else:
            print('User or Pass incorrect ! retry.')


    # Redirection en fonction du rôle
    def departement_redirect(self, email, departement):
        if departement == 'gestion':
            gestion_app = GestionController()
            gestion_app.gestion_menu_controller()
        elif departement == 'support':
            support_app = SupportController()
            support_app.support_menu_controller(email)
        elif departement == 'commercial':
            commercial_app = CommercialController()
            commercial_app.commercial_menu_controller()