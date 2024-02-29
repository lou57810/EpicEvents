


class UserMenuView:
    def __init__(self):
        pass


    def user_menu_view(self, db_name):
        print("Choose options for(user_menu_view):", db_name)
        answer = True
        while answer:
            print("""
            1. Sign in.
            2. Quit.
            """)

            answer = input("Faites votre choix ! \n")
            if answer == "1":
                login_data = self.user_sign_in()
                return 1, login_data
            elif answer == "2":
                return 2, None

    def user_sign_in(self):
        # from controller.gestion_controller import GestionController
        # gestion_app = GestionController()
        email = input('Email: ')
        # pwd = maskpass.askpass(prompt="Password:", mask="#")
        # print('pwd:', pwd)
        password = str(input('Password: '))
        # password = pwd
        return email, password



    
