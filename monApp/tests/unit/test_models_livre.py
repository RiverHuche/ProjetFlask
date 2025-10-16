from monApp.models import Livre


def test_livre_init(testapp):
    with testapp.app_context():
        livre = Livre.query.first()
        assert livre.Titre == "Les Misérables"
        assert livre.Prix == 15.5


def test_livre_repr(testapp):
    with testapp.app_context():
        livre = Livre.query.first()
        assert repr(livre) == f"<Livre ({livre.idL}) {livre.Titre}>"
