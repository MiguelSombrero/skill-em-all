from application import db
from sqlalchemy.ext.declarative import declared_attr

account_project = db.Table('account_project',
    db.Column('account_id', db.Integer, db.ForeignKey('account.id', ondelete='cascade'), primary_key=True),
    db.Column('project_id', db.Integer, db.ForeignKey('project.id', ondelete='cascade'), primary_key=True)
)

class Base(db.Model):
    __abstract__ = True
  
    id = db.Column(db.Integer, primary_key=True)
    created = db.Column(db.DateTime, default=db.func.current_timestamp())

class UserResource(db.Model):
    __abstract__ = True
  
    def is_owned_by(self, user_id):
        return int(self.owner_id) == int(user_id)

    @declared_attr
    def owner_id(cls):
        return db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)
    