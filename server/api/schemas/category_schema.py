from marshmallow import fields, validates

from api.utilities.validators.name_validator import validate_name
from api.utilities.validators.string_length_validator import empty_string_validator
from .base_schema import BaseSchema
from marshmallow.validate import Length


class CategorySchema(BaseSchema):
    type = fields.String(required=True, validate=Length(max=60))

    @validates('type')
    def name_validator(self, value):
        validate_name(value)
        empty_string_validator(value)
