from flask import json

from api.utilities.messages.serialization import serialization_messages
from api.utilities.messages.success import success_messages
from config import AppConfig
from tests.mocks.user import VALID_USER_DATA, INVALID_USER_DATA

BASE_URL = AppConfig.API_BASE_URL
AUTH_URL = f'{BASE_URL}/auth/register'


class TestUserRegistartionEndpoint():
    """ Tests endpoint for creating a new user """

    def test_user_created_with_valid_data_success(self, init_db, client):
        """
            Should return a 201 status code with new user data and
            token when data provided in request is valid
            :param init_db: fixture to initialize the db
            :param client: fixture to get flask test client
            :param request_header: fixture to add header data to request
            :return: assertions
        """
        response = client.post(
            AUTH_URL, data=json.dumps(VALID_USER_DATA),
            headers={'Content-Type': 'application/json', 'Accept': 'application/json'}
        )
        response_json = json.loads(response.data.decode('utf-8'))
        user = response_json['data']['user']
        assert response.status_code == 201
        assert response_json['message'] == success_messages[
            'created'].format('User')
        assert user['name'] == VALID_USER_DATA['name']
        assert user['email'] == VALID_USER_DATA['email']
        assert 'id' in user
        assert 'password' not in user
        assert type(user['id']) == int
        assert 'token' in response_json['data']
        assert type(response_json['data']['token']) == str

    def test_user_created_with_invalid_email_fails(self, init_db, client):
        """
            Should return a 400 if email is invalid
            :param init_db: fixture to initialize the db
            :param client: fixture to get flask test client
            :param request_header: fixture to add header data to request
            :return: assertions
        """
        response = client.post(
            AUTH_URL, data=json.dumps(INVALID_USER_DATA),
            headers={'Content-Type': 'application/json', 'Accept': 'application/json'}
        )
        response_json = json.loads(response.data.decode('utf-8'))
        error = response_json['errors']
        assert response.status_code == 400
        assert response_json['message'] == 'An error occurred'
        assert error['email'][0] == serialization_messages['invalid_email']
        assert response_json['status'] == 'error'

    def test_user_created_with_no_email_field_fails(self, init_db, client):
        """
            Should return a 400 status code with if an email field is not available in the user data
            :param init_db: fixture to initialize the db
            :param client: fixture to get flask test client
            :param request_header: fixture to add header data to request
            :return: assertions
        """
        NO_EMAIL_FIELD = INVALID_USER_DATA.copy()
        del (NO_EMAIL_FIELD['email'])
        response = client.post(
            AUTH_URL, data=json.dumps(NO_EMAIL_FIELD),
            headers={'Content-Type': 'application/json', 'Accept': 'application/json'}
        )
        response_json = json.loads(response.data.decode('utf-8'))
        assert response.status_code == 400
        assert response_json['message'] == 'email is required'
        assert response_json['status'] == 'error'

    def test_user_with_already_existing_email_fails(self, init_db, client, new_user):
        """
            Should return a 400 status code with if an email already exist in the database
            :param init_db: fixture to initialize the db
            :param client: fixture to get flask test client
            :param request_header: fixture to add header data to request
            :return: assertions
        """
        new_user.save()
        existing_user = INVALID_USER_DATA.copy()
        existing_user['email'] = new_user.email
        response = client.post(
            AUTH_URL, data=json.dumps(existing_user),
            headers={'Content-Type': 'application/json', 'Accept': 'application/json'}
        )
        response_json = json.loads(response.data.decode('utf-8'))
        assert response.status_code == 409
        assert response_json['message'] == serialization_messages['exists'].format('User')
        assert response_json['status'] == 'error'

    def test_create_user_with_invalid_name_fails(
            self, init_db, client):
        """
        Should return a 400 error code with an error message if the
        user creates with an invalid name
        :param init_db: fixture to initialize the db
        :param request_header: fixture for invalid request header
        :param client: fixture to get a flask client
        :return: assertions
        """
        invalid_name = INVALID_USER_DATA.copy()
        invalid_name['name'] = '!@#$%^&*()...'
        invalid_name['email'] = 'validemail@gmail.com'
        response = client.post(
            AUTH_URL, data=json.dumps(invalid_name),
            headers={'Content-Type': 'application/json', 'Accept': 'application/json'}
        )
        response_json = json.loads(response.data.decode('utf-8'))
        assert response.status_code == 400
        assert response_json['errors']['name'][0] == \
            serialization_messages['string_characters']

    def test_create_user_with_empty_name_fails(
            self, init_db, client):
        """
        Should return a 400 error code with an error message if the
        user creates with an empty name
        :param init_db: fixture to initialize the db
        :param request_header: fixture for invalid request header
        :param client: fixture to get a flask client
        :return: assertions
        """
        invalid_name = INVALID_USER_DATA.copy()
        invalid_name['name'] = ''
        invalid_name['email'] = 'validemail@gmail.com'
        response = client.post(
            AUTH_URL, data=json.dumps(invalid_name),
            headers={'Content-Type': 'application/json', 'Accept': 'application/json'}
        )
        response_json = json.loads(response.data.decode('utf-8'))
        assert response.status_code == 400
        assert response_json['errors']['name'][0] == \
               serialization_messages['not_empty']

    def test_create_user_with_name_greater_than_60_characters_fails(
            self, init_db, client):
        """
        Should return a 400 error code with an error message if the
        user creates with an name higher than 60 characters
        :param init_db: fixture to initialize the db
        :param request_header: fixture for invalid request header
        :param client: fixture to get a flask client
        :return: assertions
        """
        invalid_name = INVALID_USER_DATA.copy()
        invalid_name['name'] = 'meme' * 60
        invalid_name['email'] = 'validemail@gmail.com'
        response = client.post(
            AUTH_URL, data=json.dumps(invalid_name),
            headers={'Content-Type': 'application/json', 'Accept': 'application/json'}
        )
        response_json = json.loads(response.data.decode('utf-8'))
        assert response.status_code == 400
        assert response_json['errors']['name'][0] == 'Longer than maximum length 60.'
