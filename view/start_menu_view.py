# import os
# import mysql.connector
import maskpass


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
