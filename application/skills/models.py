from application import db
from application.models import account_skill

class Skill(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(64), nullable=False, unique=True)
    
    def __init__(self, name, account):
        self.name = name
        self.account = account