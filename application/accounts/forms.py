from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField

class AccountForm(FlaskForm):
    name = StringField("Name")
    username = StringField("Username")
    password = PasswordField("Password")
    email = StringField("Email")

    class Meta:
        csrf = False