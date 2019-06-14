
from .user_schema import UserSchema
from .category_schema import CategorySchema
from .base_schema import BaseSchema
from marshmallow import fields
from marshmallow.validate import Length, Range


class FavoriteSchema(BaseSchema):
    title = fields.String(required=True, validate=Length(max=60))
    description = fields.String(validate=Range(min=10))
    rank = fields.Integer()
    category_id = fields.Integer(
        load_from="categoryId",
        dump_to="categoryId")
    meta_data = fields.Raw(
        load_from="metaData", dump_to="metaData")
    categories = fields.Nested(
        CategorySchema,
        only=['type'],
        dump_to='category')
    users = fields.Nested(
        UserSchema,
        only=['id', 'name'],
        dump_to='user'
    )
