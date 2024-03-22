from view.start_menu_view import StartMenuView
from .administration_controller import AdministrationController
from .user_controller import UserController
from .engine_controller import EngineController


class StartMenuController:
    def __init__(self):
        self.user_controller = UserController(self)
        self.admin_controller = AdministrationController(self)


    def start_dbepic_app(self):           # Administration, Sign in  run_application
        main_app = StartMenuView()
        # main_control = EngineController()
        choice = main_app.start_menu_view()

        if choice == "1":
            self.admin_controller.start_administration()
        if choice == "2":
            main_app.display_tables()
            print('\n')
            self.user_controller.sign_in()
        elif choice == "0":
            print("\n Bye!")
            raise SystemExit
