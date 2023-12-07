class RegisterMenu():
	def __init__(self)
		pass


	def register_menu(self):
		answer = True

		while answer:
			print("""
                1. Sign in.
                2. Quit.
                """)
				answer = input('Choix')
				return answer

	def sign_in(self):
		username = input('Nom d\'utilisateur: ')
		password = input('Mot de passe: ')
		