from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restplus import Resource

from api.models import Audit
from api.schemas.audit_schema import AuditSchema
from api.utilities.helpers.response import response
from api.utilities.messages.success import success_messages
from main import flask_api,db


@flask_api.route('/audits')
class AuditResource(Resource):

    @jwt_required
    def get(self):
        """
        Get List of all Audit for a user
        """
        schema = AuditSchema(many=True)
        user = get_jwt_identity()
        user_id = user.get('id')
        audits = Audit.get_user_audits(user_id)

        data = schema.dump(audits).data
        return response('success', success_messages['retrieved'].format('Audits'), data)

@flask_api.route('/audits/<int:audit_id>')
class SingleAuditResource(Resource):
    """
    Resource class for single category endpoints
    """

    def get(self, audit_id):
        """
        Get a single audit by id
        :param audit_id:
        :return: Audit object
        """
        schema = AuditSchema()

        user = get_jwt_identity()
        user_id = user.get('id')
        audits = Audit.get_single_audit(user_id, audit_id)
        data = schema.dump(audits).data
        return response('success', success_messages['retrieved'], data)


