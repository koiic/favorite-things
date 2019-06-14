from .base import BaseModel
from .database import db


class Category(BaseModel):
    """
    Model for CATEGORIES
    """
    __tablename__ = 'categories'

    type = db.Column(db.String(60), nullable=False)
    favorite_things = db.relationship('Favorite', lazy='select', backref=db.backref('categories', lazy='joined'))

    def get_child_relationship(self):
        """
        Method to get all child relationships a model has. Override in the
        subclass if the model has child models.
        """
        return None

    def __repr__(self):
        return '<Category {}>'.format(self.type)
