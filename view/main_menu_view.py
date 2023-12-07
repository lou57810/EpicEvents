import os


class MainMenuView:
    def __init__(self):
        pass

    def main_menu_view(self):
            print("Choose options:")
            answer = True
            while answer:
                print("""
                1. Administrateur mysql.
                2. Choose and Connect database.
                3. Quit.
                """)
                answer = input("Choix:")
                return answer


    
    def choose_db_and_connect(self):
        db_name = input('Database: ')
        return db_name
