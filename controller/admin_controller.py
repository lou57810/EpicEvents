import os
import mysql.connector

from getpass import getpass
import keyring
from mysql.connector import connect, Error
import sqlalchemy
from sqlalchemy import URL
from sqlalchemy import create_engine, ForeignKey, text
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, create_database, drop_database

from view.admin_menu_view import MenuAdminDb
from model.users_model import Base, Collaborator, Customer


class AdminController:

    def __init__(self, username, password):
        self.username = username
        self.password = password


    def run(self):
        self.test()
        menuApp = MenuAdminDb()
        choice, db_name = menuApp.menu_administrator()  # From admin_menu_view        

        if choice == 1:
            print('db_name:', db_name)
            self.create_db(db_name, self.username, self.password)
        elif choice == 2:
            self.delete_db(db_name)
        elif choice == 3:
            self.create_table()
        
        return


    def test(self):        
        print('Version sqlalchemy: ', sqlalchemy.__version__, '\n')
        print('Repertoire de base: ', os.getcwd(),'\n')
        self.display_databases()
        

    def create_db(self, db_name, username, password):
        # "<dialect>+<driver>://<username>:<password>@<host>/<database>"
        # example mysql:
        # mysql_db_url = "mysql://<username>:<password>@<hostname>:<port>/<database>"
        
        url_object = URL.create(
                    "mysql+pymysql",
                    username = username,
                    password = password,
                    host="localhost",
                    database=db_name,
                )
        engine = create_engine(url_object)
        
        if not database_exists(engine.url):
            create_database(engine.url)
            print('Nouvelle Base de donnees:', db_name)
            self.display_databases()
        else:
            print(db_name, 'Is existing, try another name')
        self.run()
 


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
            print("Exception occured:{}".format(e))
        finally:
            self.display_databases()
            conn.close()
        self.run()

    
    def db_connect(self):
        conn = mysql.connector.connect(            
            username = self.username,
            password = self.password,
            host="localhost",
            # auth_plugin="mysql_native_password"
            )
        return conn


    def create_table(self):
        engine = self.db_connect()
        Base.metadata.create_all(bind=engine)
    

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
            print("Exception occured:{}".format(e))
        finally:
            conn.close()