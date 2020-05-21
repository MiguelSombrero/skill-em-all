from application import db
from application.models import account_skill, Base

class Skill(Base):
    name = db.Column(db.String(64), nullable=False, unique=True)
    experiences = db.relationship("Experience", backref='skill', lazy=False)

    def __init__(self, name):
        self.name = name
        

class Experience(Base):
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)
    skill_id = db.Column(db.Integer, db.ForeignKey('skill.id'), nullable=False)

    experience_type = db.Column(db.String(64), nullable=False)
    experience = db.Column(db.Integer, nullable=False)
    
    def __init__(self, experience_type, experience):
        self.experience_type = experience_type
        self.experience = experience