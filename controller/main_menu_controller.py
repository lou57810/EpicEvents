from view.main_menu_view import MainMenu
from view.user_menu_view import UserMenu
from .admin_controller import AdminController
from .user_controller import UserController
# from sqlalchemy_utils import database_exists
from sqlalchemy import URL
from sqlalchemy import create_engine
import mysql.connector



class MainMenuController:
    def __init__(self):
        pass


    def run(self):
        main_app = MainMenu()
        choice = main_app.main_menu()


        if choice == "1":            
            username, password = main_app.menu_sign_in()
            admin_app = AdminController(username, password)
            admin_app.run()
            
        elif choice == "2":            
            username, password = main_app.menu_sign_in()
            user_app = UserController(username, password)
            user_app.run()
            

        elif choice == "3":
            print("\n Bye!")
            raise SystemExit
        