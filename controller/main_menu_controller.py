import os
from view.main_menu_view import MainMenuView
from view.user_menu_view import UserMenuView
from .admin_controller import AdminController
from .user_controller import UserController
import sqlalchemy
from sqlalchemy import URL
from sqlalchemy import create_engine
import mysql.connector




class MainMenuController:
    def __init__(self):
        pass


    def run_db(self):
        username = os.environ.get('DB_USER')
        password = os.environ.get('DB_PASS')
        # self.display_databases()
        main_app = MainMenuView()
        choice = main_app.main_menu_view()

        if choice == "1":
            # admin_app = AdminController('mysql', username, password)
            admin_app = AdminController('mysql')
            admin_app.start_db('mysql')

        if choice == "2":
            print('\n')
            db_name = main_app.choose_db_and_connect()
            user_app = UserController()
            user_app.run_table(db_name)

        elif choice == "3":
            print("\n Bye!")
            raise SystemExit


    """def connect_mysql(self):
        username = os.environ.get('DB_USER')
        password = os.environ.get('DB_PASS')
        mydb = mysql.connector.connect(host="localhost", user=username, password=password)
        return mydb

    def display_databases(self):
        print('Version sqlalchemy: ', sqlalchemy.__version__, '\n')
        mydb = self.connect_mysql()
        mycursor = mydb.cursor()
        mycursor.execute("SHOW DATABASES")
        print('DATABASES:')
        for x in mycursor:
            print(x)
    """
