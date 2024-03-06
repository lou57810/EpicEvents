from model.users_model import Event
from controller.engine_controller import session
from model.users_model import User, Customer, Permissions_roles, UPDATE_OWN_EVENT


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
        user = session.get(User, current_user)
        events = session.query(Event).filter(Event.support_contact == current_user).all()
        print('Current_user:', user.username)
        if events:
            i = 0
            z = len(events)
 
            while i < z:
                print('\n')
                print('N°:', i,
                '\n', 'Event name:', events[i].event_name,
                '\n', 'Contract id:', events[i].contract_id,
                '\n', 'Customer name:', events[i].customer_name,
                '\n', 'Customer contact:', events[i].customer_contact,
                '\n', 'Start date:', events[i].start_date,
                '\n', 'End date:', events[i].end_date,
                '\n', 'Location:', events[i].location,
                '\n', 'Support contact:', events[i].support_contact,
                '\n', 'Attendees:', events[i].attendees,
                '\n', 'Notes:', events[i].notes,
                )
                i = i + 1
            return events
        else:
            print('Any Events to display!')


    def display_filtered_events_to_update(self, role, current_user):
        events = self.display_filtered_events(role, current_user)
        print('\n')

        choix = input("Choisir un N° event:")
        event = events[int(choix)]
        return event

    def update_own_events(self, role, current_user):
        event_filtered = self.display_filtered_events_to_update(role, current_user)
        customer = session.get(Customer, event_filtered.customer_contact)

        query = session.query(Event)
        column_names = query.statement.columns.keys()

        print('Choose one key :',
        '\n', '1:', column_names[1],
        '\n', '2:', column_names[5],
        '\n', '3:', column_names[6],
        '\n', '4:', column_names[7],
        '\n', '5:', column_names[9],
        '\n', '6:', column_names[10],
        '\n')

        if self.get_permission(role, UPDATE_OWN_EVENT):
            key_to_update = input('N° Clé à modifier: ')
            if key_to_update == "1":
                key_to_update = column_names[1]
                value_to_update = input('Nouvelle valeur: ')
            elif key_to_update == "2":
                key_to_update = column_names[5]
                value_to_update = input('Nouvelle valeur: ')
            elif key_to_update == "3":
                key_to_update = column_names[6]
                value_to_update = input('Nouvelle valeur: ')
            elif key_to_update == "4":
                key_to_update = column_names[7]
                value_to_update = input('Nouvelle valeur: ')
            elif key_to_update == "5":
                key_to_update = column_names[9]
                value_to_update = input('Nouvelle valeur: ')
            elif key_to_update == "6":
                key_to_update = column_names[10]
                value_to_update = input('Nouvelle valeur: ')
            print('test:', event_filtered.id, key_to_update, value_to_update)
            return event_filtered.id, key_to_update, value_to_update


        else:
            print('You are not allowed to update events!')
        self.support_menu_view(id, role)
