from flask import request
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restplus import Resource

from api.middlewares.base_validator import ValidationError
from api.models import Favorite, Category, Audit
from api.schemas.favorite_schema import FavoriteSchema
from api.utilities.helpers.response import response
from api.utilities.messages.audit import audit_messages
from api.utilities.messages.serialization import serialization_messages
from api.utilities.messages.success import success_messages
from main import flask_api,db


@flask_api.route('/favorites')
class FavoriteResource(Resource):
    """ Resources for favorite thing creation """

    @jwt_required
    def post(self):
        data = request.get_json()
        schema = FavoriteSchema()
        title = data.get('title')
        category_id = data.get('categoryId')
        Category.get(category_id)
        user = get_jwt_identity()
        query_dict = {'user_id': user.get('id'), 'category_id': category_id, 'rank': int(data.get('rank'))}
        rank = Favorite.get_last_favorite_in_category(**query_dict)
        data['rank'] = int(rank)
        favorite_data = schema.load_object_into_schema(data)
        favorite_exist = Favorite.find_by_title_and_user(title=title, user_id=user.get('id'))
        if favorite_exist:
            raise ValidationError({
                "message": serialization_messages['exists'].format('Favorite with title')
            }, 409)
        Favorite.reorder_favorite_things_on_create(**query_dict)
        favorite_data['user_id'] = user.get('id')
        favorite = Favorite(**favorite_data)
        favorite.save()
        audit = Audit(**{'action':'Create', 'description': audit_messages['created'].format('Favorite', favorite.rank), 'user_id': user.get('id')})
        audit.save()

        return response('success', message=success_messages['created'].format('Favorite'), data=schema.dump(favorite).data, status_code=201)

    @jwt_required
    def get(self):
        """
        Get all favorite thing by a user
        :param favorite_id:
        :return: Favorite thing object
        """
        user = get_jwt_identity()
        print('******', user)
        schema = FavoriteSchema(many=True)
        favorite_thing = Favorite.get_all_favorite(user.get('id'))
        if favorite_thing is None:
            raise ValidationError({'message': 'Favorite thing is empty'})
        favorites = schema.dump(favorite_thing).data
        return response('success', success_messages['retrieved'].format('Favorites'), favorites)


@flask_api.route('/favorites/<int:favorite_id>')
class SingleFavoriteResource(Resource):
    """ Resource for singl,e Favorite things"""

    @jwt_required
    def patch(self, favorite_id):
        """ Endpoint to update favorite things"""
        # import pdb; pdb.set_trace()
        request_data = request.get_json()
        user = get_jwt_identity()
        favorite = Favorite.get(favorite_id)

        if user.get('id') != favorite.user_id:
            raise ValidationError({'message': 'Unauthorized user, you cannot perform this operation'})
        rank = int(request_data.get('rank'))
        query_dict = {'user_id': user.get('id'), 'category_id': favorite.category_id, 'rank': rank, 'id': favorite_id, 'favorite_things': favorite}
        rank = Favorite.get_last_favorite_in_category(**query_dict)
        request_data['rank'] = rank
        Favorite.reorder_favorite_things_on_update(**query_dict)
        schema = FavoriteSchema(context={'id': favorite_id})
        data = schema.load_object_into_schema(request_data, partial=True)
        favorite.update_(**data)
        audit = Audit(**{'action': 'Update', 'description': audit_messages['updated'].format('Favorite', favorite.rank),
                         'user_id': user.get('id')})
        audit.save()
        return response('success', message=success_messages['updated'].format('Favorite'), data=schema.dump(favorite).data, status_code=200)

    @jwt_required
    def get(self, favorite_id):
        """
        Get a single favorite thing
        :param favorite_id:
        :return: Favorite thing object
        """
        user = get_jwt_identity()

        schema = FavoriteSchema()
        favorite_thing = Favorite.find_by_id_and_user(favorite_id, user.get('id'))
        if favorite_thing is None:
            raise ValidationError({'message': 'Favorite thing not found'})
        favorite = schema.dump(favorite_thing).data
        return response('success', success_messages['retrieved'].format('Favorite'), favorite)

    @jwt_required
    def delete(self, favorite_id):
        """
        Delete a single category
        :param favorite_id:
        :return:
        """
        user = get_jwt_identity()
        favorite_exist = Favorite.find_by_id_and_user(favorite_id, user.get('id'))
        if favorite_exist is None:
            raise ValidationError({'message': 'Favorite thing not found'})

        query_dict = {'user_id': user.get('id'), 'category_id': favorite_exist.category_id, 'rank': favorite_exist.rank, 'id': favorite_id, 'favorite_things': favorite_exist }
        Favorite.reorder_deleted_favorite_things(**query_dict)
        Favorite.delete_favorite_thing(favorite_id)
        return {
            'status':  'success',
            'message': 'Favorite deleted successfully'
        }


@flask_api.route('/category/favorites')
class getFavoriteByCatgeory(Resource):

    @jwt_required
    def get(self):
        """

        :param category_id:
        :return: Favorite List
        """
        #
        schema = FavoriteSchema(many=True)
        #
        # user = get_jwt_identity()
        #
        # category_exist = Category.get(category_id)
        # query_dict = {'category_id': category_exist.id, 'user_id': user.get('id')}
        # favorites = Favorite.get_by_category(**query_dict)
        # category_favorite = schema.dump(favorites).data
        # return response('success', success_messages['retrieved'].format('Favorite'), category_favorite)

        user = get_jwt_identity()
        all_category = []
        categories = Category.get_all_categories()
        for category in categories:
            favorites = Favorite.query.filter(Favorite.user_id==user.get('id'), Favorite.category_id==category.id, Favorite.deleted==False).order_by(Favorite.rank.asc()).all()
            if not len(favorites):
                continue
            category_response = dict(category_id= category.id, type=category.type, favorite_things=schema.dump(favorites).data)
            all_category.append(category_response)

        return response('success', success_messages['retrieved'].format('Favorite'), all_category)







