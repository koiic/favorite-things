import pytest
from api.models.category import Category

@pytest.fixture(scope='module')
def new_category(app, init_db):
    """
        Fixture to create a new category
        :param app: app instance
        :param init_db: fixture to initialize the db
        :return: a new user instance
    """
    category_object = {
        'type': 'working',

    }

    category = Category(**category_object)
    return category
