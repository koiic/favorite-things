from marshmallow import fields
from .base_schema import BaseSchema
from marshmallow.validate import Length


class CategorySchema(BaseSchema):
    type = fields.String(required=True, validate=Length(max=60))
