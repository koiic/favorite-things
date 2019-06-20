from flask import request
from flask_restplus import Resource

from api.middlewares.base_validator import ValidationError
from api.models import Category
from api.schemas.category_schema import CategorySchema
from api.utilities.helpers.response import response
from api.utilities.messages.serialization import serialization_messages
from api.utilities.messages.success import success_messages
from main import api,db

@api.route('/categories')
class CategoryResource(Resource):

    def post(self):
        data = request.get_json()
        schema = CategorySchema()
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
