


class SupportMenuView:

    def __init__(self):
        pass



    def support_menu_view(self):
        print("Choose options")
        answer = True
        while answer:
            print("""
            1. Display own events.
            2. Update own events.
            3. Quit.
            """)

            answer = input("Faites votre choix ! \n")
            if answer == "1":
                value = self.display_own_events()
                return 1, value
            elif answer == "2":
                value = self.update_own_events()
                return 2, value
            elif answer == "3":
                return 3, None


    def display_own_events():
        pass
        


    def update_own_events():
        pass