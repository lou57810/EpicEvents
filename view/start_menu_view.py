# import os
from controller.engine_controller import engine
from sqlalchemy import inspect


class StartMenuView:
    def __init__(self):
        pass

    def start_menu_view(self):
            print("Choose options:")
            answer = True
            while answer:
                print("""
                1. Administration.
                2. Sign in.
                3. Quit.
                """)
                answer = input("Choix:")
                return answer

    def user_sign_in(self):
        email = input('Email: ')
        password = str(input('Password: '))
        
        return email, password


    def display_tables(self):
        # print('Connexion à dbepic ! \n')
        print('TABLES:')
        insp = inspect(engine)
        print(insp.get_table_names())
    
