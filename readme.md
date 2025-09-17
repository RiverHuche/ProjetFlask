# ProjetFlask
 
 pip freeze > requirements.txt -> sert à indiquer les informations nécessaires pour lancer le projet.

 Un paquet est essentiellement un ensemble de modules python rassemblés dans un même dossier. Il est ensuite possible de rajouter facilement un sous-module d'un paquet dans l'espace de noms courant, afin de pouvoir utiliser les variables et les méthodes qu'il propose.

 j'ai oublié de faire mon readme dans la 1ère séance.

#### Séance 2
importer toutes les variables en une fois dans votre projet en utilisant la méthode
config.from_object(file_name)

db.session.add() : Cette méthode permet d'ajouter un enregistrement à la base. En paramètres,
vous passez l'instance de l'objet que vous voulez créer.

db.session.commit() : Chaque création est ajoutée dans une session. Lorsque vous avez terminé
d'ajouter des éléments, vous devez indiquer à SQLAlchemy de faire les requêtes dans la base pour
finaliser l'opération.

##### Séance 3

ajustement de la view ABOUT, notamment de l'import. 
ajout de la base de données monApp.db avec la commande loaddb
Réalisation des commandes dans le shell

## RiverHuche

###