from application import db
from application.models import account_skill

class Account(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(64), nullable=False)
    username = db.Column(db.String(64), nullable=False, unique=True)
    passwordhash = db.Column(db.String(64), nullable=False)
    email = db.Column(db.String(64), nullable=True)
    profile_info = db.Column(db.String(500), nullable=True)

    skills = db.relationship('Skill', secondary=account_skill, lazy='subquery',
        backref=db.backref('account', uselist=False, lazy=False))

    def __init__(self, name, username, passwordhash, email):
        self.name = name
        self.username = username
        self.passwordhash = passwordhash
        self.email = email
    
    def get_id(self):
        return self.id

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True