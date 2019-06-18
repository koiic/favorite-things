from flask_restplus import Resource

from main import api,db

@api.route('/favorites')
class FavoriteResource(Resource):
    pass