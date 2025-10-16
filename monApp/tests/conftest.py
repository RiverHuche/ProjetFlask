import pytest
from monApp import app, db
from monApp.models import Auteur, Livre, User
from hashlib import sha256


@pytest.fixture
def testapp():
    app.config.update({
        "TESTING": True,
        "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:",
        "WTF_CSRF_ENABLED": False
    })
    
    with app.app_context():
        db.create_all()

        # Ajouter un auteur de test
        auteur = Auteur(Nom="Victor Hugo")
        db.session.add(auteur)
        db.session.commit()

        livre = Livre(Prix=15.5, Titre="Les Misérables", Url = "https://example.com", Img = "lesmis.jpg", auteur_id=auteur.idA)
        db.session.add(livre)
        db.session.commit()

        m=sha256()
        m.update("AIGRE".encode())
        user = User(Login="CDAL", Password=m.hexdigest())
        db.session.add(user)

        db.session.commit()

    yield app
    
    # Cleanup après les tests
    with app.app_context():
        db.drop_all()


@pytest.fixture
def client(testapp):
    return testapp.test_client()
