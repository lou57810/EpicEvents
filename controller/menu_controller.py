from view.menu_view import Menu
from .db_controller import DbController
from view.db_menu import DbMenu
import mysql.connector
# import mariadb


class MenuController:
    def __init__(self, menu: Menu):
        self.menu = menu


    def run(self):
        menu_db = DbMenu()
        menu = Menu()

        # menu.menu_sign_in()
        self.verify_sign_in()
        # menu.user_connect()
        db_app = DbController()
        db_app.run()
        menu.menu_gestion_admin()
        
    def verify_sign_in(self):
        menu = Menu()
        user_name, password = menu.menu_sign_in()
        
        conn = None
        try:
            conn = mysql.connector.connect(
            user = user_name, passwd = password,
            host="localhost",
            auth_plugin="mysql_native_password"
        )
            if conn.is_connected():
                print('Connected to MySQL database')

                mycursor = conn.cursor()
                mycursor.execute("SHOW DATABASES")
                for db in mycursor:
                    print('Databases:', db)

        except ValueError as e:
            print(e)

        finally:
            if conn is not None and conn.is_connected():
                conn.close()
                print('Connection closed.')

