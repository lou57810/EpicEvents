import os
import mysql.connector

from getpass import getpass
from mysql.connector import connect, Error
import sqlalchemy
from sqlalchemy import URL
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database, drop_database

from view.menu_admin_view import MenuAdminDb


class AdminController:
    def __init__(self):
        pass
        

    def run(self):
        menuApp = MenuAdminDb()
        self.test()
        
        choice, name = menuApp.menu_administrator()  # From db_menu
        if choice == 1:
            self.create_db(name)
        elif choice == 2:
            self.delete_db(name)
        
        return


    def test(self):
        # print('Database: to do !')
        print('Demarrage session administrateur.')
        print('Version sqlalchemy: ', sqlalchemy.__version__, '\n')
        print('Repertoire de base: ', os.getcwd(),'\n')
        self.display_databases()
        

    def create_db(self, db_name):        
        # "<dialect>+<driver>://<username>:<password>@<host>/<database>"
        # example mysql:
        # mysql_db_url = "mysql://<username>:<password>@<hostname>:<port>/<database>"        
        self.display_databases()
        url_object = URL.create(
                    "mysql+pymysql",
                    username=input("Enter username: "),
                    password=getpass("Enter password: "),
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


    def db_connect(self):
        conn = mysql.connector.connect(
            username = "lou", password = "edwood",
            host="localhost",
            auth_plugin="mysql_native_password")
        return conn


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