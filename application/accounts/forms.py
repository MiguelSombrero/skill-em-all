from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, PasswordField, validators

class AccountForm(FlaskForm):
    name = StringField("Name",
        [validators.Length(min=2, max=50, message="Name must be between 2-50 characters"),
        validators.DataRequired()]
    )
    username = StringField("Username",
        [validators.Length(min=5, max=20, message="Username must be between 5-50 characters"),
        validators.DataRequired()]
    )
    password = PasswordField("Password",
        [validators.Length(min=5, max=20, message="Password must be between 5-20 characters"),
        validators.DataRequired()]
    )

    email = StringField("Email",
        [validators.Length(max=50, message="Email must be under 50 characters")]
    )

    profile_info = TextAreaField("Info",
        [validators.Length(max=500, message="Profile info must be under 500 characters")]
    )

    class Meta:
        csrf = False

class AccountProfileForm(FlaskForm):
    name = StringField("Name",
        [validators.Length(min=2, max=50, message="Name must be between 2-50 characters"),
        validators.DataRequired()]
    )
    
    password = PasswordField("Password",
        [validators.Length(max=20, message="Password must be between 5-20 characters")]
    )

    email = StringField("Email",
        [validators.Length(max=50, message="Email must be under 50 characters")]
    )

    profile_info = TextAreaField("Info",
        [validators.Length(max=500, message="Profile info must be under 500 characters")]
    )

    class Meta:
        csrf = False