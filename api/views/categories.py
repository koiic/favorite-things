from flask_restplus import Resource

from main import api,db

@api.route('/categories')
class CategoryResource(Resource):
    pass