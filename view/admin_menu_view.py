

class AdminMenuView:
    def __init__(self):
        pass


    def admin_menu_db(self):
        
        answer = True
        while answer:
            print("""
            1. Create or connect database.
            2. Delete database.
            3. Tables menu.
            4. Quit.
            """)
            
            answer = input("Choix: ")
            if answer == "1":
                db_name = input('Entrer le nom de la base de donnees: ')
                return 1, db_name   # Renvoi tuple
            elif answer == "2":
                db_name = input('Entrer le nom de la base de donnees a supprimer: ')
                return 2, db_name   # Renvoi tuple
            elif answer == "3":
                db_name = input('Entrer le nom de la bd: ')
                return 3, db_name
            elif answer == "":
                print("\n Choice are 1, 2, 3, 4: Retry !")
            elif answer == "4":
                return 4, None 
                
                

    """def admin_menu_table(self):
        answer = True
        while answer:
            print(
            1.Create Table.
            2.Delete Table.
            3.Quit.
            )
            
            answer = input("Choix: ")
            if answer =="1":
                db_name = input ('Entrer le nom de la Base de donnees: ')
                table_name = input('Entrer le nom de la table: ')
                return 1, db_name, table_name
            elif answer == "2":
                db_name = input("Entrer le nom de la base de donnees: ")
                table_name = input('Entrer le nom de la table a supprimer: ')
                return 2, db_name, table_name
            elif answer == "3":
                print("\n Bye!")
                raise SystemExit"""