from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, validators, ValidationError

class SkillForm(FlaskForm):
    name = StringField("Name of the skill",
        [validators.Length(min=1, max=50, message="Skill name must be between 2-50 characters"),
        validators.DataRequired()]
    )

    work_experience_years = IntegerField("Work experience years",
        [validators.NumberRange(min=0, max=50, message="experience years should be between 0-50 months"),
        validators.InputRequired()]
    )

    work_experience_months = IntegerField("Work experience months",
        [validators.NumberRange(min=0, max=1000, message="experience months should be between 0-1000 months"),
        validators.InputRequired()]
    )

    other_experience_years = IntegerField("Other experience years",
        [validators.NumberRange(min=0, max=50, message="experience years should be between 0-50 months"),
        validators.InputRequired()]
    )

    other_experience_months = IntegerField("Other experience months",
        [validators.NumberRange(min=0, max=1000, message="experience months should be between 0-1000 months"),
        validators.InputRequired()]
    )

    class Meta:
        csrf = False