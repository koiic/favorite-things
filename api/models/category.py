from api.middlewares.base_validator import ValidationError
from api.utilities.messages.serialization import serialization_messages
from .base import BaseModel
from .database import db


class Category(BaseModel):
    """
    Model for CATEGORIES
    """
    __tablename__ = 'categories'

    type = db.Column(db.String(60), unique=True, nullable=False)
    favorite_things = db.relationship('Favorite', lazy='select', backref=db.backref('categories', lazy='joined'))

    def get_child_relationship(self):
        """
        Method to get all child relationships a model has. Override in the
        subclass if the model has child models.
        """
        return None

    def __repr__(self):
        return '<Category {}>'.format(self.type)

    @staticmethod
    def find_by_type(category_type):
        """
            Find category by type
        """
        if type:
            return Category.query.filter_by(type=category_type).first()
        raise ValidationError({ 'message': serialization_messages['required_field'].format('type')}, 400)
