import bcrypt
from view.main_menu_view import MainMenuView
from .gestion_controller import GestionController
from .commercial_controller import CommercialController



class MainController:
    def __init__(self):
        pass


    def main_menu_controller(self, id, role):           # Administration, Sign in
        
        menu_app = MainMenuView()
        choice, values = menu_app.main_menu_view(id, role)
        
        gestion_app = GestionController()
        customer_app = CommercialController()
        
        # Gestion
        if choice == 1:
            gestion_app.create_user(id, role, values)
        elif choice == 2:
            gestion_app.update_user(id, role, values)
        elif choice == 3:
            gestion_app.delete_user(id, role, values)
        elif choice == 4:
            gestion_app.create_contract(id, role, values)
        elif choice == 5:
            gestion_app.update_contract(id, role, values)
        elif choice == 6:
            pass    # display_filtered_events() --> view.main_menu_view()
        elif choice == 7:
            gestion_app.update_events(values)
        # Commercial
        elif choice == 8:
            customer_app.create_customer_account(id, role, values)
        elif choice == 9:
            # menu_app = GestionMenuView()
            # menu_app.display_customers()
            # print('\n')
            # self.gestion_menu_controller()     # Retour menu
            pass
        elif choice == 10:
            # menu_app = GestionMenuView()
            # menu_app.display_contracts()
            # print('\n')
            # self.gestion_menu_controller()     # Retour menu
            pass
        elif choice == 11:
            # menu_app = GestionMenuView()
            # menu_app.display_events()
            # print('\n')
            # self.gestion_menu_controller()     # Retour menu
            pass
        elif choice == 12:
            customer_app.create_event(self, values, contact_id)
        elif choice == 13:
            pass
        elif choice == 14:
            pass
        elif choice == 15:
            pass
        elif choice == 16:
            pass
        elif choice == 17:
            pass
        elif choice == 18:
            pass
        elif choice == 19:
            print("\n Bye!")
            raise SystemExit


    def create_user(self, values):
        # ident, username, password, email, role = values
        username, password, email, role = values

        # Création User = Input mot de passe: password =>bd
        bytes = password.encode('utf-8')
        hashed_password = bcrypt.hashpw(bytes, bcrypt.gensalt())

        user = User(username, password, hashed_password, email, role)
        session.add(user)   # stage
        session.commit()    # push
        
        users = session.query(User).all()
        for user in users:
            print(f"id: {user.id}, username: {user.username},\
                    password: {user.password}, email: {user.email},\
                    role: {user.role.value}")
        self.gestion_menu_controller()     # Retour menu gestion


    def update_user(self, values):
        id, key_to_update, value_to_update = values

        user = session.query(User).filter_by(id=id).one_or_none()
        print('user_values_to_update:', user)

        query = session.query(User)
        column_names = query.statement.columns.keys()
        
        for elt in column_names:
            if elt == key_to_update:
                if key_to_update == 'id':
                    user.id = value_to_update
                elif key_to_update == 'username':
                    user.username = value_to_update
                elif key_to_update == 'password':
                    bytes = value_to_update.encode('utf-8')
                    salt = bcrypt.gensalt()        
                    hashed_password = bcrypt.hashpw(bytes, salt)
                    # print('hashed_password:', bcrypt.hashpw(bytes, salt))
                    user.password = value_to_update
                    user.hashed_pass = hashed_password
                elif key_to_update == 'email':
                    user.email = value_to_update
                elif key_to_update == 'role':
                    user.role = value_to_update
        
        session.commit()
        print('user_updated:', user)

        self.gestion_menu_controller()


    def delete_user(self, values):
        id = values

        user = session.query(User).filter_by(id=id).one_or_none()

        session.delete(user)
        session.commit()

        # menu_app = GestionMenuView()
        # menu_app.display_gestion_table()

        self.gestion_menu_controller()


    def create_contract(self, values):
        id, customer_info, total_amount, balance_payable, start_date, contract_status = values
        id_commercial = session.query(Customer).where(Customer.id == customer_info).all()
        print('id_commercial:', id_commercial[0].contact)
        commercial_contact = id_commercial[0].contact
        contract = Contract(id, customer_info, commercial_contact, total_amount, balance_payable, start_date, contract_status)
        
        session.add(contract)   # stage
        session.commit()    # push

        with engine.connect() as conn:
            result = conn.execute(text("select * from contracts"))
            for rows in result:
                print("Contracts:", rows)
        self.gestion_menu_controller()     # Retour menu gestion


    def update_contract(self, values):
        contract_id, attribut_to_update, new_attribut_value = values

        contract = session.query(Contract).filter_by(id=contract_id).one_or_none()
        print('contract_to_update:', contract)
        # print('contrac.attribut:', contract.attribut_to_update) # ==>  'Contract' object has no attribute 'attribut_to_update'
        print('attribut: ', attribut_to_update)
        query = session.query(Contract)
        column_names = query.statement.columns.keys()
        print('Choose one key :', column_names)
        for elt in column_names:

            if elt == attribut_to_update:
                if attribut_to_update == 'contract_id':
                    contract.id = new_attribut_value
                elif attribut_to_update == 'customer_info':
                    contract.customer_info = new_attribut_value
                elif attribut_to_update == 'commercial_contact':
                    contract.commercial_contact = new_attribut_value
                elif attribut_to_update == 'total_amount':
                    contract.total_amount = new_attribut_value
                elif attribut_to_update == 'balance_payable':
                    contract.balance_payable = new_attribut_value
                elif attribut_to_update == 'start_date':
                    contract.start_date = new_attribut_value
                elif attribut_to_update == 'contract_status':
                    contract.contract_status = new_attribut_value

        print('new session:', session.commit())
        session.commit()
        print('contract updated:', contract)
        self.gestion_menu_controller()      # Retour au menu



    def update_events(self, values):
        id, key_to_update, new_attribut_value = values

        event = session.query(Event).filter_by(id=id).one_or_none()
        print('event_to_update:', event)

        print('attribut: ', key_to_update)
        query = session.query(Event)
        column_names = query.statement.columns.keys()
        print('col:', column_names)
        for elt in column_names:
            if elt == key_to_update:
                if key_to_update == 'id':
                    event.event_id = new_attribut_value
                elif key_to_update == 'event_name':
                    event.event_name = new_attribut_value
                elif key_to_update == 'contract_id':
                    event.contract_id = new_attribut_value
                elif key_to_update == 'customer_name':
                    event.customer_name = new_attribut_value
                elif key_to_update == 'customer_contact':
                    event.customer_contact = new_attribut_value
                elif key_to_update == 'start_date':
                    event.start_date = new_attribut_value
                elif key_to_update == 'end_date':
                    event.end_date = new_attribut_value
                elif key_to_update == 'support_contact':
                    event.support_contact = new_attribut_value
                elif key_to_update == 'location':
                    event.location = new_attribut_value
                elif key_to_update == 'attendees':
                    event.attendees = new_attribut_value
                elif key_to_update == 'notes':
                    event.notes = new_attribut_value

        print('new session:', session.commit())
        session.commit()

        menu_app = GestionMenuView()        # Affichage update
        menu_app.display_events()
        
        self.gestion_menu_controller()      # Retour au menu
    