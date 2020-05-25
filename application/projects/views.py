from application import app, db, login_manager
from flask import render_template, request, redirect, url_for
from application.projects.models import Project
from application.accounts.models import Account
from application.projects.forms import ProjectForm
from flask_login import login_required, current_user

@app.route("/projects/new")
@login_required
def projects_form():
    return render_template("projects/project_form.html",
        form = ProjectForm()
    )

@app.route("/projects/", methods=["GET"])
@login_required
def projects_my():
    return render_template("projects/projects.html",
        projects = Project.find_projects_by_owner(current_user.id)
    )

@app.route("/projects/<project_id>", methods=["GET"])
@login_required
def projects_manage(project_id):
    return render_template("projects/project.html",
        project = Project.query.get(project_id)
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
        form.end_date.data
    )

    project.owner_id = current_user.id
    db.session.add(project)
    db.session.commit()

    return redirect(url_for("projects_my"))

@app.route("/projects/<project_id>/accounts/<account_id>", methods=["POST"])
@login_required
def projects_add_staff(project_id, account_id):
    project = Project.query.get(project_id)

    if not project.is_owned_by(account_id):
        return login_manager.unauthorized()

    account = Account.query.get(account_id)
    project.staff.append(account)
    db.session.commit()

    return redirect(url_for("projects_manage", project_id=project_id))
