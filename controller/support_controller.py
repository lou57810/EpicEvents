from view.support_menu_view import SupportMenuView
from model.users_model import Event # User, 
from .engine_controller import session # engine, 


class SupportController:

    def __init__(self, user_controller):
        self.user_controller = user_controller
        self.support_views = SupportMenuView()


    def support_menu_controller(self, id, role):
        choice, values = self.support_views.support_menu_view(id, role)

        if choice == 1:
            print('Departement Support')
            self.support_views.display_filtered_events(id, role)
        elif choice == 2:
            print('Departement Support')
            self.update_own_events(values, id, role)
        elif choice == 3:
            
            self.user_controller.start_controller.run_db(self)


    def update_own_events(self, values, id, role):
        if values:
            event_id, attribut_to_update, new_attribut_value = values
            print('values:', values)
            event = session.query(Event).filter_by(id=event_id).one_or_none()

            print('event_to_update:', event)
        
            query = session.query(Event)
            column_names = query.statement.columns.keys()

            # Test sur l'appartenance du contrat evenementiel
            for elt in column_names:
                if elt == attribut_to_update:
                    if attribut_to_update == 'event_name':
                        event.event_name = new_attribut_value
                    # elif attribut_to_update == 'event_id':
                        # event.event_id = new_attribut_value
                    # elif attribut_to_update == 'contract_id':
                        # event.contract_id = new_attribut_value
                    # elif attribut_to_update == 'customer_name':
                        # event.customer_name = new_attribut_value
                    # elif attribut_to_update == 'customer_contact':
                        # event.customer_contact = new_attribut_value
                    elif attribut_to_update == 'start_date':
                        event.start_date = new_attribut_value
                    elif attribut_to_update == 'end_date':
                        event.end_date = new_attribut_value
                    # elif attribut_to_update == 'support_contact':
                        # event.support_contact = new_attribut_value
                    elif attribut_to_update == 'location':
                        event.location = new_attribut_value
                    elif attribut_to_update == 'attendees':
                        event.attendees = new_attribut_value
                    elif attribut_to_update == 'notes':
                        event.notes = new_attribut_value
            session.commit()

            print('Event updated: ', event)
        else:
            print('No values')
        # Retour au menu
        self.support_menu_controller(id, role)
