from flask_wtf import FlaskForm
from wtforms import TextField, IntegerField, TextAreaField, SubmitField, RadioField, SelectField
from wtforms import validators, ValidationError

class command(FlaskForm):
    command = TextField('command:')
    submit = SubmitField('Submit')
