from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, validators

class SkillForm(FlaskForm):
    name = StringField("Name of the skill",
        [validators.Length(min=1, max=50, message="Skill name must be between 2-50 characters")]
    )

    work_experience = IntegerField("Work experience",
        [validators.NumberRange(min=0, max=1000, message="experience should be between 0-1000 months")]
    )

    other_experience = IntegerField("Other experience",
        [validators.NumberRange(min=0, max=1000, message="experience should be between 0-1000 months")]
    )

    class Meta:
        csrf = False