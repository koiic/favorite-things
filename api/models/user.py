from .base import BaseModel
from.database import db

class User(BaseModel):
    """
    Model for User
    """
    __tablename__ = 'users'

    name = db.Column(db.String(60), nullable=False)
    email = db.Column(db.String(60), nullable=False, unique=True)
    password = db.Column(db.String(200), nullable=False)
    favorite_things = db.relationship('Favorite', lazy='select', backref=db.backref('users', lazy='joined'))

    def get_child_relationship(self):
        """
        Method to get all child relationships a model has. Override in the
        subclass if the model has child models.
        """
        return None

    def __repr__(self):
        return '<User {}>'.format(self.name)