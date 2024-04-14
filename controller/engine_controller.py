import os
from dotenv import load_dotenv  # dotenv_values
from sqlalchemy.orm import sessionmaker  # Session
from sqlalchemy import create_engine


load_dotenv()
username = os.getenv('DB_USER')
password = os.getenv('DB_PASS')
db_name = os.getenv('DB_NAME')

engine = create_engine(
    "mysql+pymysql://" + username + ":" + password + "@localhost/" + db_name)
Session = sessionmaker(bind=engine)
session = Session()


class EngineController:

    def __init__(self):
        pass

    def start_engine(self, db_name):
        Engine = create_engine(
            "mysql+pymysql://" + username +
            ":" + password + "@localhost/" + db_name)
        return Engine
