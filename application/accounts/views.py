from application import app, db
from flask import render_template, request, redirect, url_for
from application.accounts.models import Account
from application.accounts.forms import AccountForm
from flask_login import login_required, current_user

@app.route("/accounts/new")
def accounts_form():
    return render_template("accounts/account_form.html",
        form = AccountForm()
    )

@app.route("/accounts/<account_id>", methods=["GET"])
@login_required
def accounts_profile(account_id):
    account = Account.query.get(account_id)
    form = AccountForm()
    
    return render_template("accounts/account_profile.html",
        form = form,
        account = account    
    )

@app.route("/accounts", methods=["GET"])
@login_required
def accounts_get():
    return render_template("accounts/accounts.html",
        accounts = Account.query.all()
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
        form.password.data,
        form.email.data
    )

    db.session.add(account)
    db.session.commit()

    return redirect(url_for("accounts_get"))

@app.route("/accounts/<account_id>", methods=["POST"])
@login_required
def accounts_update(account_id):
    form = AccountForm(request.form)
    account = Account.query.get(account_id)

    if not form.validate():
        return render_template("accounts/account_profile.html",
            form = form,
            account = account
        )

    if not account:
        return redirect(url_for("index"))

    #form.populate_obj(account)

    print("TULTIIN TÄNNE")
    account.name = form.name.data
    account.passwordhash = form.password.data
    account.email = form.email.data
    account.profile_info = form.profile_info.data

    db.session.commit()

    return redirect(url_for("accounts_profile", account_id=account_id))
