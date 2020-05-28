from application import db
from application.models import Base, UserResource
from sqlalchemy.sql import text

class Skill(Base, UserResource):
    name = db.Column(db.String(64), nullable=False)
    
    experiences = db.relationship('Experience',
        lazy=False, cascade="all, delete-orphan", order_by="desc(Experience.experience)",
        backref=db.backref('skill', uselist=False, lazy=True))

    def __init__(self, name):
        self.name = name
        
    @staticmethod
    def find_skills_by_project(project_id):
        statement = text(
            "SELECT Skill.name, SUM(Experience.experience)"
            " FROM Account_project"
            " LEFT JOIN Account ON Account.id = Account_project.account_id"
            " LEFT JOIN Skill ON Skill.owner_id = Account.id"
            " LEFT JOIN Experience ON Experience.skill_id = Skill.id"
            " WHERE Account_project.project_id = :project_id"
            " GROUP BY Skill.name"
        ).params(project_id=project_id)

        res = db.engine.execute(statement)

        response = []
        for row in res:
            response.append({
                "name": row[0],
                "experience": row[1]
            })

        return response


class Experience(Base):
    skill_id = db.Column(db.Integer, db.ForeignKey('skill.id'), nullable=False)
    experience_type = db.Column(db.String(64), nullable=False)
    experience = db.Column(db.Integer, nullable=False)

    def __init__(self, experience_type, experience):
        self.experience_type = experience_type
        self.experience = experience