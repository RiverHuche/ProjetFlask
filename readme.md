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

Ajout d'une views contact (oubli TP1)


##### Séance 4

Ajout du fichier index.html dans templates.
Affichage de la template du fichier index.html dans la méthode index().
modification d'import dans le fichier __init qui faisait bug le chargement des vues.
Ajout des templates pour les deux autres vues : contact et about.

##### Séance 5 

Scinder index en 2 parties, avec base.html et index.html en implémentant ud nouveau code

##### Séance 6

Mise à jour de la base html,pour un rendu plus fluide et agréable à travers un menu, un bootstrap etc..

Debut TP5
installation de pip flask-wtf
Ajout d'une route auteur avec un idA, soit ajout d'une vue pour ce dernier

##### Suite TP5

 Ajout d'une template auteur_update pour compléter la vue ajouté précédement, permettant de mettre à jour les données sur un auteur.

 Ajout d'une view pour permettre de sauvegarder les modifications apportées à un auteur, puis d'une template auteur_update.html pour mettre en place l'action sur le formulaire. et enfin création d'une template auteur_view.html pour illustrer la vue ajoutée.

Ajout du support pour visualiser erreurs de validation. màj template auteur_update.html

Ajout d'une fonctionnalité "ajout d'un auteur", donc ajout de la fonctionnalité dans le menu, puis création de la vue et de la template pour permettre la réalisation de cette action, et ajout d'une autre vue insertAuteur pour validé la création.

Ajout de vues pour permettre la suppression d'un auteur, via deleteAuteur et eraseAuteur pour valider l'action de suppression, et inévitablement implémentation d'une template auteur_delete.html pour afficher et prendre en compte la confirmation de la suppression

Réitération sur Livre de presque toutes les modifications apportées sur Auteur, soit juste ajout d'un livres_view.html et d'un livres_update.html et de leur ves, car on ne cherche pas à supprimer ni ajouter de livres.


##### TP6

Ajout d'une classe User pour permettre l'authentification des utilisateurs sur l'application, mise à jour également dans la base de données.

Ajout d'une fonction dans la BD (newuser) permettant d'ajouter un nouvel utilisateur à la BD

Ajout d'une fonction newpasswrd pour changer le mdp d'un utilisateur déjà existant.


## RiverHuche

