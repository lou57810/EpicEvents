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
                # self.display_filtered_events(id, role)
                return 1, None
            elif answer == "2":
                value = self.update_owner_events(id, role)
                return 2, value
            elif answer == "3":
                return 3, None
                # print("\n Bye!")
                # raise SystemExit


    def display_filtered_events(self, id, role):
        print('id', id)
        i = 0
        event = session.query(Event).filter(Event.support_contact == id).all()
        print('Your own events:\n')
        for elt in event:
            print(i,'.', elt)
            i = i + 1
        # Retour au menu
        self.support_menu_view(id, role)


    def display_own_events(self, id, role):
        # events = session.query(Event).all()
        events = session.query(Event).filter(Event.support_contact == id).all()
        i = 0
        print('Your events:\n')
        for elt in events:
            print('N°', i,'.', elt)
            i = i + 1

        choix = input("Choisir un N° event:")
        event = events[int(choix)]
        return event
        # Retour au menu
        # self.support_menu_view(id, role)


    def update_owner_events(self, id, role):
        event_to_update = self.display_own_events(id, role)
        
        if self.get_permission(role, UPDATE_OWN_EVENT):
            query = session.query(Event)
            column_names = query.statement.columns.keys()
            print('Choose one key :', column_names[1], column_names[5], column_names[6], column_names[7], column_names[8], column_names[9], column_names[10])
            #  = input("N° de l\'evenement :")
            attribut_to_update = input("Attribut à modifier :")
            new_attribut_value = input("Nouvelle valeur :")
            return event_to_update.id, attribut_to_update, new_attribut_value
            
        else:
            print('You are not allowed to update events!')
        self.support_menu_view(id, role)
