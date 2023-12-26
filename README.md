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

	### admin compte générique sans hachage.
	### user2 password user2 GESTION
	### user3 password user3 COMMERCIAL
	### user4 password user4 SUPPORT