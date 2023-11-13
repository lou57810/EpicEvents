

class MenuAdminDb:
    def __init__(self):
        pass


    def menu_administrator(self):
        
        answer = True
        while answer:
            print("""
            1. Create database.
            2. Delete database.
            3. Create table.
            4. Delete table.
            5. Register Gestion Departement User.
            6. Quit.
            """)
            
            answer = input("Choix: ")
            if answer == "1":
                db_name = input('Entrer le nom de la base de donnees: ')
                return 1, db_name   # Renvoi tuple
            elif answer == "2":
                db_name = input('Entrer le nom de la base de donnees a supprimer: ')
                return 2, db_name   # Renvoi tuple            
            elif answer =="3":
                db_table = input('Entrer le nom de la table: ')
                return 3, db_table
            elif answer == "4":
                db_table = input('Entrer le nom de la table a supprimer: ')
                return 4, db_table
            elif answer == "5":
                email = input('Entrer l\' email du collaborateur.')
                return 5, email
            elif answer == "":
                print("\n Choice are 1, 2, 3: Retry !")
            elif answer == "6":
                print("\n Bye!")
                raise SystemExit