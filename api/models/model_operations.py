from datetime import datetime

from flask import request

from api.middlewares.base_validator import ValidationError
from api.models.database import db


class ModelOperations(object):
    """Mixin class with generic model operations."""

    def save(self):
        """
        Save a Model Instance
        :return:
        """
        db.session.add(self)
        db.session.commit()
        return self

    def update_(self, **kwargs):
        """
        update entries
        """
        for field, value in kwargs.items():
            setattr(self, field, value)
            self.updated_at = datetime.utcnow()

        db.session.commit()

    @classmethod
    def get(cls, id):
        """
           return entries by id
        """
        return cls.query.filter_by(id=id, deleted=False).first()

    @classmethod
    def get_or_404(cls, id):
        """
           return entries by id
        """
        return cls.query.get_or_404(id).first()

    @classmethod
    def find_by_email(cls, email):
        """
            Find user by email
        """
        if email:
            return cls.query.filter_by(email=email).first()
        return {
           'message': 'email field is required',
            'status': 'Failed'
        }, 400

    def delete(self):
        """
        Deletes a database instance
        :return: None
        """
        db.session.delete(self)
        db.session.commit()
