# import os
import mysql.connector
import maskpass
from controller.engine_controller import engine
from sqlalchemy import inspect


class StartMenuView:
    def __init__(self):
        pass

    def start_menu_view(self):
            answer = True
            while answer:
                print("""
                1. Administration.
                2. Sign in.
                0. Quit.
                """)
                answer = input("Choice:")
                return answer


    def user_sign_in(self):
        print('Enter Email and then, password: ')
        email = input('Email: ')
        password = maskpass.askpass(prompt="Password:", mask="#")
        return email, password


    def display_tables(self):
        print('TABLES:')
        insp = inspect(engine)
        print(insp.get_table_names())
