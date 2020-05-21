from application import db
from application.models import account_skill, Base
from sqlalchemy.sql import text

class Account(Base):
    name = db.Column(db.String(64), nullable=False)
    username = db.Column(db.String(64), nullable=False, unique=True)
    password = db.Column(db.String(64), nullable=False)
    email = db.Column(db.String(64), nullable=True)
    profile_info = db.Column(db.String(500), nullable=True)

    skills = db.relationship('Skill', secondary=account_skill, lazy='joined',
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

    @staticmethod
    def user_has_skill(user_id, skill_id):
        statement = text(
            "SELECT *"
            " FROM Account_skill"
            " WHERE Account_skill.account_id = :user_id"
            " AND Account_skill.skill_id = :skill_id"
        ).params(user_id=user_id, skill_id=skill_id)

        res = db.engine.execute(statement)

        if res == []:
            return False

        return True