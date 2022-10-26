from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired

class AddForm(FlaskForm):
    name = StringField('Model:', validators=[DataRequired()])
    year = IntegerField('Year:', validators=[DataRequired()])
    origin = StringField('Origin:', validators=[DataRequired()])
    mpg = IntegerField('MPG:', validators=[DataRequired()])
    submit = SubmitField('ADD')
    
        
class SearchForm(FlaskForm):
    name = StringField('Model:', validators=[DataRequired()])
    submit = SubmitField('SEARCH ME')
    