from mysql.connector import connect, Error
from view.user_menu_view import UserMenu
from sqlalchemy import URL
from sqlalchemy import create_engine, ForeignKey, text
from sqlalchemy_utils import database_exists, create_database, drop_database
import mysql.connector
from mysql.connector import connect, Error


class UserController:
    def __init__(self, username, password):
        self.username = username
        self.password = password


    def run(self):
        menuApp = UserMenu()
        choice, db_name = menuApp.menu_user() 
        if choice == 1:
            print('db_name:', db_name)
            self.create_db(db_name, self.username, self.password)


    def create_db(self, db_name, username, password):
        # "<dialect>+<driver>://<username>:<password>@<host>/<database>"
        # example mysql:
        # mysql_db_url = "mysql://<username>:<password>@<hostname>:<port>/<database>"
        self.display_databases()
        url_object = URL.create(
                    "mysql+pymysql",
                    username = username,
                    password = password,
                    host="localhost",
                    database="dbepic",
                )
        engine = create_engine(url_object)
        
        if not database_exists(engine.url):
            create_database(engine.url)
            print('Bad database, Retry !')
            
        else:
            print(db_name, 'Ok, start working !')
        self.display_databases()
        self.run()

    def create_table(self):
        engine = self.db_connect()
        Base.metadata.create_all(bind=engine)


    def db_connect(self):
        conn = mysql.connector.connect(
            # username = "lou", password = "edwood",
            username = self.username,
            password = self.password,
            host="localhost",
            # auth_plugin="mysql_native_password"
            )
        return conn


    def display_databases(self):
        conn = self.db_connect()

        try:
            # Create a cursor object
            if conn.is_connected():
                print('Connected to MySQL database')
                mycursor = conn.cursor()
                mycursor.execute("SHOW DATABASES")
                rows = mycursor.fetchall()
                for row in rows:
                    print(row)

        except Exception as e:
            print("Exception occured:{}".format(e))
        finally:
            conn.close()