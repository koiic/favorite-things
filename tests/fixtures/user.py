import pytest
from api.models.user import User

@pytest.fixture(scope='module')
def new_user(app, init_db):
    """
        Fixture to create a new user
        :param app: app instance
        :param init_db: fixture to initialize the db
        :return: a new user instance
    """
    user_object = {
        'name': 'calory',
        'email': 'ibrahim@gmail.com',
        'password': 'password'
    }

    user = User(**user_object)
    return user
