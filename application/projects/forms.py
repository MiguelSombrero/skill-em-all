from flask_wtf import FlaskForm
from wtforms import StringField, DateField, validators

class ProjectForm(FlaskForm):
    name = StringField("Project name",
        [validators.Length(min=2, max=50, message="Project name must be between 2-50 characters")]
    )
    
    start_date = DateField("Start date", format='%d-%m-%Y')
    end_date = DateField("Start date", format='%d-%m-%Y')

    class Meta:
        csrf = False