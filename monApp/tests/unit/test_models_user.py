from monApp.models import User, load_user
from hashlib import sha256


def test_user_get_id(testapp):
    with testapp.app_context():
        user = User.query.get("CDAL")
        assert user is not None
        assert user.get_id() == "CDAL"


def test_load_user_function(testapp):
    with testapp.app_context():
        user = load_user("CDAL")
        assert user is not None
        assert user.Login == "CDAL"


def test_password_hashing_consistency(testapp):
    """Vérifie que le mot de passe hashé correspond à la valeur stockée."""
    with testapp.app_context():
        user = User.query.get("CDAL")
        assert user is not None
        m = sha256()
        m.update("AIGRE".encode())
        assert user.Password == m.hexdigest()
        assert repr(user) == f"<User ({user.Login}) {user.Password}>"
