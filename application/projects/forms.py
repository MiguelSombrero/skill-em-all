from flask_wtf import FlaskForm
from wtforms import StringField, DateField, validators

class ProjectForm(FlaskForm):
    name = StringField("Project name",
        [validators.Length(min=2, max=50, message="Project name must be between 2-50 characters")]
    )
    
    start_date = DateField("Start date")
    end_date = DateField("End date")

    class Meta:
        csrf = False