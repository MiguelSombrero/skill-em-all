from application import db
from application.models import Base, UserResource

class Skill(Base, UserResource):
    name = db.Column(db.String(64), nullable=False)
    
    experiences = db.relationship('Experience', lazy=False, cascade="all, delete-orphan",
        backref=db.backref('skill', uselist=False, lazy=True))

    def __init__(self, name):
        self.name = name
        

class Experience(Base):
    skill_id = db.Column(db.Integer, db.ForeignKey('skill.id'), nullable=False)
    experience_type = db.Column(db.String(64), nullable=False)
    experience = db.Column(db.Integer, nullable=False)

    def __init__(self, experience_type, experience):
        self.experience_type = experience_type
        self.experience = experience