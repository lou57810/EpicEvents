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
	1. Administration. (Permet de créer ou de supprimer une base de données.)
	2. Sign in. (Permet de se logger en tant que collaborateur. En fonction de son rôle l'utilisateur, sera orienté vers les commandes lui étant reservées.)
	3. Quit. (Quitte le programme.)

	###      EMAIL		    PASSWORD		ROLE
	### admin@localhost     admin           GESTION     #  compte générique sans hachage.

	### user2@localhost		user2			GESTION
	### user3@localhost		user3			COMMERCIAL
	### user4@localhost		user4			SUPPORT
	### user5@localhost		user5			GESTION
	### user6@localhost		user6			SUPPORT
	### user7@localhost		user7			COMMERCIAL
	### user8@localhost		user8			COMMERCIAL