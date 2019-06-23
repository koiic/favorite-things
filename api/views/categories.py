from flask import request
from flask_restplus import Resource

from api.middlewares.base_validator import ValidationError
from api.models import Category
from api.schemas.category_schema import CategorySchema
from api.utilities.helpers.response import response
from api.utilities.messages.serialization import serialization_messages
from api.utilities.messages.success import success_messages
from main import api,db

schema = CategorySchema()



@api.route('/categories')
class CategoryResource(Resource):

    def post(self):
        data = request.get_json()
        category_type = data.get('type')
        category_data = schema.load_object_into_schema(data)
        category_exist = Category.find_by_type(category_type)
        if category_exist:
            raise ValidationError({
                "message": serialization_messages['exists'].format('Category')
            }, 409)
        category = Category(**category_data)
        category.save()

        return response('success', message=success_messages['created'].format('Category'), data=schema.dump(category).data, status_code=201)

    def get(self):
        """
        Get List of all fovorite things
        """
        categories = Category.get_all_categories()
        data = schema.dump(categories, many=True).data
        return {
            'status': 'success',
            'message': 'Categories fetched successfully',
            'data': data
        }, 200

    @api.route('/favorite/<int:category_id>')
    class SingleCategoryResource(Resource):
        """
        Resource class for single category endpoints
        """

        def get(self, category_id):
            """
            Get a single category thing
            :param category_id:
            :return: Favorite thing object
            """
            category = Category.get_single_category(category_id)
            category_data = schema.dump(category).data
            return {
                'status': 'success',
                'message': 'Categories fetched successfully',
                'data': category_data
            }, 200

        def patch(self, category_id):
            """ Endpoint for updating a favorite thing"""
            thing = Category.get_single_category(category_id)
            request_data = request.get_json()
            schema = CategorySchema(context={'id': category_id})
            data = schema.load_object_into_schema(request_data, partial=True)
            thing.update_(data)

            return {
                'status': 'success',
                'message': 'Favorite things updated successfully',
                'data': schema.dump(thing).data
            }, 200

        def delete(self, favorite_id):
            """ Endpoint to soft delete a favorite thing"""
            Category.delete(favorite_id)
            return {
                'status': 'success',
                'message': 'Categry deleted successfully',
            }, 200

