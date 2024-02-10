from model.users_model import Event
from controller.engine_controller import session
from model.users_model import Permissions_roles, UPDATE_OWN_EVENT


class SupportMenuView:

    def __init__(self):
        pass

    def get_permission(self, role, role_fct):
        for elt in Permissions_roles:
            if elt == role:
                result = Permissions_roles[role]
        for elt in result:
            if elt == role_fct:
                print('elt')
                return True

    def support_menu_view(self, id, role):
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
                self.display_filtered_events(id, role)
            elif answer == "2":
                value = self.update_own_events(id, role)
                return 2, value
            elif answer == "3":
                # return 3, None
                print("\n Bye!")
                raise SystemExit


    def display_filtered_events(self, id, role):
        # event = session.query(Events).filter_by(support_contact=email).one_or_none()
        print('id', id)
        event = session.query(Event).filter(Event.support_contact == role).all()
        for elt in event:
            print('Your Events :', elt)
        # Retour au menu
        self.support_menu_view(id, role)


    def update_own_events(self, id, role):
        if self.get_permission(role, UPDATE_OWN_EVENT):
            event_to_update = input("N° de l\'evenement :")
            attribut_to_update = input("Attribut à modifier :")
            new_attribut_value = input("Nouvelle valeur :")
            return event_to_update, attribut_to_update, new_attribut_value
        else:
            self.support_menu_view(id, role)
            