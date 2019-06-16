from datetime import datetime

from flask import request

from api.models.database import db


class ModelOperations(object):
    """Mixin class with generic model operations."""

    def save(self):
        """
        Save a Model Instance
        :return:
        """
        if request and request.decoded_token:
            self.user_id = request.decoded_token.get('UserInfo').get('id')
        db.session.add(self)
        db.session.commit()
        return self

    def update_(self, **kwargs):
        """
        update entries
        """
        for field, value in kwargs.items():
            setattr(self, field, value)
        if request and request.decoded_token:
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

