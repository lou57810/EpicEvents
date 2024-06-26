from view.start_menu_view import StartMenuView
from .administration_controller import AdministrationController
from .user_controller import UserController


class StartMenuController:
    def __init__(self):
        self.user_controller = UserController(self)
        self.admin_controller = AdministrationController(self)

    def start_dbepic_app(self):
        main_app = StartMenuView()
        choice = main_app.start_menu_view()

        if choice == "1":
            self.admin_controller.start_administration()
        if choice == "2":
            print('\n')
            self.user_controller.sign_in()
        elif choice == "0":
            print("\n Bye!")
            raise SystemExit
