import os
from mysql.connector import connect, Error
from view.user_menu_view import UserMenuView
import sqlalchemy 
from sqlalchemy import URL, insert
from sqlalchemy import create_engine, ForeignKey, text, inspect
from sqlalchemy_utils import database_exists, create_database, drop_database
import mysql.connector
from mysql.connector import connect, Error
from model.users_model import Base, Collaborator, Customer
# from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Session
import pymysql.cursors
import pymysql

# Connect to the database



class UserController:
    def __init__(self):
        pass


    def run_table(self, db_name):
        
        self.create_db_connection(db_name)
        self.display_tables(db_name)
        menu_user = UserMenuView()
        choice, value_table = menu_user.user_menu_view(db_name)    # value = table_name
        
            
        if choice == 1:
            # print('table_name: ', value)
            self.create_collaborator(value_table)

        elif choice == 2:
            print("\n Bye!")
            raise SystemExit
        

        
        # return
    def create_collaborator(self, value_table):
        db_name, ident, username, password, email, role = value_table
        connection = self.create_db_connection(db_name, self.username, self.password)
        mycursor = connection.cursor()
        mycursor.execute("select * from collaborators")
        for i in mycursor:
            print('Collaborators:', i)
        sql = "INSERT INTO collaborators (ident, username, email, password, role) VALUES (%d, %s, %s, %s, %s)"
        val = ("ident", "username", "email", "password", "role")

        mycursor.execute(sql, val)
        connection.commit()


    def create_db_connection(self, db_name):
        username = os.environ.get('DB_USER')
        password = os.environ.get('DB_PASS')
        try:
            connection = mysql.connector.connect(host="localhost", user=username, passwd=password, database=db_name)            
        except Error as e:
            print(f"Error: '{e}'")
        return connection

    def display_tables(self, db_name):
        print('Connexion établie! ')
        connection = self.create_db_connection(db_name)
        print('TABLES:')
        mycursor = connection.cursor()
        mycursor.execute("SHOW TABLES")
        for x in mycursor:
            print(x)
