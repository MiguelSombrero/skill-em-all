from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, validators

class AccountForm(FlaskForm):
    name = StringField("Name",
        [validators.Length(min=2, max=50, message="Name must be between 2-50 characters")]
    )
    username = StringField("Username",
        [validators.Length(min=5, max=20, message="Username must be between 5-50 characters")]
    )
    password = PasswordField("Password",
        [validators.Length(min=5, max=20, message="Password must be between 5-20 characters")]
    )

    email = StringField("Email")

    class Meta:
        csrf = False