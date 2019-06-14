from .base import BaseModel
from .database import db

class Favorite(BaseModel):
    """
    Model For Favorite
    """
    __tablename__ = 'favorite_things'

    title = db.Column(db.String(60), nullable=False)
    description = db.Column(db.String(200), nullable=True)
    meta_data = db.Column(db.JSON, nullable=True)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    rank = db.Column(db.Integer)

    def get_child_relationship(self):
        """
        Method to get all child relationships a model has. Override in the
        subclass if the model has child models.
        """
        return None

    def __repr__(self):
        return '<Favorite {}>'.format(self.title)
