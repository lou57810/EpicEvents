import os
from dotenv import load_dotenv, dotenv_values

from sqlalchemy.orm import Session, sessionmaker

from sqlalchemy import create_engine
import bcrypt
load_dotenv()
username = os.getenv('DB_USER')
password = os.getenv('DB_PASS')
db_name = os.getenv('DB_NAME')
print('username, password:', username, password)
# username = os.environ.get('DB_USER')
# password = os.environ.get('DB_PASS')
# engine = create_engine("mysql+pymysql://" + username + ":" + password + "@localhost/" + 'dbepic')
engine = create_engine("mysql+pymysql://" + username + ":" + password + "@localhost/" + db_name)
print('engine:', engine)

Session = sessionmaker(bind=engine)
session = Session()



class EngineController:

    def __init__(self):
        pass


    def start_engine(self, db_name):
        # username = os.getenv('DB_USER')
        # password = os.getenv('DB_PASS')
        print('username, password:', username, password)
        Engine = create_engine("mysql+pymysql://" + username + ":" + password + "@localhost/" + db_name)
        print("engine2:", Engine)
        return Engine


