from marshmallow import Schema, fields

class BaseSchema(Schema):
    """Base marshmallow schema with common attributes."""
    id = fields.Integer(dump_only=True)
    deleted = fields.Boolean(dump_only=True)

    created_at = fields.DateTime(dump_only=True, dump_to='createdAt')
    updated_at = fields.DateTime(dump_only=True, dump_to='updatedAt')

    def load_object_into_schema(self, data, partial=False):
        """Helper function to load python objects into schema"""
        data, errors = self.load(data, partial=partial)

        if errors:
            raise AttributeError(dict(errors=errors, message='An error occurred'), 400)

        return data
