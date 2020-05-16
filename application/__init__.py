from flask import Flask
app = Flask(__name__)

import os

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

if os.environ.get("HEROKU"):
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
else:
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///skills.db"
    app.config["SQLALCHEMY_ECHO"] = True

    from sqlalchemy.engine import Engine
    from sqlalchemy import event

    @event.listens_for(Engine, "connect")
    def set_sqlite_pragma(dbapi_connection, connection_record):
        cursor = dbapi_connection.cursor()
        cursor.execute("PRAGMA foreign_keys=ON")
        cursor.close()

from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy(app)

from application import models
from application import views
from application.accounts import models
from application.accounts import views
from application.skills import models
from application.skills import views
from application.auth import views

from os import urandom
app.config["SECRET_KEY"] = urandom(32)

from application.accounts.models import Account
from flask_login import LoginManager
login_manager = LoginManager()
login_manager.init_app(app)

login_manager.login_view = "login"
login_manager.login_message = "Login required"

@login_manager.user_loader
def load_user(user_id):
    return Account.query.get(user_id)

try:
    db.create_all()
except:
    pass