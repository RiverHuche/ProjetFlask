from monApp import app, db 
from monApp.models import Livre
# IMPORTANT: Importe la fonction login depuis le fichier où elle est définie
from monApp.tests.functional.test_routes_auteur import login



# 1. TESTS DES ROUTES PUBLIQUES GÉNÉRALES


def test_index_route(client):
    """Teste la route /index/."""
    response = client.get('/index/')
    assert response.status_code == 200
    # CORRECTION : Cherche le texte réel de <h1> pour l'index par défaut
    assert b"Bienvenu Cricri !!" in response.data 

def test_about_route(client):
    """Teste la route /about/."""
    response = client.get('/about/')
    assert response.status_code == 200
    # CORRECTION : Cherche le texte réel de <h1>
    assert b"Bienvenue sur la page \xc3\xa0 propos de Flask" in response.data # "à" en byte

def test_contact_route(client):
    """Teste la route /contact/."""
    response = client.get('/contact/')
    assert response.status_code == 200
    # CORRECTION : Cherche le texte réel de <h1>
    assert b"veuillez nous laisser un message via notre adresse mail" in response.data

def test_logout_route(client):
    """Teste la route /logout/ (doit rediriger vers /index/)."""
    response = client.get('/logout/', follow_redirects=False)
    assert response.status_code == 302
    assert response.headers['Location'] == '/' or response.headers['Location'] == '/index/'


# 2. TESTS DES ROUTES LIVRES (GET)


def test_livres_liste(client):
    """Teste l'accès à la liste des livres (publique)."""
    response = client.get('/livres/')
    assert response.status_code == 200
    # NOTE: Ce test nécessite que le template Jinja soit corrigé.
    assert b'Les Mis\xc3\xa9rables' in response.data 

def test_livre_view(client):
    """Teste l'accès à la page de visualisation d'un livre (ID 1)."""
    response = client.get('/livres/1/view/')
    assert response.status_code == 200
    assert b'15.5' in response.data 


# 3. TESTS DES ROUTES LIVRES (PROTÉGÉES GET/POST)


# --- Route GET /livres/<idL>/update/ ---

def test_livre_update_access_before_login(client):
    """Teste l'accès à la page de modification de livre sans connexion."""
    response = client.get('/livres/1/update/', follow_redirects=True)
    assert b"Login" in response.data

def test_livre_update_access_after_login(client, testapp):
    """Teste l'accès à la page de modification de livre après connexion."""
    with app.app_context():
        response = login(client, "CDAL", "AIGRE", "/livres/1/update/")
        assert response.status_code == 200
        assert b'Les Mis\xc3\xa9rables' in response.data

# --- Route POST /livres/save/ (Modification) ---

def test_livre_save_success(client, testapp):
    """
    Teste la soumission de modification de livre via POST /livres/save/.
    """
    with testapp.app_context():
        # Nécessite tous les arguments du constructeur
        livre = Livre(Prix=10.0, Titre="Livre à modifier", Url="", Img="", auteur_id=1)
        db.session.add(livre)
        db.session.commit()
        idL = livre.idL

    data_to_submit = {
        "idL": idL,
        "Titre": "Nouveau Titre",
        "Prix": 99.99,
        "auteur_id": 1, # ID de l'auteur (Victor Hugo)
        "Url": "http://new.url",
        "Img": "http://new.img"
    }
    
    response = client.post("/livres/save/",
        data=data_to_submit,
        follow_redirects=True
    )
    
    assert response.status_code == 200
    assert f"/livres/{idL}/view/" in response.request.path
    assert b"Nouveau Titre" in response.data
    assert b"99.99" in response.data
    
    with testapp.app_context():
        livre_modifie = Livre.query.get(idL)
        assert livre_modifie.Titre == "Nouveau Titre"
        assert livre_modifie.Prix == 99.99
        
        db.session.delete(livre_modifie)
        db.session.commit()

# --- Route POST /livre/insert/ (Création) ---

def test_livre_insert_after_login_success(client, testapp):
    """
    Teste la création d'un livre via POST /livre/insert/ (Protégée).
    Ceci fonctionnera SEULEMENT après avoir corrigé le TypeError dans routes.py.
    """
    with testapp.app_context():
        initial_count = Livre.query.count()
        
    login(client, "CDAL", "AIGRE", "/") 
    
    data_to_submit = {
        "Titre": "Un livre de test",
        "Prix": 25.0,
        "auteur_id": 1, # ID de l'auteur (Victor Hugo)
        "Url": "http://test.url",
        "Img": "http://test.img"
    }
    
    response = client.post(
        '/livre/insert/', 
        data=data_to_submit,
        follow_redirects=True
    )
    
    assert response.status_code == 200
    assert b"Un livre de test" in response.data
    
    # Nettoyage
    with testapp.app_context():
        assert Livre.query.count() == initial_count + 1
        livre_cree = Livre.query.filter_by(Titre="Un livre de test").first()
        if livre_cree:
            db.session.delete(livre_cree)
            db.session.commit()
