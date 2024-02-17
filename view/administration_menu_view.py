import os
from mysql import connector
import mysql.connector
from mysql.connector import errorcode
import bcrypt
from model.users_model import User
from controller.engine_controller import EngineController, engine
from dotenv import load_dotenv, dotenv_values
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy import text


load_dotenv()
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")
DB_HOST = os.getenv("DB_HOST")
# db_name = os.getenv('DB_NAME')




class AdministrationMenuView:
    def __init__(self):
        pass


    def administration_menu_view(self):
        # print('env:', os.getenv("DB_PASS"), os.getenv("DB_USER"))
        # self.display_databases()
        answer = True
        while answer:
            print("""
            1. Create database.
            2. Create admin startuser.
            3. Delete database.
            4. Display databases.
            5. Quit.
            """)

            answer = input("Choix: ")
            if answer == "1":
                db_name = input('Entrer le nom de la base de donnees à créer: ')
                return 1, db_name   # Renvoi tuple
            if answer == "2":
                db_name = input('Entrer la base de données à utiliser:')
                return 2, db_name
            elif answer == "3":
                db_name = input('Entrer le nom de la base de donnees a supprimer : ')
                return 3, db_name   # Renvoi tuple
            elif answer == "4":
                return 4, None
            elif answer == "":
                print("\n Choice are 1, 2, 3, 4 : Retry !")
            elif answer == "5":
                return 5, None


    def display_databases(self):
        show_existing_db = "SHOW DATABASES"
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
                        print(db)

        except connector.Error as e:
            print(e)


    
