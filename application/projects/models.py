from application import db
from application.models import account_project, UserResource, Base
from sqlalchemy.sql import text

class Project(Base, UserResource):
    name = db.Column(db.String(64), nullable=False)
    start_date = db.Column(db.Date)
    end_date = db.Column(db.Date)
    active = db.Column(db.Integer, nullable=False)

    staff = db.relationship('Account', secondary=account_project, lazy='joined')

    def __init__(self, name, start_date, end_date):
        self.name = name
        self.start_date = start_date
        self.end_date = end_date
        self.active = 1
    
    @staticmethod
    def find_projects_by_owner(owner_id):
        statement = text(
            "SELECT a.id, a.name, a.start_date, a.end_date, a.active, a.account_name, b.staff_count"
            " FROM"
            " (SELECT Project.*, Account.name AS account_name"
                " FROM Project"
                " LEFT JOIN Account_project ON Project.id = Account_project.project_id"
                " LEFT JOIN Account ON Account.id = Account_project.account_id"
                " WHERE Project.owner_id = :owner_id"
                " GROUP BY Project.id, Account.name) a"
            " LEFT JOIN"
            " (SELECT project_id AS id, COUNT(*) AS staff_count"
            " FROM Account_project"
            " GROUP BY project_id) b ON a.id = b.id"
        ).params(owner_id=owner_id)

        res = db.engine.execute(statement)
        response = []

        for row in res:
            id = row[0]
            name = row[1]
            start_date = row[2]
            end_date = row[3]
            active = row[4]
            staff_name = row[5]
            staff_count = row[6]

            isInList = False

            for project in response:
                if project["id"] == id:
                    isInList = True

            if isInList:
                last = len(response) - 1

                response[last]["staff"].append({
                    "name": staff_name
                })

            else:
                new = {
                    "id": id,
                    "name": name,
                    "start_date": start_date,
                    "end_date": end_date,
                    "active": active,
                    "staff_count": staff_count,
                    "staff": []
                }

                if staff_name:
                    new["staff"].append({
                        "name": staff_name
                    })

                response.append(new)

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