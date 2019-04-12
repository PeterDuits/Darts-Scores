import json

from marshmallow import Schema, fields


def timestamps():
    return fields.DateTime(), fields.DateTime()


class BaseSchema(Schema):
    class Meta:
        ordered = True
        strict = True


class JsonField(fields.Field):
    def _serialize(self, value, attr, obj):
        try:
            return json.loads(value)
        except (TypeError, json.JSONDecodeError, UnicodeDecodeError) as e:
            return {}


class UserSchema(BaseSchema):
    id = fields.Str(attribute='user_id')
    first_name = fields.Str()
    last_name = fields.Str()
    email = fields.Str()
    created_at, updated_at = timestamps()
