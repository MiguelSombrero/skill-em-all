from application import app, db
from flask import render_template, request, redirect, url_for
from application.accounts.models import Account
from application.accounts.forms import AccountForm

@app.route("/accounts/new")
def accounts_form():
    return render_template("accounts/account_form.html",
        form = AccountForm()
    )

@app.route("/accounts/<account_id>", methods=["GET"])
def account_profile(account_id):
    return render_template("accounts/account_profile.html",
        account = Account.query.get(account_id)
    )

@app.route("/accounts", methods=["GET"])
def accounts_get():
    return render_template("accounts/accounts.html",
        accounts = Account.query.all()
    )

@app.route("/accounts", methods=["POST"])
def accounts_create():
    form = AccountForm(request.form)

    if not form.validate():
        return render_template("accounts/account_form.html", form = form)

    account = Account(
        form.name.data,
        form.username.data,
        form.password.data,
        form.email.data
    )

    db.session.add(account)
    db.session.commit()

    return redirect(url_for("accounts_get"))
