from application import app, db
from flask import render_template, request, redirect, url_for
from application.accounts.models import Account
from application.accounts.forms import AccountForm
from flask_login import login_required

@app.route("/accounts/new")
def accounts_form():
    return render_template("accounts/account_form.html",
        form = AccountForm()
    )

@app.route("/accounts/<account_id>", methods=["GET"])
@login_required
def account_profile(account_id):
    return render_template("accounts/account_profile.html",
        account = Account.query.get(account_id)
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
