from monApp.models import Auteur
from monApp.app import db # Importez 'db' depuis 'monApp.app' si nécessaire
from monApp.tests.functional.test_routes_auteur import login # Importez la fonction de connexion (peut être inutile ici)

def test_auteur_save_success(client, testapp):
    # Créer un auteur dans la base de données
    with testapp.app_context():
        auteur = Auteur(Nom="Ancien Nom")
        db.session.add(auteur)
        db.session.commit()
        idA = auteur.idA
        
    # La route /auteur/save/ n'est pas protégée par login_required. 
    # La ligne de connexion ci-dessous est donc superflue pour la soumission POST.
    # response=login(client, "CDAL", "AIGRE", "/auteur/save/")

    # Soumission du formulaire de modification
    response = client.post("/auteur/save/",
        data={"idA": idA, "Nom": "Alexandre Dumas"},
        follow_redirects=True
    )
    
    # Vérifier que la redirection a eu lieu vers /auteurs/<idA>/view/ et que le contenu
    # est correct
    assert response.status_code == 200
    # Vérifie que le chemin final de la requête est bien la page de vue
    assert f"/auteurs/{idA}/view/" in response.request.path 
    assert b"Alexandre Dumas" in response.data # contenu de la page vue
    
    # Vérifier que la base a été mise à jour
    with testapp.app_context():
        auteur = Auteur.query.get(idA)
        assert auteur.Nom == "Alexandre Dumas"

    
def test_auteur_insert_after_login_success(client, testapp):
    """
    Teste la création d'un auteur via POST /auteur/insert/ après connexion.
    Doit insérer l'auteur et rediriger vers la page de vue.
    """
    
    # 1. Déterminer le prochain ID (pour la vérification de la redirection)
    with testapp.app_context():
        # L'ID de l'auteur créé sera le nombre actuel + 1
        from monApp.models import Auteur 
        initial_count = Auteur.query.count()
        new_id = initial_count + 1
        
    # 2. Simuler connexion de l'utilisateur (Login: CDAL, Mdp: AIGRE)
    # L'utilisateur se connecte, ce qui établit la session
    login(client, "CDAL", "AIGRE", "/") 
    
    # 3. Simuler la soumission du formulaire d'insertion (avec le client connecté)
    new_author_name = 'Albert Camus'
    response = client.post(
        '/auteur/insert/', 
        data={'Nom': new_author_name},
        follow_redirects=False # On vérifie la redirection (302)
    )
    
    # 4. Vérification de la redirection (doit être vers la vue du nouvel auteur)
    assert response.status_code == 302
    assert response.headers['Location'] == f'/auteurs/{new_id}/view/'
    
    # 5. Suivre la redirection pour s'assurer que l'auteur est bien créé (200 OK)
    response_view = client.get(response.headers['Location'])
    assert response_view.status_code == 200
    assert new_author_name.encode('utf-8') in response_view.data
    
    # 6. Vérification finale de la base de données et nettoyage
    with testapp.app_context():
        auteur_cree = Auteur.query.get(new_id)
        assert auteur_cree is not None
        assert auteur_cree.Nom == new_author_name
        
        # Nettoyage (supprimer l'auteur créé pour ne pas perturber les autres tests)
        db.session.delete(auteur_cree)
        db.session.commit()

# --- TEST DE LA ROUTE POST /auteur/erase/ (SUPPRESSION) ---

def test_auteur_erase_after_login_success(client, testapp):
    """
    Teste la suppression d'un auteur via POST /auteur/erase/ après connexion.
    Doit supprimer l'auteur et rediriger vers la liste des auteurs.
    """
    # 1. Préparation : Créer un auteur temporaire à supprimer
    with testapp.app_context():
        auteur_a_supprimer = Auteur(Nom="Auteur à effacer")
        db.session.add(auteur_a_supprimer)
        db.session.commit()
        idA_delete = auteur_a_supprimer.idA
        
    # 2. Vérifier qu'il est bien présent avant l'effacement
    with testapp.app_context():
        assert Auteur.query.get(idA_delete) is not None
        
    # 3. Simuler connexion de l'utilisateur
    # On se connecte vers une page quelconque pour établir la session
    login(client, "CDAL", "AIGRE", "/") 
    
    # 4. Simuler la soumission du formulaire de suppression (méthode POST)
    response = client.post(
        '/auteur/erase/', 
        data={'idA': idA_delete}, # Le formulaire soumet l'identifiant de l'auteur
        follow_redirects=True # Suivre la redirection vers la liste des auteurs (/auteurs/)
    )
    
    # 5. Vérification post-suppression
    assert response.status_code == 200
    # Vérifier que l'on a bien été redirigé vers la liste des auteurs
    assert '/auteurs/' in response.request.path 
    
    # 6. Vérification finale de la base de données
    with testapp.app_context():
        assert Auteur.query.get(idA_delete) is None

