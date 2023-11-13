# coding:utf-8
import os

import keyring
import sqlalchemy

from sqlalchemy import create_engine, ForeignKey, text
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, create_database, drop_database
from sqlalchemy import URL
import mysql.connector
from getpass import getpass
from mysql.connector import connect, Error
from model.users_model import Base, Collaborator, Customer



from view.menu_admin_view import MenuAdminDb

# create admin password


class DbController:
    def __init__(self):
        pass
        

    def run(self):
        menuApp = MenuAdminDb()
        self.test()
        # menuApp.menu_create_database()
        choice, name = menuApp.menu_administrator()  # From db_menu
        if choice == 1:
            self.create_db(name)
        elif choice == 2:
            self.delete_db(name)
        elif choice == 3:
            print('table creation.')
            self.create_table()
        elif choice == 4:
            print('table deletion.')
        elif choice == 5:
            print('collaborator_gestion creation.')
        return


    def test(self):
        print('Demarrage du programme. \n')
        print('Version sqlalchemy: ', sqlalchemy.__version__, '\n')
        print('Repertoire de base: ', os.getcwd(),'\n')
        # self.set_hide_password()
        
    
    def create_db(self, db_name):        
        # "<dialect>+<driver>://<username>:<password>@<host>/<database>"
        # example mysql:
        # mysql_db_url = "mysql://<username>:<password>@<hostname>:<port>/<database>"        
        
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
            print('Nouvelle Base de donnees:', db_name)
        else:
            print(db_name, 'Is existing, try another name') 


    def delete_db(self, db_name):
        conn = self.db_connect()
        
        try:
            # Create a cursor object
            if conn.is_connected():
                mycursor = conn.cursor()
                # SQL Statement to delete a database
                mycursor.execute('DROP DATABASE' + ' ' + db_name)
                print(db_name, ' Deleted')

        except Exception as e:
            print("Exeception occured:{}".format(e))
        finally:
            self.display_databases()            
            conn.close() 
        
    def connect_database(self):
        try:
            url_object = URL.create(
                "mysql+pymysql",
                username=input("Enter username: "),
                password=getpass("Enter password:"),  # plain (unescaped) text
                host="localhost",
                database="dbepic",
                )
            engine = create_engine(url_object)

        except Error as e:
            print(e)
        return engine 



    def create_table(self):
        engine = self.db_connect()
        Base.metadata.create_all(bind=engine)
 


    def update_table():
        pass


    def delete_table():
        engine = self.db_connect()
        pass


    def display_databases(self):
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

    def db_engine(self):
        conn = self.db_connect()
        engine = create_engine(conn)


    def set_hide_password(self):
        keyring.get_password("mysql", "root")
        
        

    
        