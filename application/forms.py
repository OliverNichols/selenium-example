from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import Length

class BasicForm(FlaskForm):
    name = StringField('Name',
        validators=[
            Length(min=1, message="The name field can't be empty!"),
            Length(max=30, message="This name is too long!")
        ])
    submit = SubmitField('🗸')