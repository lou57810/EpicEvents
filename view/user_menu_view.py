# import mysql.connector



class UserMenuView:
    def __init__(self):
        pass


    def user_menu_view(self):
        print("Choose options")
        answer = True
        while answer:
            print("""
            1. Connect database.
            2. Create collaborator.
            3 Quit.
            """)

            
            # 3. Update collaborator.
            # 4. Delete collaborator.
            # 5. Create contracts.
            # 6. Update contracts.
            # 7. Select events.
            # 8. Update events.
            # 9. Create table.
            # 10. Quit.
            
            answer = input("Faites votre choix ! \n")

            if answer == "1":
                db_name = input('Entrer le nom de la base de donnees: ')
                return 1, db_name   # Renvoi tuple
            if answer == "2":
                value_table = self.create_collaborator_account()
                print('value_table:', value_table)
                # email = input('Entrer l\'email collaborateur: ')
                # return 2, email
                # return 2, value_table
                return 2, value_table
            elif answer == "3":
                print("\n Bye!")
                raise SystemExit
            # elif answer == "3":
                # print("\n Update collaborator")
            """elif answer == "4":
                print("\n Delete collaborator")
            elif answer == "5":
                print("\n Create contracts")
            elif answer == "6":
                print("\n Update contracts")
            elif answer == "7":
                print("\n Select events")
            elif answer == "8":
                print("\n Update events")
            elif answer == "9":
                return 8, name  # create_db(db_name, self.username, self.password)
            elif answer == "10":
                print("\n Bye!")
                raise SystemExit
            elif answer == "":
                print("\n Choice are 1, 2, 3, 4, 5, 6, 7, or 8 : Retry!")"""


    def create_collaborator_account(self):
        db_name = input("Nom de la base de donnees: ")
        email = input("collaborator email : ")
        password = input("Mot de passe : ")
        role = input('A quel departement est affecte le nouveau collaborateur ?: ')
        # return db_name, email, password, role
        return db_name, email, password, role


    """
    def user_connect(self):
        # create instance 'mydb'
        mydb = mysql.connector.connect(
            user="root", passwd="edwood",
            host="localhost",  # , database="dbepic",
            auth_plugin="mysql_native_password"
        )
        print("mydb:", mydb)
        
        print('Sign in \n')
        n = 3
        
        #email = "admin"
        #password = "admin"
        # mysql -u root -p dbepic < input.sql
        # Mysql SQL>  connect root@localhost
        
        var_email = input("email : ")
        var_pass = input("password : ")
        if var_pass == password and var_email == email:
            print("You are logged as Gestion Departement User! ")
            # self.menu_create_database()
        else:
            while n > 0:
                var_email = input("email : ")
                var_pass = input("password : ")
                print("retry!")
                n = n - 1
                print('n:', n)
                if n == 0:
                    print("\n Bye!")
                    raise SystemExit
        
    def user_register(self, email, password):
        print('Sign in \n')
        n = 3        
        
        var_email = input("email : ")
        var_pass = input("password : ")
        if var_pass == password and var_email == email:
            print("You are logged as Gestion Departement User! ")
            # self.menu_create_database()
        else:
            while n > 0:
                var_email = input("email : ")
                var_pass = input("password : ")
                print("retry!")
                n = n - 1
                print('n:', n)
                if n == 0:
                    print("\n Bye!")
                    raise SystemExit
        

    def register(self):
        password = "edwood"
        email = "doe@site.com"
        print('Sign in')
        var_email = input("email : ")
        var_pass = input("password : ")
        if var_pass != password or var_email != email:
            print("retry!")
            self.register()
        else:
            print("You are logged ! ")
            self.display_collaborator_menu()

    def display_collaborator_menu(self):
        print("Choose options")
        answer = True
        while answer:
            print(triple quote            
            1. Commercial Departement.
            2. Support Departement.
            3. Quit
            triple quote)
            answer = input("Faites votre choix ! \n")

            if answer == "1":
                print("\n Departement Commercial")
                self.register()
            elif answer == "2":
                print("\n Departement Support")
                self.register()
            elif answer == "3":
                print("\n Bye!")
                raise SystemExit
            elif answer == "":
                print("\n Choice are 1, 2, or 3!")
     """    

