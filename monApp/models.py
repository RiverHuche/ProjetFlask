from .app import db

class Auteur(db.Model):
    idA = db.Column(db.Integer,primary_key=True)
    Nom = db.Column(db.String(100))
    
    def __init__(self, Nom):
        self.Nom = Nom

class Livre(db.Model):
    idL = db.Column(db.Integer,primary_key=True)
    Prix = db.Column(db.Float)
    Titre = db.Column(db.String(255))
    Url = db.Column(db.String(255))
    Img = db.Column(db.String(255))
    auteur_id = db.Column(db.Integer,db.ForeignKey("auteur.idA"))
    auteur = db.relationship("Auteur",backref =db.backref("livres",lazy="dynamic"))

    def __init__(self,idL,Prix,Titre,Url,Img,auteur_id,auteur):
        self.idL = idL
        self.Prix = Prix
        self.Titre = Titre
        self.Url = Url
        self.Img = Img
        self.auteur_id = auteur_id
        self.auteur = auteur



