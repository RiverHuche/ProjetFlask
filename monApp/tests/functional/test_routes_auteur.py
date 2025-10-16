from monApp import app


def test_auteurs_liste(client):  # client est la fixture définie dans conftest.py
    response = client.get('/auteurs/')
    assert response.status_code == 200
    assert b'Victor Hugo' in response.data

def test_auteur_update_before_login(client):
    response = client.get('/auteurs/1/update/', follow_redirects=True)
    assert b"Login" in response.data # vérifier redirection vers page Login

def login(client, username, password, next_path):
    return client.post( "/login/",
                       data={"Login": username,"Password": password, "next":next_path} ,
                       follow_redirects=True)

def test_auteur_update_after_login(client,testapp):
    with app.app_context():
        # user non connecté
        response=client.get('/auteurs/1/update/', follow_redirects=False)
        # Redirection vers la page de login
        assert response.status_code == 302
        # vérification redirection vers page Login
        assert "/login/?next=%2Fauteurs%2F1%2Fupdate%2F" in response.headers["Location"]
        # simulation connexion user
        response=login(client, "CDAL", "AIGRE", "/auteurs/1/update/")
        # Page update après connexion
        assert response.status_code == 200
        assert b"Modification de l'auteur Victor Hugo" in response.data

def test_auteur_view(client):
    """Teste l'accès à la page de visualisation d'un auteur (publique)."""
    response = client.get('/auteurs/1/view/')
    assert response.status_code == 200
    # Vérifie que le nom de l'auteur est présent sur la page
    assert b'Victor Hugo' in response.data
    # Vérifie qu'un champ de formulaire est présent (pour le formulaire de vue)
    assert b'Nom' in response.data

def test_auteur_delete_before_login(client):
    """Teste l'accès à la page de suppression sans être connecté (doit rediriger)."""
    # follow_redirects=True permet de suivre la redirection vers /login/
    response = client.get('/auteurs/1/delete/', follow_redirects=True)
    # Vérifie que la page de login est affichée
    assert b"Login" in response.data 
    # Optionnel : vérifier que le statut de la réponse finale est 200 (après redirection)
    assert response.status_code == 200

def test_auteur_delete_after_login(client, testapp):
    """Teste l'accès à la page de suppression après connexion (doit être OK)."""
    with app.app_context():
        # 1. Tenter d'accéder (user non connecté)
        response = client.get('/auteurs/1/delete/', follow_redirects=False)
        # Vérification de la redirection (302)
        assert response.status_code == 302
        
        # 2. Simuler connexion user et suivre la redirection vers la page de suppression
        # Assurez-vous que l'utilisateur 'CDAL' existe et que 'AIGRE' est son mot de passe non haché.
        response = login(client, "CDAL", "AIGRE", "/auteurs/1/delete/")
        
        # 3. Vérifier la page de suppression après connexion
        assert response.status_code == 200
        # Vérifie que le titre de la page de suppression est affiché
        assert b"Suppression de l'auteur" in response.data
        # Vérifie que l'auteur ciblé est mentionné
        assert b'Victor Hugo' in response.data

def test_auteur_create_access(client):
    """Teste l'accès à la page de création d'un auteur (publique)."""
    response = client.get('/auteur/')
    assert response.status_code == 200
    # Vérifie qu'un formulaire de création est présent
    assert b"Cr\xc3\xa9ation d'un auteur" in response.data # Utilise la version byte de "Création"
    # Vérifie la présence du champ Nom
    assert b'Nom' in response.data

def test_auteur_insert_before_login(client):
    """Teste la soumission du formulaire de création sans être connecté (doit rediriger)."""
    # Simulation de la soumission d'un formulaire valide vers /auteur/insert/
    response = client.post(
        '/auteur/insert/', 
        data={'Nom': 'Jules Verne'},
        follow_redirects=True
    )
    
    # Vérifie que la page de login est affichée (car la route est protégée)
    assert b"Login" in response.data
    assert response.status_code == 200

def test_auteur_insert_after_login(client, testapp):
    """Teste la soumission du formulaire de création après connexion (doit insérer et rediriger)."""
    
    # Déterminer le prochain ID pour la vérification
    with app.app_context():
        from monApp.models import Auteur
        initial_count = Auteur.query.count()
        new_id = initial_count + 1
        
    # 1. Simuler connexion (sans redirection immédiate)
    # L'utilisateur se connecte, puis va manuellement sur la page de création
    response = login(client, "CDAL", "AIGRE", "/") # Connexion standard vers l'index
    
    # 2. Simuler la soumission du formulaire d'insertion (avec le client connecté)
    new_author_name = 'Albert Camus'
    response = client.post(
        '/auteur/insert/', 
        data={'Nom': new_author_name},
        follow_redirects=False # On ne suit pas la redirection tout de suite pour vérifier l'URL
    )
    
    # 3. Vérification de la redirection (doit être vers la vue du nouvel auteur)
    assert response.status_code == 302
    assert response.headers['Location'] == f'/auteurs/{new_id}/view/'
    
    # 4. Suivre la redirection pour s'assurer que l'auteur est bien créé
    response = client.get(response.headers['Location'])
    assert response.status_code == 200
    assert new_author_name.encode('utf-8') in response.data
    
    # Optionnel: Nettoyage (supprimer l'auteur créé)
    with app.app_context():
        from monApp.models import Auteur, db
        auteur_cree = Auteur.query.get(new_id)
        db.session.delete(auteur_cree)
        db.session.commit()