class DbMenu:
    def __init__(self):
        pass


    def menu_create_database(self):
            print('Création d\'une base de données')
            answer = True
            while answer:
                print("""
                1. Create database.
                2. Quit.
                """)
                answer = input("Choix: ")
                if answer == "1":
                    print('Entrer le nom de la base de données: ')
                elif answer == "2":
                    print("\n Bye!")
                    raise SystemExit
                elif answer == "":
                    print("\n Choice are 1, 2 : Retry !")

                print(answer)