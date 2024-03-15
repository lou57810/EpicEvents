import os

from mysql import connector
from controller.engine_controller import engine  # EngineController,
from dotenv import load_dotenv  # , dotenv_values
from sqlalchemy import inspect  # text, 


# import depuis .env
load_dotenv()
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")
DB_HOST = os.getenv("DB_HOST")
# db_name = os.getenv('DB_NAME')




class AdministrationMenuView:
    def __init__(self):
        pass


    def administration_menu_view(self):
        answer = True
        while answer:
            print("""
            1. Create database.
            2. Create admin startuser.
            3. Delete database.
            4. Display databases.
            0. Start Menu.
            """)

            answer = input("Choix: ")
            # Db creation:
            if answer == "1":
                self.display_databases()
                db_name = input('Entrer le nom de la base de donnees à créer: ')
                return 1, db_name   # Renvoi 
            # Admin user creation 
            if answer == "2":
                db_name = input('Entrer la base de données à utiliser(dbepic):')
                return 2, db_name
            # Db deletion
            elif answer == "3":
                self.display_databases()
                db_name = input('Entrer le nom de la base de donnees a supprimer : ')
                return 3, db_name   # Renvoi tuple
            # Return Menu and Db display
            elif answer == "4":
                return 4, None
            # Bad entry
            elif answer == "":
                print("\n Choice are 1, 2, 3, 4 : Retry !")
            # Return start_menu
            elif answer == "0":
                return 0, None


    def display_databases(self):
        print('DATABASES:')
        show_existing_db = "SHOW DATABASES"
        db_list = []
        try:
            with connector.connect(
                host = DB_HOST,
                user = DB_USER,
                password = DB_PASS
            ) as database:
                # print(database)
                with database.cursor() as cursor: 
                    cursor.execute(show_existing_db)
                    for db in cursor:
                        db_list.append(db)
                        print(db)

        except connector.Error as e:
            print(e)
        return db_list


    def display_tables(self):
        print('\n')
        print('Connexion à dbepic ! \n')
        print('TABLES:')
        insp = inspect(engine)
        print(insp.get_table_names(), '\n')
