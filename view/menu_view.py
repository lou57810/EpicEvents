
class Menu:
    def __init__(self):
        pass


    def menu_gestion_admin(self):
        print("Choose options")
        answer = True
        while answer:
            print("""            
            1. Create collaborator.
            2. Update collaborator.
            3. Delete collaborator.
            4. Create contracts.
            5. Update contracts.
            6. Select events.
            7. Update events.
            8. Quit.                    
            """)
            answer = input("Faites votre choix ! \n")

            if answer == "1":
                print("\n Creer un collaborateur.")
                self.create_collaborator_account()
            elif answer == "2":
                print("\n Update collaborator")
            elif answer == "3":
                print("\n Delete collaborator")
            elif answer == "4":
                print("\n Create contracts")
            elif answer == "5":
                print("\n Update contracts")
            elif answer == "6":
                print("\n Select events")
            elif answer == "7":
                print("\n Update events")
            elif answer == "8":
                print("\n Bye!")
                raise SystemExit
            elif answer == "":
                print("\n Choice are 1, 2, 3, 4, 5, 6, 7, or 8 : Retry!")

    def create_collaborator_account(self):
        complete_name = input("Renseignez le nom suivi du prénom : ")
        email = input("Renseignez l' email: ")
        tel = input('Renseignez le n° de téléphone: ')
        role = input('A quel département est affecté le nouveau collaborateur ?: ')
        print('result:', complete_name, email, tel, role)


    def admin_register(self):        
        email = "admin"
        password = "admin"
        print('Sign in \n')
        var_email = input("email : ")
        var_pass = input("password : ")
        if var_pass != password or var_email != email:
            print("retry!")
            self.register()
        else:
            print("You are logged as Root Administrator User! ")
            # self.menu_create_database()

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
            print("""            
            1. Commercial Departement.
            2. Support Departement.
            3. Quit
            """)
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


