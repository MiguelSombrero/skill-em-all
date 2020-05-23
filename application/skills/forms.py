from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, validators

class SkillForm(FlaskForm):
    name = StringField("Name of the skill",
        [validators.Length(min=1, max=50, message="Skill name must be between 2-50 characters")]
    )

    work_experience_years = IntegerField("Work experience years",
        [validators.NumberRange(min=0, max=50, message="experience years should be between 0-50 months")]
    )

    work_experience_months = IntegerField("Work experience months",
        [validators.NumberRange(min=0, max=1000, message="experience months should be between 0-1000 months")]
    )

    other_experience_years = IntegerField("Other experience years",
        [validators.NumberRange(min=0, max=50, message="experience years should be between 0-50 months")]
    )

    other_experience_months = IntegerField("Other experience months",
        [validators.NumberRange(min=0, max=1000, message="experience months should be between 0-1000 months")]
    )

    class Meta:
        csrf = False