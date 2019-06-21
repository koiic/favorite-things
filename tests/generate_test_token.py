from api.middlewares.base_validator import ValidationError
from api.utilities.helpers.generate_token import generate_token
from api.utilities.messages.serialization import serialization_messages


def generate_test_token(user_data=None):
    if user_data:
        print('+++++<><>', user_data.id)
        return generate_token(user_data)
    raise ValidationError({'message': serialization_messages['not_empty']})