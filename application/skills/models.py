from application import db
from application.models import account_skill, Base

class Skill(Base):
    name = db.Column(db.String(64), nullable=False, unique=True)
    
    def __init__(self, name, account):
        self.name = name
        self.account = account