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
                2. other databases.
                3. Quit.
                """)
                answer = input("Choix:")
                return answer


    def menu_sign_in(self):
        # print("sign_in: ")
        username = os.environ.get('DB_USER')
        password = os.environ.get('DB_PASS')
        db_name = input('Database: ')
        # username = input('Nom d\'utilisateur: ')
        # password = input('Mot de passe: ')
        return db_name, username, password

        
