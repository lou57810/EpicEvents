from view.support_menu_view import SupportMenuView
from model.users_model import Event
from .engine_controller import session


class SupportController:

    def __init__(self, user_controller):
        self.user_controller = user_controller
        self.support_views = SupportMenuView()


    def support_menu_controller(self):
        choice = self.support_views.support_menu_view()
        role = self.user_controller.current_user.role.value
        current_user = self.user_controller.current_user.id

        if choice == "1":
            print('Departement Support')
            self.support_views.display_filtered_events(role, current_user)
            print('\n')
            self.support_menu_controller()
        elif choice == "2":
            print('Departement Support')
            self.update_own_events(role, current_user)
        elif choice == "3":
            self.user_controller.start_controller.start_dbepic_app()


    def update_own_events(self, role, current_user):
        event_id, key_to_update, value_to_update = self.support_views.update_own_events(role, current_user)
        event = session.query(Event).filter_by(id=event_id).one_or_none()

        query = session.query(Event)
        column_names = query.statement.columns.keys()
        for elt in column_names:
            if elt == key_to_update:
                if key_to_update == 'event_name':
                    event.event_name = value_to_update
                elif key_to_update == 'start_date':
                    event.start_date = value_to_update
                elif key_to_update == 'end_date':
                    event.end_date = value_to_update
                elif key_to_update == 'location':
                    event.location = value_to_update
                elif key_to_update == 'attendees':
                    event.attendees = value_to_update
                elif key_to_update == 'notes':
                    event.notes = value_to_update
        session.commit()
        print('\n')
        print('Event updated: ', event.event_name, key_to_update, ':', value_to_update)

        # Retour au menu
        self.support_menu_controller()
