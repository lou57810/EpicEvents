from view.menu_view import Menu
from .db_controller import DbController
# import mariadb


class MenuController:
    def __init__(self, menu: Menu):
        self.menu = menu


    def run(self):
        
        menu = Menu()
        menu.admin_register()
        
        
        """try:
            conn = mariadb.connect(
                user="root",
                password="edwood111",
                host="127.0.0.1",
                port=3306,
                )

            # cur = conn.cursor()

        except mariadb.Error as e:
            print(f"Error : {e}")

        
        menu.admin_register()


        # /c/Program Files/MariaDB 11.3/bin
        """

