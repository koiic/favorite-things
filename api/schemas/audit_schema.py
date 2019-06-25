from marshmallow import fields

from .user_schema import UserSchema
from .base_schema import BaseSchema
from marshmallow.validate import Length, Range


class AuditSchema(BaseSchema):
    action = fields.String(required=True, validate=Length(max=60), load_from='action', dump_to='action')
    description = fields.String(validate=Range(min=10), load_from='description', dump_to='description')
    users = fields.Nested(
        UserSchema,
        only=['email', 'name'],
        dump_to='user')
