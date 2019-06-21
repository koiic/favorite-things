from flask_jwt_extended import create_access_token


def generate_token(user_info):
    return create_access_token(identity=dict(
        id=user_info.id,
        email=user_info.email,
        name=user_info.name
    ))