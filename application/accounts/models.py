from application import db

class Account(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(64), nullable=False)
    username = db.Column(db.String(64), nullable=False, unique=True)
    passwordhash = db.Column(db.String(64), nullable=False)
    email = db.Column(db.String(64), nullable=True)
    profile_info = db.Column(db.String(500), nullable=True)

    def __init__(self, name, username, passwordhash, email):
        self.name = name
        self.username = username
        self.passwordhash = passwordhash
        self.email = email