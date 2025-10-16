# ProjetFlask
 
 pip freeze > requirements.txt -> sert à indiquer les informations nécessaires pour lancer le projet.

 Un paquet est essentiellement un ensemble de modules python rassemblés dans un même dossier. Il est ensuite possible de rajouter facilement un sous-module d'un paquet dans l'espace de noms courant, afin de pouvoir utiliser les variables et les méthodes qu'il propose.

 j'ai oublié de faire mon readme dans la 1ère séance.

## Séance 2
importer toutes les variables en une fois dans votre projet en utilisant la méthode
config.from_object(file_name)

db.session.add() : Cette méthode permet d'ajouter un enregistrement à la base. En paramètres,
vous passez l'instance de l'objet que vous voulez créer.

db.session.commit() : Chaque création est ajoutée dans une session. Lorsque vous avez terminé
d'ajouter des éléments, vous devez indiquer à SQLAlchemy de faire les requêtes dans la base pour
finaliser l'opération.

## Séance 3

ajustement de la view ABOUT, notamment de l'import. 
ajout de la base de données monApp.db avec la commande loaddb
Réalisation des commandes dans le shell

Ajout d'une views contact (oubli TP1)


## Séance 4

Ajout du fichier index.html dans templates.
Affichage de la template du fichier index.html dans la méthode index().
modification d'import dans le fichier __init qui faisait bug le chargement des vues.
Ajout des templates pour les deux autres vues : contact et about.

## Séance 5 

Scinder index en 2 parties, avec base.html et index.html en implémentant ud nouveau code

## Séance 6

Mise à jour de la base html,pour un rendu plus fluide et agréable à travers un menu, un bootstrap etc..

Debut TP5
installation de pip flask-wtf
Ajout d'une route auteur avec un idA, soit ajout d'une vue pour ce dernier

## Suite TP5

 Ajout d'une template auteur_update pour compléter la vue ajouté précédement, permettant de mettre à jour les données sur un auteur.

 Ajout d'une view pour permettre de sauvegarder les modifications apportées à un auteur, puis d'une template auteur_update.html pour mettre en place l'action sur le formulaire. et enfin création d'une template auteur_view.html pour illustrer la vue ajoutée.

Ajout du support pour visualiser erreurs de validation. màj template auteur_update.html

Ajout d'une fonctionnalité "ajout d'un auteur", donc ajout de la fonctionnalité dans le menu, puis création de la vue et de la template pour permettre la réalisation de cette action, et ajout d'une autre vue insertAuteur pour validé la création.

Ajout de vues pour permettre la suppression d'un auteur, via deleteAuteur et eraseAuteur pour valider l'action de suppression, et inévitablement implémentation d'une template auteur_delete.html pour afficher et prendre en compte la confirmation de la suppression

Réitération sur Livre de presque toutes les modifications apportées sur Auteur, soit juste ajout d'un livres_view.html et d'un livres_update.html et de leur ves, car on ne cherche pas à supprimer ni ajouter de livres.


## TP6

Ajout d'une classe User pour permettre l'authentification des utilisateurs sur l'application, mise à jour également dans la base de données.

Ajout d'une fonction dans la BD (newuser) permettant d'ajouter un nouvel utilisateur à la BD

Ajout d'une fonction newpasswrd pour changer le mdp d'un utilisateur déjà existant.

## Suite TP6

Mise en place de l'authentification avec l'extension Flask-Login.

Installation de la dépendance :

pip install flask-login

Modification du modèle User dans models.py pour qu'il hérite de UserMixin et implémente la méthode get_id(), comme requis par Flask-Login.

Ajout d'une fonction user_loader pour permettre à Flask-Login de récupérer un utilisateur depuis la base de données à partir de son identifiant de session.

Création d'un formulaire de connexion LoginForm dans forms.py. Ce formulaire inclut une méthode get_authenticated_user() pour vérifier si l'identifiant et le mot de passe sont corrects.

Ajout de la vue login() et de son template login.html pour afficher le formulaire et gérer la connexion de l'utilisateur.

Mise à jour de la barre de navigation dans base.html pour afficher dynamiquement l'état de connexion : un lien "Se connecter" pour les visiteurs, ou le nom de l'utilisateur et un lien "Déconnexion" pour les utilisateurs authentifiés.

Création de la vue logout() pour permettre la déconnexion.

Protection des routes de création, modification et suppression avec le décorateur @login_required. Désormais, seul un utilisateur connecté peut accéder à ces fonctionnalités.

Mise en place d'une redirection automatique. Si un utilisateur non connecté tente d'accéder à une page protégée, il est automatiquement redirigé vers la page de connexion. Après s'être connecté, il est ensuite redirigé vers la page qu'il essayait d'atteindre initialement.

## TP7

Mise en place de l'environnement de test pour assurer la fiabilité de l'application.

Installation des outils de test :

pip install pytest pytest-flask coverage

Création d'un fichier de configuration conftest.py à la racine du dossier tests/. Ce fichier met en place une application de test et une base de données en mémoire (sqlite:///:memory:) pour que les tests n'affectent pas la base de données de développement.

Réalisation de tests unitaires sur les modèles (User, Auteur, Livre). Ces tests vérifient que les objets sont créés correctement et que leurs méthodes (comme repr) fonctionnent comme prévu.

Réalisation de tests fonctionnels sur les vues. Ces tests simulent des requêtes HTTP (GET et POST) vers l'application et vérifient que :

    Les pages publiques (liste des auteurs, des livres) se chargent correctement pour tout le monde. 

L'accès aux pages protégées sans être connecté provoque bien une redirection vers la page de login.

La connexion fonctionne et permet d'accéder aux pages protégées.

La soumission des formulaires (ajout, modification, suppression) fonctionne et met bien à jour la base de données.

Utilisation de l'outil coverage pour mesurer la couverture de test du code. Lancement des tests avec la commande coverage run -m pytest et génération de rapports pour identifier les parties du code non testées. L'objectif est d'atteindre une couverture supérieure à 90% pour garantir la robustesse de l'application.

# RiverHuche BUT2 2A

