# forms.py

from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, IntegerField, PasswordField, SubmitField
from wtforms.validators import DataRequired 

class RegisterForm(FlaskForm):
    name = StringField('Name:', validators=[DataRequired()])
    email = EmailField('Email:', validators=[DataRequired()])
    age = IntegerField('Age:', validators=[DataRequired()])
    password = PasswordField('Password:', validators=[DataRequired()])
    password_confirmation = PasswordField('Password:', validators=[DataRequired()])
    button = SubmitField('Submit', validators=[DataRequired()])