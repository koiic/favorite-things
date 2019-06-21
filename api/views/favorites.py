from flask import request
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restplus import Resource

from api.middlewares.base_validator import ValidationError
from api.models import Favorite
from api.schemas.favorite_schema import FavoriteSchema
from api.utilities.helpers.response import response
from api.utilities.messages.serialization import serialization_messages
from api.utilities.messages.success import success_messages
from main import api,db


@api.route('/favorites')
class FavoriteResource(Resource):
    """ Resources for favorite thing creation """

    @jwt_required
    def post(self):
        data = request.get_json()
        schema = FavoriteSchema()
        title = data.get('title')
        user = get_jwt_identity()
        favorite_data = schema.load_object_into_schema(data)
        favorite_exist = Favorite.find_by_title_and_user(title=title, user_id=user.get('id'))
        if favorite_exist:
            raise ValidationError({
                "message": serialization_messages['exists'].format('Favorite')
            }, 409)
        favorite_data['user_id'] = user.get('id')
        category = Favorite(**favorite_data)
        category.save()

        return response('success', message=success_messages['created'].format('Favorite'), data=schema.dump(category).data, status_code=201)