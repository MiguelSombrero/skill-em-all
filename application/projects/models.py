from application import db
from application.models import account_project, Base

class Project(Base):
    name = db.Column(db.String(64), nullable=False)
    start_date = db.Column(db.DateTime)
    end_date = db.Column(db.DateTime)

    owner_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)

    staff = db.relationship('Account', secondary=account_project, lazy='subquery',
        backref=db.backref('projects', lazy=False))

    def __init__(self, name, start_date, end_date, owner_id):
        self.name = name
        self.start_date = start_date
        self.end_date = end_date
        self.owner_id = owner_id
    