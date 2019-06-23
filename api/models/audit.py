from .base import BaseModel
from .database import db

class Audit(BaseModel):
    """
    Model For Favorite
    """
    __tablename__ = 'audits'

    action = db.Column(db.String(60), nullable=False)
    description = db.Column(db.String(200), nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def get_child_relationship(self):
        """
        Method to get all child relationships a model has. Override in the
        subclass if the model has child models.
        """
        return None

    def __repr__(self):
        return '<Audit {}>'.format(self.action)

    @staticmethod
    def get_user_audits(user_id):

        audits = Audit.query.filter_by(user_id=user_id).all()
        return audits

    @staticmethod
    def get_single_audits(user_id, audit_id):
        audits = Audit.query.filter_by(id=audit_id, user_id=user_id).first()
        return audits
