from flask_wtf import FlaskForm
from wtforms import StringField, validators

class SkillForm(FlaskForm):
    name = StringField("Name of the skill",
        [validators.Length(min=2, max=50, message="Skill name must be between 2-50 characters")]
    )

    class Meta:
        csrf = False