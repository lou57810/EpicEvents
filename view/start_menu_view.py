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


    """def select_database(self):
        conn = mysql.connector.connect (user='root', password='edwood',
            host='localhost',buffered=True)
        cursor = conn.cursor()
        databases = ("show databases")
        cursor.execute(databases)
        print('#### DATABASES ####')
        i = 0
        db = []
        for (databases) in cursor:
             print(i, ':', databases[0])
             db.append(databases[0])
             i = i + 1
        
        choice = input("Choisir un N° Database:")
        return db[int(choice)]"""
