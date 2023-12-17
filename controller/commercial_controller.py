from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy import text, update
from view.commercial_menu_view import CommercialMenuView
from .engine_controller import EngineController
from .engine_controller import engine
from model.users_model import Customer


	
class CommercialController:
    def __init__(self):
        pass


    def commercial_menu_controller(self):
        menu_app = CommercialMenuView()
        choice, value = menu_app.commercial_menu_view()

        
        if choice == 1:
            self.create_or_update_customer(value)
            
        elif choice == 2:
            self.create_or_update_customer(value)
        """
        elif choice == 3:
            # self.delete_collaborator(value)
            pass
        elif choice == 4:
            print("\n Bye!")
            raise SystemExit
        """

    def create_or_update_customer(self, value):
        print('values:', value)
        ident, full_name, email, tel, company_name, first_date, last_date, contact = value

        Session = sessionmaker(bind=engine)
        session = Session()
        customer = session.query(Customer).filter_by(ident=ident).one_or_none()
        # customer = Customer(ident, full_name, email, tel, company_name, first_date, last_date, contact)
        customer.full_name = full_name
        customer.email = email
        customer.tel = tel
        customer.company_name = company_name
        customer.first_date = first_date
        customer.last_date = last_date
        customer.contact = contact
        
        # session.add(customer)   # stage
        session.commit()    # push

        with engine.connect() as conn:
            result = conn.execute(text("select * from customers"))
            for rows in result:
                print("Customers:", rows)
        self.commercial_menu_controller()     # Retour menu
	
	