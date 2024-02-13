import bcrypt
from model.users_model import User
from controller.engine_controller import session

class DatabaseMenuView:
    def __init__(self):
        pass


    def menu_db(self):
        
        answer = True
        while answer:
            print("""
            1. Create database.
            2. Create admin startuser.
            3. Delete database.
            4. Quit.
            """)

            answer = input("Choix: ")
            if answer == "1":
                db_name = input('Entrer le nom de la base de donnees à créer: ')
                return 1, db_name   # Renvoi tuple
            if answer == "2":
                # db_name = input('Entrer le nom de la base de donnees à créer: ')
                # return 1, db_name   # Renvoi tuple
                username = "admin"
                password = "admin"
                email = "admin@localhost"
                role = "gestion"

                bytes = password.encode('utf-8')
                hashed_password = bcrypt.hashpw(bytes, bcrypt.gensalt())
                user = User(username, password, hashed_password, email, role)
                session.add(user)   # stage
                session.commit()    # push
                return 2, None

            elif answer == "3":
                db_name = input('Entrer le nom de la base de donnees a supprimer : ')
                return 3, db_name   # Renvoi tuple
            elif answer == "":
                print("\n Choice are 1, 2, 3, 4 : Retry !")
            elif answer == "4":
                return 4, None 
