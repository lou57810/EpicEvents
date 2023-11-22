from mysql.connector import connect, Error
from view.user_menu_view import UserMenuView
import sqlalchemy
from sqlalchemy import URL
from sqlalchemy import create_engine, ForeignKey, text, inspect
from sqlalchemy_utils import database_exists, create_database, drop_database
import mysql.connector
from mysql.connector import connect, Error
from model.users_model import Base, Collaborator, Customer
# from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Session


class UserController:
    def __init__(self, username, password):
        self.username = username
        self.password = password


    def run_table(self):
        menu_user = UserMenuView()
        choice, value = menu_user.user_menu_view()    # value = table_name
        # menutable = UserMenuView()
        # choice, value_table = menutable.user_menu_view()
        if choice == 1:
            print('db_name:', value)
            self.create_db_connection(value, self.username, self.password)
        elif choice == 2:
            print('table_name: ', value)
            self.create_collaborator(value)
            # choice, value_table = menu_user.user_menu_view()
            # choice, value_table = menu_user.create_collaborator_account()
            # choice, value_table = menu_user.create_collaborator_account()
            # value_table = menu_user.create_collaborator_account()
            # print('values0: ', value_table)
            # self.create_collaborator(value_table)
            
            
        elif choice == 3:
            print("\n Bye!")
            raise SystemExit
        return


    def create_db_connection(self, db_name, username, password):
        engine = create_engine("mysql+pymysql://" + username + ":" + password + "@localhost/" + db_name)
        
        if not database_exists(engine.url):
            create_database(engine.url)
            print('Nouvelle Base de donnees:', db_name)
            self.display_databases()
            Base.metadata.create_all(bind=engine)

        else:
            with engine.connect() as connection:
                result = connection.execute(text('select "Hello"'))
                print('result:', result.all())
                print('You are connected with: ', db_name)
                self.display_tables(engine)
        self.run_table()


    def db_connect(self):
        conn = mysql.connector.connect(
            username = self.username,
            password = self.password,
            host="localhost",
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
            print("Exeception occured:{}".format(e))
        finally:
            conn.close()


    def display_tables(self, engine):
        inspector = inspect(engine)

        for table_name in inspector.get_table_names():
            print('\n')
            print('tables:', table_name)
            for column in inspector.get_columns(table_name):
               print("Column: %s" % column['name'])

    """def define_engine(self):
        engine = create_engine("mysql+pymysql://" + username + ":" + password + "@localhost/" + db_name)
        return engine"""


    def create_collaborator(self, value):
        # menu_user = UserMenuView()
        # db_name, email, password, role = user_app.create_collaborator_account()
        db_name, email, password, role = value
        print('values1:', db_name, email, password, role)
        # engine = self.define_engine()
        engine = create_engine("mysql+pymysql://" + email + ":" + password + "@localhost/" + db_name)
        # connection = sqlalchemy.create_engine(
                # "mysql+mysqlconnector://" + email + ":" + password + "@localhost/" + db_name)   # ?auth_plugin=mysql_native_password
        
        with Session(engine) as session:
            new_collaborator = Collaborator(db_name, email=email, password=password, role=role)
            session.add(new_collaborator)
            session.commit()
        
        """connection = engine.connect()
        # make a cursor to run sql queries
        mycursor = connection.cursor()
        mycursor.execute("Grant all on *.* to email@localhost")
        mycursor.execute("Show grants for geeksforgeeks@localhost")
        result = mycursor.fetchall()
        print(result)
 
        # commit privileges
        mycursor.execute("Flush Privileges")
 
        # close connection to MySQL
        connection.close()"""
            