from application import app, db
from flask import render_template, request, redirect, url_for
from application.accounts.models import Account
from application.auth.forms import LoginForm
from flask_login import login_user, logout_user
from passlib.hash import sha256_crypt

@app.route("/login")
def login_form():
    return render_template("auth/login_form.html",
        form = LoginForm()
    )

@app.route("/login", methods=["POST"])
def login():
    form = LoginForm(request.form)

    if not form.validate():
        return render_template("auth/login_form.html",
            form = form
        )

    account = Account.query.filter_by(username=form.username.data).first()

    if not account or not sha256_crypt.verify(form.password.data, account.password):
        return render_template("auth/login_form.html",
            form = form, error = "Username or password wrong"
        )

    login_user(account)
    return redirect(url_for("index"))

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("index"))