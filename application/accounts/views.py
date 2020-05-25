from application import app, db, login_manager
from flask import render_template, request, redirect, url_for
from application.accounts.models import Account
from application.skills.models import Skill
from application.projects.models import Project
from application.accounts.forms import AccountForm
from flask_login import login_required, current_user
from passlib.hash import sha256_crypt

@app.route("/accounts/new")
def accounts_form():
    return render_template("accounts/account_form.html",
        form = AccountForm()
    )

@app.route("/accounts/<account_id>", methods=["GET"])
@login_required
def accounts_profile(account_id):
    if not __is_owner(account_id):
        return login_manager.unauthorized()

    account = Account.query.get(account_id)
    form = AccountForm(obj=account)
    
    return render_template("accounts/account_profile.html",
        form = form,
        account = account    
    )

@app.route("/accounts", methods=["GET"])
@login_required
def accounts_get():
    skill_name = request.args.get("skill")

    if skill_name:
        accounts = Account.query.join(Account.skills)\
            .filter(Skill.name.like(skill_name))
    else:
        accounts = Account.query.all()

    projects = Project.find_project_names_by_owner(current_user.id)

    return render_template("accounts/accounts.html",
        accounts = accounts, projects = projects
    )

@app.route("/accounts", methods=["POST"])
def accounts_create():
    form = AccountForm(request.form)

    if not form.validate():
        return render_template("accounts/account_form.html", form = form)

    account = Account.query.filter_by(username=form.username.data).first()

    if account:
        return render_template("accounts/account_form.html", form = form, error = "Username is taken, please select another one")

    account = Account(
        form.name.data,
        form.username.data,
        sha256_crypt.encrypt(form.password.data),
        form.email.data
    )

    db.session.add(account)
    db.session.commit()

    return redirect(url_for("accounts_get"))

@app.route("/accounts/<account_id>/update", methods=["POST"])
@login_required
def accounts_update(account_id):
    if not __is_owner(account_id):
        return login_manager.unauthorized()

    form = AccountForm(request.form)
    account = Account.query.get(account_id)

    #add validation here

    if not account:
        return redirect(url_for("index"))

    if form.password.data:
        account.password = sha256_crypt.encrypt(form.password.data)

    account.name = form.name.data
    account.email = form.email.data
    account.profile_info = form.profile_info.data

    db.session.commit()

    return redirect(url_for("accounts_profile", account_id=account_id))

@app.route("/accounts/<account_id>/delete", methods=["POST"])
@login_required
def accounts_delete(account_id):
    if not __is_owner(account_id):
        return login_manager.unauthorized()
        
    account = Account.query.get(account_id)
    db.session.delete(account)
    db.session.commit()

    return redirect(url_for("index"))

def __is_owner(account_id):
    return int(account_id) == current_user.id
