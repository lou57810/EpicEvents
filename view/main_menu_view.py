import os


class MainMenuView:
    def __init__(self):
        pass

    def main_menu_view(self):
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
    
