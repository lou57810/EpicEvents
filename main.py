import os
from dotenv import load_dotenv, dotenv_values
from controller.start_menu_controller import StartMenuController

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


load_dotenv()
# print('env:', os.getenv("DB_PASS"), os.getenv("DB_USER"))

def main():
    # print('BASE_DIR:', BASE_DIR)
    print('Repertoire de base: ', os.getcwd(),'\n')

    main_app = StartMenuController()
    main_app.start_dbepic_app()


if __name__ == "__main__":
    main()