from controller.menu_controller import MenuController
# from controller.db_controller import DbController
from view.menu_view import Menu


def main():
    # db_control = DbController()    
    menu = Menu()
    app = MenuController(menu)
    app.run()
    print('Ouverture de la database !')

    # main cree les controllers : session accessible a tous les controllers.

if __name__ == "__main__":
    main()

