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
            return answer


    def display_filtered_events(self, role, current_user):
        print('current_user:', current_user)
        i = 0
        event = session.query(Event).filter(Event.support_contact == current_user).all()
        print('event:', event)
        print('support_contact, current_user:', Event.support_contact, current_user)
        print('Your own events:\n')
        for elt in event:
            print(i,'.', elt)
            i = i + 1


    def display_own_events(self, role, current_user):
        print('own_events:')
        # events = session.query(Event).all()
        events = session.query(Event).filter(Event.support_contact == current_user).all()
        i = 0
        print('Your events:\n')
        for elt in events:
            print('N°', i,'.', 'Event_id:',elt.id,\
                 "\n", 'Event', 
                  )
            i = i + 1

        choix = input("Choisir un N° event:")
        event = events[int(choix)]
        return event
        # Retour au menu
        # self.support_menu_view(id, role)


    def update_own_events(self, role, current_user):
        # event_to_update = self.display_own_events(role, current_user)
        event = session.query(Event).filter_by(id=event_to_update.id).one_or_none()
        
        if self.get_permission(role, UPDATE_OWN_EVENT):
            query = session.query(Event)
            column_names = query.statement.columns.keys()
            print('Choose one key :', column_names[1], column_names[5], column_names[6], column_names[7], column_names[8], column_names[9], column_names[10])
            #  = input("N° de l\'evenement :")
            attribut_to_update = input("Attribut à modifier :")
            new_attribut_value = input("Nouvelle valeur :")
            print('att, new_att, event_id', event_to_update.id, attribut_to_update, new_attribut_value)
            return event_to_update.id, attribut_to_update, new_attribut_value
            
        else:
            print('You are not allowed to update events!')
        self.support_menu_view(id, role)
