from flask_restplus import Resource

from main import api,db

@api.route('/audits')
class AuditResource(Resource):
    pass