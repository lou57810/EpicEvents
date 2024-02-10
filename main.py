import os

from controller.start_menu_controller import StartMenuController



BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def main():
    print('BASE_DIR:', BASE_DIR)
    print('Repertoire de base: ', os.getcwd(),'\n')

    main_app = StartMenuController()
    main_app.run_db()



if __name__ == "__main__":
    main()