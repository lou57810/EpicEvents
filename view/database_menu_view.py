import os
import bcrypt
from model.users_model import User
from controller.engine_controller import EngineController, engine
from dotenv import load_dotenv, dotenv_values
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy import text


load_dotenv()
# db_name = os.getenv('DB_NAME')


class DatabaseMenuView:
    def __init__(self):
        pass


    def menu_db(self):
        print('env:', os.getenv("DB_PASS"), os.getenv("DB_USER"))
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
                dbName = os.getenv("DB_NAME")
                app = EngineController()
                Engine = app.start_engine(dbName)
                Session = sessionmaker(bind=Engine)
                Session = Session()
                user_id = Session.query(User).filter_by(id=1).one_or_none()
                print('user_id:', user_id)
                if user_id:
                    print('SuperUser déjà créé!')
                    self.menu_db
                else:
                    print('user_id:', user_id)
                    # db_name = input('Entrer le nom de la base de donnees à créer: ')
                    # return 1, db_name   # Renvoi tuple
                    username = os.getenv("DB_ADMIN")
                    password = os.getenv("DB_ADMIN_PASS")
                    email = os.getenv("DB_ADMIN_MAIL")
                    role = os.getenv("DB_DEPARTMENT")

                    bytes = password.encode('utf-8')
                    hashed_password = bcrypt.hashpw(bytes, bcrypt.gensalt())
                    user = User(username, password, hashed_password, email, role)
                    Session.add(user)   # stage
                    Session.commit()    # push
                    self.menu_db
                return 2, dbName

            elif answer == "3":
                db_name = input('Entrer le nom de la base de donnees a supprimer : ')
                return 3, db_name   # Renvoi tuple
            elif answer == "4":
                self.display_databases()
                return 4, None
            elif answer == "":
                print("\n Choice are 1, 2, 3, 4 : Retry !")
            elif answer == "5":
                return 5, None


    def display_databases(self):
        print('Mysql is starting ! \n')
        print('DATABASES:')
        
        with engine.connect() as connection:
            result = connection.execute(text("SHOW DATABASES"))
            for x in result:
                print(x)
        connection.close()
        from controller.start_menu_controller import StartMenuController
        menu_app = StartMenuController()
        menu_app.run_db()
