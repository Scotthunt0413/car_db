from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired

class AddForm(FlaskForm)
    carModel = StringField('Model:', validators=[DataRequired()])
    modelYear = IntegerField('Year:', validators=[DataRequired()])
    origin = StringField('Origin:', validators=[DataRequired()])
    mpg = IntegerField('MPG:', validators=[DataRequired()])
    submit = SubmitField('ADD', validators[DataRequired()])