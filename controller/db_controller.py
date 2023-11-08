import os

import keyring
import sqlalchemy

from sqlalchemy import create_engine, ForeignKey, text
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, create_database, drop_database
from model.users_model import Collaborator
from sqlalchemy import URL
import mysql.connector


from view.db_menu import DbMenu

# create admin password


class DbController:
    def __init__(self):
        pass
        

    def run(self):
        menuApp = DbMenu()
        self.test()
        # menuApp.menu_create_database()
        choice, db_name = menuApp.menu_administrator()  # From db_menu
        if choice == 1:
            self.create_db(db_name)
        elif choice == 2:
            self.delete_db(db_name)
        return


    def test(self):
        print('Demarrage du programme. \n')
        print('Version sqlalchemy: ', sqlalchemy.__version__, '\n')
        print('Repertoire de base: ', os.getcwd(),'\n')
        # self.set_hide_password()
        
    
    def create_db(self, db_name):
        print('create_db begin !')
        # "<dialect>+<driver>://<username>:<password>@<host>/<database>"
        # example mysql:
        # mysql_db_url = "mysql://<username>:<password>@<hostname>:<port>/<database>"
        
        print('db: ', db_name)
        url_object = URL.create(
                    "mysql+pymysql",
                    username="lou",
                    password="edwood",  # plain (unescaped) text
                    host="localhost",
                    database=db_name,
                )
        engine = create_engine(url_object)
        
        if not database_exists(engine.url):
            create_database(engine.url)
            print('Nouvelle Base de donnees:', engine.url)
        else:
            print('DataBase name :', engine.url) 


    def delete_db(self, db_name):
        print('db: ', db_name)
        # menuApp = DbMenu()
        # choice, db_name = menuApp.menu_administrator()
        conn = self.db_connect()
        
        """conn = mysql.connector.connect(
            username = "lou", password = "edwood",
            host="localhost",
            auth_plugin="mysql_native_password")"""
        
        try:
            # Create a cursor object
            if conn.is_connected():
                print('Connected to MySQL database')
                self.display_databases()
                mycursor = conn.cursor()
                """mycursor.execute("SHOW DATABASES")
                rows = mycursor.fetchall()
                for row in rows:
                    print(row)"""
                print('db_name:', db_name)
                # SQL Statement to delete a database
                mycursor.execute('DROP DATABASE' + ' ' + db_name)

        except Exception as e:
            print("Exeception occured:{}".format(e))
        finally:
            conn.close() 
        
    def create_tables():
        pass


    def update_tables():
        pass


    def delete_tables():
        pass


    def display_databases(self):
        """conn = mysql.connector.connect(
            username = "lou", password = "edwood",
            host="localhost",
            auth_plugin="mysql_native_password")
        """
        conn = self.db_connect()

        try:
            # Create a cursor object
            if conn.is_connected():
                print('Connected to MySQL database')
                mycursor = conn.cursor()
                mycursor.execute("SHOW DATABASES")
                rows = mycursor.fetchall()
                for row in rows:
                    print(row)

        except Exception as e:
            print("Exeception occured:{}".format(e))
        finally:
            conn.close()


    def db_connect(self):
        conn = mysql.connector.connect(
            username = "lou", password = "edwood",
            host="localhost",
            auth_plugin="mysql_native_password")
        return conn


    def set_hide_password(self):
        keyring.get_password("mysql", "root")
        
        