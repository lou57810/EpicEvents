![alt logo](img/logo.png)

# Epic Events
#### Epic Events est entreprise de conseil et de gestion dans l'�v�nementiel.
#### Objet: Cr�ation d'un logiciel CRM interne.
#### CRM: Customer Relationship Management.

## Cr�ation d'un environnement virtuel:
`python -m venv env`
## Puis activation avec Windows, depuis git bash:
`source env/scripts/activate`
## Ou sur Linux:
`source env/bin/activate`

## Installation de mysql depuis le site de son nom.

## Installation des packages avec pip:
## En particulier de l'orm sqlalchemy.
`pip install -r requirements.txt`

## Installer mysql depuis le site: https://dev.mysql.com/downloads/
## Installer en même temps mysql Workbench.

## Exécuter la commande `mysql -u root -p` pour créer un mot de passe.
## Ce mot de passe pourra vous identifier en ligne de commande et également avec Workbench.
## En ligne de commande nous disposons alors de toutes les commandes mysql.
## Par exemple: ` SHOW DATABASES;` affiche les bases de données.
## Ici en particulier la base de données crée pour Epic Events: dbepic.
## Démarrer le programme:
`python main.py`
## Affichage:
	1. Administration. (Permet de créer ou de supprimer une base de données, et de créer un administrateur.)
		1. Création de la base de donnée.
		2. Création de l'administrateur:	(email: admin@localhost password: admin)
		3. Suppression de la base de données.
		4. Affichage des bases de données.
		5. Quit
		
		La connection avec Workbench se fera avec root et "edwood" comme password.
		
	2. Sign in. Permet de se logger en tant que collaborateur. (1ere connection avec admin@localhost et admin) 
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

### `flake8 --format=html --htmldir=flake-report --line-max-length 110`