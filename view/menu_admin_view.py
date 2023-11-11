

class MenuAdminDb:
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
            # 3. Create table.
            # 4. Delete table.
            # 5. Register Gestion Departement User.
            answer = input("Choix: ")
            if answer == "1":                    
                name = input('Entrer le nom de la base de donnees: ')
                return 1, name   # Renvoi tuple sur db_controller
            elif answer == "2":
                name = input('Entrer le nom de la base de donnees a supprimer: ')
                return 2, name   # Renvoi tuple sur db_controller            
            elif answer == "":
                print("\n Choice are 1, 2, 3: Retry !")
            elif answer == "3":
                print("\n Bye!")
                raise SystemExit

            """elif answer =="3":
                name = input('Entrer le nom de la table: ')
                return 3, name
            elif answer == "4":
                name = input('Entrer le nom de la table a supprimer: ')
                return 4, name
            elif answer == "5":
                name = input('Entrer l\' email du collaborateur.')
                return 5, name"""