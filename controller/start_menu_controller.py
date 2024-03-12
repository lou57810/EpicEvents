from view.start_menu_view import StartMenuView
from .administration_controller import AdministrationController
from .user_controller import UserController
from .engine_controller import EngineController
# from .engine_controller import engine, session

# from dotenv import load_dotenv, dotenv_values

# load_dotenv()
# db_name = os.getenv('DB_NAME')


class StartMenuController:
    def __init__(self):
        self.user_controller = UserController(self)
        self.admin_controller = AdministrationController(self)


    def start_dbepic_app(self):           # Administration, Sign in  run_application
        main_app = StartMenuView()
        main_control = EngineController()
        choice = main_app.start_menu_view()

        if choice == "1":
            self.admin_controller.start_administration()
        if choice == "2":
            # db = main_app.select_database()
            # print('choix database:', db)
            # engine = main_control.start_engine(db)
            # print('engine:', engine)
            main_app.display_tables()
            print('\n')
            # print('Enter Email and then, password: ')
            # email, password = main_app.user_sign_in()
            self.user_controller.sign_in()
        elif choice == "0":
            print("\n Bye!")
            raise SystemExit
