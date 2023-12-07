import os
import mysql.connector

from getpass import getpass
import keyring
from mysql.connector import connect, Error
import sqlalchemy
from sqlalchemy import URL
from sqlalchemy import create_engine, ForeignKey, text, select, inspect # Column, String, Integer, CHAR
# from sqlalchemy.ext.declarative_base import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, create_database, drop_database
from sqlalchemy.orm import DeclarativeBase
from view.admin_menu_view import AdminMenuView
from view.user_menu_view import UserMenuView
from model.users_model import Base, Collaborator, Customer
from .user_controller import UserController
# from view.user_menu_view import UserMenuView




class AdminController:
    def __init__(self, db_name):
        # self.db_name = db_name
        pass

    # def __init__(self, db_name, username, password):
        # self.db_name = db_name
        # self.username = username
        # self.password = password


    def start_db(self, db_name):
        
        dbApp = AdminMenuView()
        choice, db_name = dbApp.admin_menu_db()  # From admin_menu_view

        if choice == 1:
            # self.create_db_connection(db_name, self.username, self.password)
            self.create_db_connection(db_name)
            self.start_db(db_name)

        elif choice == 2:
            self.delete_db(db_name)
            self.start_db(db_name)

        elif choice == 3:
            print("\n Bye!")
            raise SystemExit
 


    # def create_db_connection(self, db_name, username, password):
    def create_db_connection(self, db_name):
        username = os.environ.get('DB_USER')
        password = os.environ.get('DB_PASS')
        user_app = UserMenuView()
        user_app_controller = UserController()
        engine = create_engine("mysql+pymysql://" + username + ":" + password + "@localhost/" + db_name)
        
        if not database_exists(engine.url):
            create_database(engine.url)
            print('Nouvelle Base de donnees:', db_name)
            self.display_databases(db_name)
            Base.metadata.create_all(bind=engine)

        else:
            with engine.connect() as connection:
                result = connection.execute(text('select "Hello"'))
                print('result:', result.all())
                print('You are connected with: ', db_name)
                # self.display_tables(engine)
                



    def delete_db(self, db_name):
        conn = self.db_connect()
        # conn = self.create_db_connection(db_name)
        

        try:
            # Create a cursor object
            if conn.is_connected():
                
                mycursor = conn.cursor()
                # SQL Statement to delete a database
                mycursor.execute('DROP DATABASE' + ' ' + db_name)
                print(db_name, ' Deleted')

        except Exception as e:
            print("Exception occured:{}".format(e))
        finally:
            self.display_databases(db_name)
            # conn.close()
        # self.start_db()
        

    
    def db_connect(self):
        username = os.environ.get('DB_USER')
        password = os.environ.get('DB_PASS')
        conn = mysql.connector.connect(
            username = username,
            password = password,
            host="localhost",
            )
        return conn
    


    def display_databases(self, db_name):
        conn = self.db_connect()
        # conn = self.create_db_connection(db_name)
        

        try:
            # Create a cursor object
            if conn.is_connected():
                # print('Connected to MySQL database')
                mycursor = conn.cursor()
                mycursor.execute("SHOW DATABASES")
                rows = mycursor.fetchall()
                for row in rows:
                    print(row)

        except Exception as e:
            print("Exception occured:{}".format(e))
        finally:
            conn.close()

 
