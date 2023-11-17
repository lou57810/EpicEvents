import os

from controller.main_menu_controller import MainMenuController


BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def main():
    print('BASE_DIR:', BASE_DIR)
    print('Repertoire de base: ', os.getcwd(),'\n')

    app = MainMenuController()
    app.run_db()


    # main cree les controllers : session accessible a tous les controllers.

if __name__ == "__main__":
    main()