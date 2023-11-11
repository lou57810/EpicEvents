# from controller.menu_controller import MenuController
# from controller.db_controller import DbController
from controller.main_menu_controller import MenuController
# from view.main_menu_view import MainMenu
# import sqlalchemy
# from sqlalchemy import create_engine ###


def main():
    
    # app = MenuAdmin()
     
    app = MenuController()
    
    app.run()

    
    """db_connection = sqlalchemy.create_engine(
        'mysql+mysqlconnector://user:pwd@hostname/db_name',
        connect_args={'auth_plugin': 'mysql_native_password'})"""
    

    # main cree les controllers : session accessible a tous les controllers.

if __name__ == "__main__":
    main()

