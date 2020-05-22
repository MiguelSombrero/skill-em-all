from application import db
from application.models import Base

class Account(Base):
    name = db.Column(db.String(64), nullable=False)
    username = db.Column(db.String(64), nullable=False, unique=True)
    password = db.Column(db.String(64), nullable=False)
    email = db.Column(db.String(64), nullable=True)
    profile_info = db.Column(db.String(500), nullable=True)

    skills = db.relationship('Skill', lazy=False,
        backref=db.backref('account', uselist=False, lazy=True))

    def __init__(self, name, username, password, email):
        self.name = name
        self.username = username
        self.password = password
        self.email = email
    
    def get_id(self):
        return self.id

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True