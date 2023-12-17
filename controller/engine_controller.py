import os

from sqlalchemy import create_engine
import bcrypt

username = os.environ.get('DB_USER')
password = os.environ.get('DB_PASS')
engine = create_engine("mysql+pymysql://" + username + ":" + password + "@localhost/" + 'dbepic')



class EngineController:

    def __init__(self):
        pass


    def start_engine(self, db_name):
        username = os.environ.get('DB_USER')
        password = os.environ.get('DB_PASS')
        engine = create_engine("mysql+pymysql://" + username + ":" + password + "@localhost/" + db_name)
        return engine

"""
class CryptoController():
    
    def __init__(self):
        pass
        # hashed = bcrypt.hashpw(password, bcrypt.gensalt())


    def encrypt_passwd(self, password):
        passwd = password.encode('utf-8')
        salt = bcrypt.gensalt()
        # hashed_password = bcrypt.hashpw(passwd, salt)
        return passwd, salt



    def decrypt_passwd(self, password, hashed_password):
        
        return bcrypt.checkpw(password.encode("utf-8"), hashed_password)

"""
