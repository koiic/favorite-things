from api.utilities.validators.name_validator import validate_name
from api.utilities.validators.string_length_validator import min_length_validator
from .user_schema import UserSchema
from .category_schema import CategorySchema
from .base_schema import BaseSchema
from marshmallow import fields, validates
from marshmallow.validate import Length, Range


class FavoriteSchema(BaseSchema):
    title = fields.String(required=True, validate=Length(max=60))
    description = fields.String(dump_to="description", load_from="description")
    rank = fields.Int(load_from="rank", dump_to="rank")
    category_id = fields.Int(
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

    @validates('description')
    def name_validator(self, value):
        min_length_validator(value)
