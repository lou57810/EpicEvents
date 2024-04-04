# import os
# import mysql.connector
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
            answer = input("Select N° Menu:  ")
            return answer

    def input_email(self):
        email = input('Email: ')
        return email

    def input_password(self):
        password = maskpass.askpass(prompt="Enter Password:", mask="#")
        return password

    """def display_tables(self):
        print('TABLES: ')
        insp = inspect(engine)
        print(insp.get_table_names())"""
