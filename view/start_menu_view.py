import os


class StartMenuView:
    def __init__(self):
        pass

    def start_menu_view(self):
            print("Choose options (main_menu_view):")
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
    
