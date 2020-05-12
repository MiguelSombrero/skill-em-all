from application import app, db
from flask import render_template, request, redirect, url_for
from application.accounts.models import Account

@app.route("/accounts/new")
def accounts_form():
    return render_template("accounts/account_form.html")

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
    account = Account(
        request.form.get("name"),
        request.form.get("username"),
        request.form.get("password"),
        request.form.get("email")
    )

    db.session.add(account)
    db.session.commit()

    return redirect(url_for("accounts_get"))
