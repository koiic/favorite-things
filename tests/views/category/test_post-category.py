from flask import json

from api.utilities.messages.serialization import serialization_messages
from api.utilities.messages.success import success_messages
from config import AppConfig
from tests.mocks.category import VALID_CATEGORY_TYPE

BASE_URL = AppConfig.API_BASE_URL
CATEGORY_URL = f'{BASE_URL}/categories'


class TestPostCategoryEndpoint():
    """ Tests endpoint for creating a new user """

    def test_category_created_with_valid_details_success(self, init_db, client):
        """
            Should return a 201 status code with new category data
            :param init_db: fixture to initialize the db
            :param client: fixture to get flask test client
            :param request_header: fixture to add header data to request
            :return: assertions
        """
        response = client.post(
            CATEGORY_URL, data=json.dumps(VALID_CATEGORY_TYPE),
            headers={'Content-Type': 'application/json', 'Accept': 'application/json'}
        )
        response_json = json.loads(response.data.decode('utf-8'))
        category = response_json['data']
        assert response.status_code == 201
        assert response_json['message'] == success_messages[
            'created'].format('Category')
        assert category['type'] == VALID_CATEGORY_TYPE['type']
        assert 'id' in category
        assert type(category['id']) == int

    def test_user_with_already_existing_email_fails(self, init_db, client, new_category):
        """
            Should return a 400 status code with if an email already exist in the database
            :param init_db: fixture to initialize the db
            :param client: fixture to get flask test client
            :param request_header: fixture to add header data to request
            :return: assertions
        """
        new_category.save()
        existing_category = VALID_CATEGORY_TYPE.copy()
        existing_category['type'] = new_category.type
        response = client.post(
            CATEGORY_URL, data=json.dumps(existing_category),
            headers={'Content-Type': 'application/json', 'Accept': 'application/json'}
        )
        response_json = json.loads(response.data.decode('utf-8'))
        assert response.status_code == 409
        assert response_json['message'] == serialization_messages['exists'].format('Category')
        assert response_json['status'] == 'error'

    def test_create_category_with_invalid_typefails(
            self, init_db, client):
        """
        Should return a 400 error code with an error message if the
         category is created with invalid type
        :param init_db: fixture to initialize the db
        :param request_header: fixture for invalid request header
        :param client: fixture to get a flask client
        :return: assertions
        """
        invalid_type = VALID_CATEGORY_TYPE.copy()
        invalid_type['type'] = '!@#$%^&*()...'
        response = client.post(
            CATEGORY_URL, data=json.dumps(invalid_type),
            headers={'Content-Type': 'application/json', 'Accept': 'application/json'}
        )
        response_json = json.loads(response.data.decode('utf-8'))
        assert response.status_code == 400
        assert response_json['errors']['type'][0] == \
               serialization_messages['string_characters']

    def test_create_user_with_empty_name_fails(
            self, init_db, client):
        """
        Should return a 400 error code with an error message if the
        category  is created with an empty type
        :param init_db: fixture to initialize the db
        :param request_header: fixture for invalid request header
        :param client: fixture to get a flask client
        :return: assertions
        """
        empty_field = VALID_CATEGORY_TYPE.copy()
        empty_field['type'] = ''
        response = client.post(
            CATEGORY_URL, data=json.dumps(empty_field),
            headers={'Content-Type': 'application/json', 'Accept': 'application/json'}
        )
        response_json = json.loads(response.data.decode('utf-8'))
        assert response.status_code == 400
        assert response_json['errors']['type'][0] == \
               serialization_messages['not_empty']

    def test_create_user_with_name_greater_than_60_characters_fails(
            self, init_db, client):
        """
        Should return a 400 error code with an error message if the
        category creates with a type with length higher than 60 characters
        :param init_db: fixture to initialize the db
        :param client: fixture to get a flask client
        :return: assertions
        """
        lengthy_type = VALID_CATEGORY_TYPE.copy()
        lengthy_type['type'] = 'meme' * 60
        response = client.post(
            CATEGORY_URL, data=json.dumps(lengthy_type),
            headers={'Content-Type': 'application/json', 'Accept': 'application/json'}
        )
        response_json = json.loads(response.data.decode('utf-8'))
        assert response.status_code == 400
        assert response_json['errors']['type'][0] == 'Longer than maximum length 60.'
