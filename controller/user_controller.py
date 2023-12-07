import os
import datetime

import requests
import jwt
from mysql.connector import connect, Error
from view.user_menu_view import UserMenuView
import sqlalchemy 
from sqlalchemy import URL, insert
from sqlalchemy import create_engine, ForeignKey, text, inspect
from sqlalchemy_utils import database_exists, create_database, drop_database
import mysql.connector
from mysql.connector import connect, Error
from model.users_model import Base, Collaborator, Customer
from sqlalchemy.orm import Session, sessionmaker
import pymysql.cursors
import pymysql






class UserController:
    def __init__(self):
        pass


    def run_table(self, db_name):
        self.display_tables(db_name)
        user_menu = UserMenuView()
        choice, values = user_menu.user_menu_view(db_name)    # value = table_name
        

        if choice == 1:
            username, password = values
            self.user_login(db_name, username, password)
            print('username, password:', db_name, username, password)

        elif choice == 2:
            self.create_collaborator(values)

        elif choice == 3:
            print("\n Bye!")
            raise SystemExit


    def create_collaborator(self, values):
        db_name, ident, username, password, email, role = values
        print('value_table_db_name:', db_name, values[0])
        
        engine = self.create_db_connection(db_name)
        
        Session = sessionmaker(bind=engine)
        session = Session()
        user = Collaborator(ident, username, password, email, role)
        session.add(user)   # stage
        session.commit()    # push

        with engine.connect() as connection:
            result = connection.execute(text("select * from collaborators"))
            for rows in result:
                print("Collaborators:", rows)


    def create_db_connection(self, db_name):
        engine = create_engine(
            "mysql+pymysql://" + os.environ.get('DB_USER') + ":"
            + os.environ.get('DB_PASS') + "@localhost/" + db_name)
        return engine

    def display_tables(self, db_name):
        engine = self.create_db_connection(db_name)
        print('Connexion établie! \n')
        print('TABLES:')
        
        with engine.connect() as connection:
            result = connection.execute(text("SHOW TABLES"))
            for x in result:
                print(x)


    def user_login(self, db_name, username, password):
        
        if password:
            print('password, user, db :', password, username, db_name)
            try:
                conn = mysql.connector.connect(host ="localhost",
                                             user = os.environ.get('DB_USER'),
                                             password = os.environ.get('DB_PASS'),
                                             database = db_name,
                                             )
                cursor = conn.cursor()
                # cursor.execute("SELECT username FROM collaborators")
                cursor.execute("SELECT * FROM collaborators")
                result = cursor.fetchall()
                for row in result:
                    print('rows:', row)
                    
            except mysql.connector.Error as err:
                print('erreur:', err)
        
        """
        if password:
            print('password:', password, username, db_name)
        try:
            conn = mysql.connector.connect(host ="localhost",
                                            database = db_name,
                                            user = username,
                                            password = password,
                                            )
        except mysql.connector.Error as err:
            print('erreur:', err)
        """
        

        """
        auth_token='123456789abcdef'
        headers = {'Authorization': f'Bearer {auth_token}'}
        data = {'app' : 'test_data1'}
        
        url = 'localhost/login'
        response = requests.post(url, json=data, headers=headers)
        print(response)
        print(response.json())
        
        
        urlpatterns = [
        path('admin/', admin.site.urls),
        path('api-auth/', include('rest_framework.urls')),
        path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
        path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
        path('api/', include(router.urls))
        ]

        url = 'https://www.w3schools.com/python/demopage.php'
        myobj = {'somekey': 'somevalue'}

        x = requests.post(url, json = myobj)

        print(x.text)
        """
