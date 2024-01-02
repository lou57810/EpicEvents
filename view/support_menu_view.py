


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
                return 1, None
            elif answer == "2":
                value = self.update_own_events()
                return 2, value
            elif answer == "3":
                return 3, None


    def update_own_events(self):
        event_to_update = input("N° de l\'evenement :")
        attribut_to_update = input("Attribut à modifier :")
        new_attribut_value = input("Nouvelle valeur :")
        return event_to_update, attribut_to_update, new_attribut_value