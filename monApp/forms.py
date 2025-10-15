from flask_wtf import FlaskForm
from wtforms import FloatField, StringField, HiddenField
from wtforms.validators import DataRequired
    
class FormAuteur(FlaskForm):
    idA=HiddenField('idA')
    Nom=StringField ('Nom',validators =[DataRequired()])

class FormLivre(FlaskForm):
    idL=HiddenField('idA')
    Prix=FloatField('Prix',validators =[DataRequired()])