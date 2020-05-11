from application import app, db
from flask import render_template, request
from application.accounts.models import Account

@app.route("/accounts/new")
def accounts_form():
    return render_template("accounts/account_form.html")

@app.route("/accounts", methods=["POST"])
def accounts_create():
    account = Account(
        request.form.get("name"),
        request.form.get("username"),
        request.form.get("password"),
        request.form.get("email")
    )

    db.session.add(account)
    db.session.commit()

    return "added account"
