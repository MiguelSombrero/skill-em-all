from flask import Flask
app = Flask(__name__)

from flask_sqlalchemy import SQLAlchemy
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///skills.db"
app.config["SQLALCHEMY_ECHO"] = True
db = SQLAlchemy(app)

from sqlalchemy.engine import Engine
from sqlalchemy import event

@event.listens_for(Engine, "connect")
def set_sqlite_pragma(dbapi_connection, connection_record):
    cursor = dbapi_connection.cursor()
    cursor.execute("PRAGMA foreign_keys=ON")
    cursor.close()

from application import views
from application.accounts import models
from application.accounts import views
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

db.create_all()