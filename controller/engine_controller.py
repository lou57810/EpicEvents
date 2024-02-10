import os

from sqlalchemy.orm import Session, sessionmaker

from sqlalchemy import create_engine
import bcrypt

username = os.environ.get('DB_USER')
password = os.environ.get('DB_PASS')
engine = create_engine("mysql+pymysql://" + username + ":" + password + "@localhost/" + 'dbepic')

Session = sessionmaker(bind=engine)
session = Session()



class EngineController:

    def __init__(self):
        pass


    def start_engine(self, db_name):
        username = os.environ.get('DB_USER')
        password = os.environ.get('DB_PASS')
        engine = create_engine("mysql+pymysql://" + username + ":" + password + "@localhost/" + db_name)
        return engine


