from .base_schema import BaseSchema
from marshmallow import fields, validates, ValidationError
from marshmallow.validate import Length
import re


class UserSchema(BaseSchema):
    name = fields.String(required=True, validate=Length(max=60))
    email = fields.String(required=True, validate=Length(max=60))
    password = fields.String(required=True)

    @validates(email)
    def validate_email(self, value):
        valid_email = re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", value)
        if not valid_email:
            return ValidationError('The email is invalid', fields=['email'])
