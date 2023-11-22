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
from model.users_model import Base, Collaborator, Customer



class AdminController:

    def __init__(self, username, password):
        self.username = username
        self.password = password


    def run_db(self):
        self.test()
        dbApp = AdminMenuView()
        choice, db_name = dbApp.admin_menu_db()  # From admin_menu_view

        if choice == 1:
            print('db_name:', db_name)
            self.create_db_connection(db_name, self.username, self.password)
        elif choice == 2:
            self.delete_db(db_name)
        # elif choice == 3:
            # print('choice:', choice)
            # self.build_table()
        elif choice == 3:
            print("\n Bye!")
            raise SystemExit
        return


    def test(self):
        print('Version sqlalchemy: ', sqlalchemy.__version__, '\n')
        print('Repertoire de base: ', os.getcwd(),'\n')
        self.display_databases()


    def create_db_connection(self, db_name, username, password):
        engine = create_engine("mysql+pymysql://" + username + ":" + password + "@localhost/" + db_name)
        
        if not database_exists(engine.url):
            create_database(engine.url)
            print('Nouvelle Base de donnees:', db_name)
            self.display_databases()
            Base.metadata.create_all(bind=engine)

        else:
            with engine.connect() as connection:
                result = connection.execute(text('select "Hello"'))
                print('result:', result.all())
                print('You are connected with: ', db_name)
                self.display_tables(engine)
        self.run_db()



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
        self.run_db()
        

    
    def db_connect(self):
        print('Enter db_connect !')
        conn = mysql.connector.connect(
            username = self.username,
            password = self.password,
            host="localhost",
            # auth_plugin="mysql_native_password"
            )
        return conn


    def display_databases(self):
        print('Enter display_databases')
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


    def display_tables(self, engine):        
        inspector = inspect(engine)

        for table_name in inspector.get_table_names():
            print('\n')
            print('tables:', table_name)
            for column in inspector.get_columns(table_name):
               print("Column: %s" % column['name'])
