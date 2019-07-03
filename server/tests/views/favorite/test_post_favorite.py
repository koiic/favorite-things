from flask import json

from api.utilities.messages.serialization import serialization_messages
from api.utilities.messages.success import success_messages
from config import AppConfig
from server.tests.mocks.favorite import VALID_FAVORITE_DETAIL

BASE_URL = AppConfig.API_BASE_URL
FAVORITE_URL = f'{BASE_URL}/favorites'


class TestPostFavoriteEndpoint():
    """ Tests endpoint for creating a new favorite things """

    def test_favorite_created_with_valid_details_success(self, init_db, client, user_auth_header, new_category):
        """
            Should return a 201 status code with new category data
            :param init_db: fixture to initialize the db
            :param client: fixture to get flask test client
            :param user_auth_header: fixture to add header data to request
            :return: assertions
        """

        new_category.save()
        VALID_FAVORITE_DETAIL['categoryId'] = new_category.id
        VALID_FAVORITE_DETAIL['user_id'] = user_auth_header.get('user').id
        response = client.post(
            FAVORITE_URL, data=json.dumps(VALID_FAVORITE_DETAIL),
            headers=user_auth_header
        )
        response_json = json.loads(response.data.decode('utf-8'))
        favorite = response_json['data']
        assert response.status_code == 201
        assert response_json['message'] == success_messages[
            'created'].format('Favorite')
        assert favorite['rank'] == VALID_FAVORITE_DETAIL['rank']
        assert 'id' in favorite
        assert 'description' in favorite
        assert 'title' in favorite
        assert type(favorite['id']) == int

    def test_favorite_with_already_existing_title_fails(self, init_db, client, new_category, user_auth_header):
        """
            Should return a 400 status code with if an title already exist in the database
            :param init_db: fixture to initialize the db
            :param client: fixture to get flask test client
            :param request_header: fixture to add header data to request
            :return: assertions
        """
        new_category.save()
        existing_favorite = VALID_FAVORITE_DETAIL.copy()
        existing_favorite['category_id'] = new_category.id
        existing_favorite['user_id'] = user_auth_header.get('user').id
        response = client.post(
            FAVORITE_URL, data=json.dumps(existing_favorite),
            headers=user_auth_header
        )
        response_json = json.loads(response.data.decode('utf-8'))
        assert response.status_code == 409
        assert response_json['message'] == serialization_messages['exists'].format('Favorite with title')
        assert response_json['status'] == 'error'

