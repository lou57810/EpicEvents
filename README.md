![alt logo](img/logo.png)

# Epic Events
#### Epic Events est entreprise de conseil et de gestion dans l'�v�nementiel.
#### Objet: Cr�ation d'un logiciel CRM interne.
#### CRM: Customer Relationship Management.

## Cr�ation d'un environnement virtuel(Windows):
`python -m venv .venv` (.venv pour différencier du fichier .env à créer et définir selon le fichier modèle env_template)
## Linux:
`python3 -m venv .venv`
## Puis activation avec Windows, depuis git bash: 
`source .venv/scripts/activate`
## Ou sur Linux:
`source .venv/bin/activate`

## Installation de mysql et Workbench depuis le site de son nom:
## Cette installation peut nécessiter l'install de Visual Studio C++ 2019.
 https://dev.mysql.com/downloads/

## Installation des packages avec pip:
## En particulier de l'orm sqlalchemy.
`pip install -r requirements.txt`

## Exécuter la commande `mysql -u root -p` pour créer un mot de passe.
## Ce mot de passe pourra vous identifier en ligne de commande et également avec Workbench.
## En ligne de commande nous disposons alors de toutes les commandes mysql.
## Par exemple: ` SHOW DATABASES;` affiche les bases de données.
## Ici en particulier la base de données crée pour Epic Events: dbepic.
## IMPORTANT:
## (Créer au préalable un fichier .env à définir selon le fichier modèle env_template:
## Exemple .env : (Remplacer les '****' par vos choix)
##				DB_PASS = "****"
				DB_USER = "root"
				DB_ADMIN = "****"
				DB_ADMIN_PASS = "****"
				DB_ADMIN_MAIL = "****@localhost"
				DB_DEPARTMENT = "1"
				DB_NAME = "****"
				DB_HOST = "localhost" )
## Ce fichier permettra d'initialiser les variables dans par exemple le fichiers engine_controller.py,
## administration_controller.py et d'autres._
## Démarrer le programme:
`python main.py`
## Affichage:
	1. Administration. (Permet de créer ou de supprimer une base de données, et de créer un administrateur.)
		1. Création de la base de donnée.
		2. Création de l'administrateur:
		3. Suppression de la base de données.
		4. Affichage des bases de données.
		5. Quit
		)
		
		La connection avec Workbench se fera avec en principe "root" et le password défini lors de l'utilisation de mysql.
		Workbench permet d'interagir avec la base de donnée, les tables, et les clés valeurs.
		
	2. Sign in. Permet de se logger en tant que collaborateur. (1ere connection avec par exemple admin@localhost et admin,
		valeurs à définir dans un fichier .env) 
		En fonction de son rôle l'utilisateur,
		sera orienté vers les menus lui étant reservés.
	3. Quit. (Quitte le programme.)

	###      EMAIL				PASSWORD				ROLE
	-------------------------------------------------------
	### Exemle:
	### gestion1@localhost			gestion1			GESTION
	

### 1. Un gestionnaire crée des collaborateurs departement gestion, commercial, et support.
### 2. Le commercial crée un client: 
		- Le client lui est automatiquement affecté.
### 3. Le commercial accepte un contrat evenementiel crée l'évènement et attribue un id au contrat et à l'évènement.
###	4. Le gestionnaire crée un contrat pour le client.
### 5. Le gestionnaire attribue un collaborateur du département support à l'évènement si il n'est pas encore défini.


	###  Lien: https://github.com/lou57810/EpicEvents Mais vous y êtes déjà.
### Remplacement de :
### `flake8 --format=html --htmldir=flake-report --line-max-length 110`
### Par
### `flake8 --format=html --htmldir=flake-report
### flake8 a son propre fichier de confi: .flake8