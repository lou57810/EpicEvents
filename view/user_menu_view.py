# import mysql.connector



class UserMenuView:
    def __init__(self):
        pass


    def user_menu_view(self, db_name):
        print("Choose options")
        answer = True
        while answer:
            print("""
            1. Create collaborator.
            2. Quit.
            """)

            answer = input("Faites votre choix ! \n")
            if answer == "1":
                value_table = self.create_collaborator_account(db_name)
                return 1, value_table
            elif answer == "2":
                return 2, None


    def create_collaborator_account(self, db_name):
        ident = input('Identifiant numérique: ')
        username = input('Nouvel utilisateur: ')
        password = input ('Password: ')
        email = input("collaborator email : ")
        role = input('A quel departement est affecte le nouveau collaborateur ?: ')
        return db_name, ident, username, password, email, role
