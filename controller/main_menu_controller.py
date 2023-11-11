from view.main_menu_view import MainMenu
from view.menu_view import Menu
from .admin_controller import AdminController
# from view.db_menu import DbMenu
import mysql.connector
# import mariadb


class MenuController:
    # def __init__(self, menu: Menu):
        # self.menu = menu
    pass


    def run(self):
        # menu_db = DbMenu()
        # menu = Menu()
        db_app = AdminController()
        # admin_app = MenuAdmin()
        app = MainMenu()

        

        choice = app.main_menu()

        if choice == "1":
            print('administrateur')
            # self.verify_sign_in()
            db_app.run()
            
        elif choice == "2":
            print('EventEpic user')
            # self.verify_sign_in()
            app.connect_database()
            menu.menu_gestion_admin()
        elif choice == "3":
            print("\n Bye!")
            raise SystemExit

        # menu.menu_sign_in()
        # self.verify_sign_in()
        # menu.user_connect()
        
        
        
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

