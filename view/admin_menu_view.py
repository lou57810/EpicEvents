

class AdminMenuView:
    def __init__(self):
        pass


    def admin_menu_db(self):
        
        answer = True
        while answer:
            print("""
            1. Create database.
            2. Delete database.
            3. Quit.
            """)

            answer = input("Choix: ")
            if answer == "1":
                db_name = input('Entrer le nom de la base de donnees: ')
                return 1, db_name   # Renvoi tuple
            elif answer == "2":
                db_name = input('Entrer le nom de la base de donnees a supprimer: ')
                return 2, db_name   # Renvoi tuple
            elif answer == "":
                print("\n Choice are 1, 2, 3, 4 : Retry !")
            elif answer == "3":
                return 3, None 
