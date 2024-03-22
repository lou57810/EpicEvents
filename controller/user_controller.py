import bcrypt
import logging

import sentry_sdk
from .gestion_controller import GestionController
from .commercial_controller import CommercialController
from .support_controller import SupportController
from model.user import User, RoleEnum # , Customer, Base
from model.customer import Customer
from .engine_controller import session   # engine,
from view.start_menu_view import StartMenuView


class UserController:

    current_user = None
    def __init__(self, start_controller):
        self.start_controller = start_controller
        self.gestion_controller = GestionController(self)
        self.commercial_controller = CommercialController(self)
        self.support_controller = SupportController(self)

    ############# Entree et sortie notifiee avec sentry #############
    def report_user_login(self, username):
        with sentry_sdk.push_scope() as scope:
            scope.set_user({"username": username})
            sentry_sdk.capture_message(f"User '{username}' logged in")
    

    def report_user_logout(self, username):
        sentry_sdk.capture_message(f"User '{username}' logged out")
    ##################################################################


    def check_email(self):
        start_app = StartMenuView()
        input_email, input_password = start_app.user_sign_in()
        user_row = session.query(User).filter_by(email=input_email).one_or_none()    # Search corresponding email
        if user_row == None:
            print('Bad email, retry!')
            self.check_email()
        else:
            # print('Email correct!')
            self.check_password(input_password, user_row)


    def check_password(self, input_password, user_row):
        # start_app = StartMenuView()
        # input_email, input_password = start_app.user_sign_in()
        check = input_password.encode('utf-8')
        db_hash = user_row.hashed_pass  # valeur hashed & salted dans la base de données
        db_hash = db_hash.encode('utf-8')

        if bcrypt.checkpw(check, db_hash):
            print('\n')

            # print('You are logged!')
            print('Signed in dbepic as user:', user_row.username, ', email:', user_row.email, '\n')
            # Redirection en fonction du rôle
            # self.department_redirect(user_row.id, user_row.role.value)
            self.current_user = user_row  # A substituer as id
            self.report_user_login(user_row.username)
            self.department_redirect()
        else:
            print('Password incorrect ! retry.')
            self.check_email()

    def sign_in(self):
        if self.check_email() == True:
            self.check_password(input_password, user_row)
            # if self.check_password(input_password, user_row) == True:
                # logging.info("You are logged!")


    """def sign_in(self):
        start_app = StartMenuView()
        input_email, input_password = start_app.user_sign_in()

        user_row = session.query(User).filter_by(email=input_email).one_or_none()    # Search corresponding email
        if user_row == None:
            print('Bad email!')
            self.sign_in()
        else:
            check = input_password.encode('utf-8')
            db_hash = user_row.hashed_pass  # valeur hashed & salted dans la base de données
            db_hash = db_hash.encode('utf-8')

            if bcrypt.checkpw(check, db_hash):
                print('\n')
                print('You are logged!')
                print('Signed in dbepic as user:', user_row.username, ', email:', user_row.email, '\n')

                # Redirection en fonction du rôle
                # self.department_redirect(user_row.id, user_row.role.value)
                self.current_user = user_row  # A substituer as id
                self.department_redirect()
            else:
                print('Pass incorrect ! retry.')
                self.sign_in()"""


    # Redirection en fonction de l'id collaborateur, et du rôle
    def department_redirect(self):
        print('#### DEPARTMENT', self.current_user.role.name, '####\n')
        if self.current_user.role.value == RoleEnum.GESTION.value:
            self.gestion_controller.gestion_menu_controller()
        elif self.current_user.role.value == RoleEnum.COMMERCIAL.value:
            self.commercial_controller.commercial_menu_controller()
        elif self.current_user.role.value == RoleEnum.SUPPORT.value:
            self.support_controller.support_menu_controller()
