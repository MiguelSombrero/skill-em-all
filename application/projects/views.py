from application import app, db
from flask import render_template, request, redirect, url_for
from application.projects.models import Project
from application.projects.forms import ProjectForm
from flask_login import login_required, current_user

@app.route("/projects/new")
def projects_form():
    return render_template("projects/project_form.html",
        form = ProjectForm()
    )

@app.route("/projects", methods=["POST"])
@login_required
def projects_create():
    form = ProjectForm(request.form)

    if not form.validate():
        return render_template("projects/project_form.html", form = form)

    project = Project(
        form.name.data,
        form.start_date.data,
        form.end_date.data,
        current_user.id
    )

    db.session.add(project)
    db.session.commit()

    return redirect(url_for("index"))
