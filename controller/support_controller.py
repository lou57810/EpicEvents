from view.support_menu_view import SupportMenuView


class SupportController:

    def __init__(self):
        pass


    def support_menu_controller(self):
        menu_app = SupportMenuView()
        choice, values = menu_app.support_menu_view()
        


        if choice == 1:
            self.display_filtered_event()
        elif choice == 2:
            self.update_own_events()
        elif choice == 3:
            print("\n Bye!")
            raise SystemExit


    def display_filtered_event():
        pass


    def update_own_events():
        pass