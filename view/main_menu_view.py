
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
