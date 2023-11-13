
class MainMenu:
    def __init__(self):
        pass

    def main_menu(self):
            print("Choose options:")
            answer = True
            while answer:
                print("""
                1. Administrateur.
                2. EpicEvent user.
                3. Quit.
                """)
                answer = input("Choix:")
                return answer


    def menu_sign_in(self):
        print("sign_in: ")
        user_name = input('Nom d\'utilisateur: ')
        password = input('Mot de passe: ')
        return user_name, password
