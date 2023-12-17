from view.support_menu_view import SupportMenuView


class SupportController:

    def __init__(self):
        pass


    def support_menu_controller(self):
        menu_app = SupportMenuView()
        choice, values = menu_app.support_menu_view()
        


        if choice == 1:
            self.create_event()
        elif choice == 2:
            print('2')
        elif choice == 3:
            print("\n Bye!")
            raise SystemExit


    def create_event():
        pass