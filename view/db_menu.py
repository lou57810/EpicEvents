

class DbMenu:
    def __init__(self):
        pass


    def menu_administrator(self):
        print('Creation d\'une base de donnees')
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
                return 1, db_name   # Renvoi tuple sur db_controller
            elif answer == "2":
                db_name = input('Entrer le nom de la base de donnees a supprimer: ')
                return 2, db_name   # Renvoi tuple sur db_controller
            elif answer == "":
                print("\n Choice are 1, 2 : Retry !")
            elif answer == "3":
                print("\n Bye!")
                raise SystemExit
                
    
        
