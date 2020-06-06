from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, validators

class LoginForm(FlaskForm):
    username = StringField("Username",
        [validators.Length(min=5, max=20, message="Username must be between 5-50 characters"),
        validators.DataRequired()]
    )
    password = PasswordField("Password",
        [validators.Length(min=5, max=20, message="Password must be between 5-20 characters"),
        validators.DataRequired()]
    )

    class Meta:
        csrf = False