from application import db
from application.models import account_project, Base
from sqlalchemy.sql import text

class Project(Base):
    name = db.Column(db.String(64), nullable=False)
    start_date = db.Column(db.DateTime)
    end_date = db.Column(db.DateTime)
    active = db.Column(db.Boolean, nullable=False)

    owner_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)

    staff = db.relationship('Account', secondary=account_project, lazy='joined',
        backref=db.backref('projects', lazy=True))

    def __init__(self, name, start_date, end_date, owner_id):
        self.name = name
        self.start_date = start_date
        self.end_date = end_date
        self.owner_id = owner_id
        self.active = True
    
    @staticmethod
    def find_projects_by_owner(owner_id):
        statement = text(
            "SELECT Account.name, Project.id, Project.name, Project.start_date, Project.end_date"
            " FROM Project"
            " LEFT JOIN Account_project ON Project.id = Account_project.project_id"
            " LEFT JOIN Account ON Account.id = Account_project.account_id"
            " WHERE Project.owner_id = :owner_id"
            " AND Project.active = 1"
            " GROUP BY Project.id, Account.name"
        ).params(owner_id=owner_id)

        res = db.engine.execute(statement)

        response = []
        for row in res:
            response.append(row)

        return response

    @staticmethod
    def find_project_names_by_owner(owner_id):
        statement = text(
            "SELECT Project.id, Project.name"
            " FROM Project"
            " WHERE Project.owner_id = :owner_id"
            " AND Project.active = 1"
        ).params(owner_id=owner_id)

        res = db.engine.execute(statement)

        response = []
        for row in res:
            response.append({
                "id": row[0],
                "name": row[1]
            })

        return response
    