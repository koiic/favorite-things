from api.utilities.validators.string_length_validator import empty_string_validator
from .base_schema import BaseSchema
from marshmallow import fields, validates, ValidationError
from marshmallow.validate import Length
from ..utilities.validators.name_validator import validate_name
import re


class UserSchema(BaseSchema):
    id = fields.Integer(dump_only=True)
    name = fields.String(required=True, validate=Length(max=60), load_from='name', dump_to='name')
    email = fields.Email(required=True, validate=Length(max=60), load_from='email', dump_to='email')
    password = fields.String(required=True, load_from='password', load_only=True)

    @validates('name')
    def name_validator(self, value):
        validate_name(value)
        empty_string_validator(value)