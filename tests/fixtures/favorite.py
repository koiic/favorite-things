import pytest
from api.models.favorite import Favorite

@pytest.fixture(scope='module')
def new_favorite(app, init_db):
    """
        Fixture to create a new favorite things
        :param app: app instance
        :param init_db: fixture to initialize the db
        :return: a new user instance
    """
    favorite_object = {
        'title': 'calory',
        'description': 'ibrahim@gmail.com',
        'metaData': 'password',
        'categoryId': 1
    }

    favorite = Favorite(**favorite_object)
    return favorite
