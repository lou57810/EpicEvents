import os

import sqlalchemy
from sqlalchemy import create_engine, ForeignKey, text
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, create_database
from model.users_model import Collaborator


class DbController:
    def __init__(self):
        pass

    def run(self):
        self.test()
        self.create_db_engine()
    """
    collaborator = Collaborator(1, "John Doe", "bla@site.com", "12 32", "Gestion")
    session.add(collaborator)
    session.commit()
    """
    def test(self):
        print('Demarrage du programme. \n')
        print('Version sqlalchemy: ', sqlalchemy.__version__, '\n')
        print('Repertoire de base: ', os.getcwd(),'\n')
        


    def create_db_engine(self):        
        self.dbname = 'dbepic'
        engine = sqlalchemy.create_engine("mysql+pymysql://lou:edwood@localhost/self.dbname", echo=True)        
        if not database_exists(engine.url):
            create_database(engine.url)
            print('Nouvelle Base de donnees:', engine.url)

        else:
            print('DataBase name :', engine.url[3])
        # engine.execute("CREATE DATABASE dbepic") #create db
        # engine.execute("USE dbepic") # select new db
        # Base.metadata.create_all(bind=engine)
        # with db.engine.connect() as conn:
            # result = conn.execute(text(dbepic))
        # conn.execute("commit")

        # Session = sessionmaker(bind=engine)
        # session = Session()
