from flask import json

from api.utilities.messages.success import success_messages
from config import AppConfig

BASE_URL = AppConfig.API_BASE_URL
AUTH_URL = f'{BASE_URL}/auth/login'

class TestUserLoginEndpoint():
    """ Tests endpoint for authenticating a user """

    def tests_user_login_with_valid_details_success(self, init_db, client, new_user):
        """
        Should return 200 status code with user details if user logs in with valid details
        :param init_db: fixture to initialize db
        :param client: fixture to get flask test client
        :param new_user: fixture to create new user
        :return:  assertions
        """
        password = new_user.password
        new_user.save()
        login_data = {
            'email': new_user.email,
            'password': password
        }
        response = client.post(AUTH_URL, data=json.dumps(login_data), headers={'Content-Type': 'application/json', 'Accept': 'application/json'})
        response_json = json.loads(response.data.decode('utf-8'))
        user = response_json['data']['user']

        assert response.status_code == 200
        assert response_json['message'] == success_messages[
            'retrieved'].format('User')
        assert user['name'] == new_user.name
        assert user['email'] == new_user.email
        assert 'password' not in user
        assert 'id' in user
        assert type(user['id']) == int
        assert 'token' in response_json['data']
        assert type(response_json['data']['token']) == str


    def tests_user_login_with_incorrect_password_fails(self, init_db, client, new_user):
        """
        Should return 400 status code and message if incorrect password is provided
        :param init_db: fixture to initialize db
        :param client: fixture to get flask test client
        :param new_user: fixture to create new user
        :return:  assertions
        """
        password = 'fishboy'
        new_user.save()
        login_data = {
            'email': new_user.email,
            'password': password
        }
        response = client.post(AUTH_URL, data=json.dumps(login_data), headers={'Content-Type': 'application/json', 'Accept': 'application/json'})
        response_json = json.loads(response.data.decode('utf-8'))

        assert response.status_code == 400
        assert response_json['message'] == 'Invalid email or Password'

    def tests_user_login_with_incorrect_email_fails(self, init_db, client, new_user):
        """
        Should return 400 status code and message if incorrect email is provided
        :param init_db: fixture to initialize db
        :param client: fixture to get flask test client
        :param new_user: fixture to create new user
        :return:  assertions
        """
        password = new_user.password
        new_user.save()
        login_data = {
            'email': 'incorrect@email.com',
            'password': password
        }
        response = client.post(AUTH_URL, data=json.dumps(login_data),
                               headers={'Content-Type': 'application/json', 'Accept': 'application/json'})
        response_json = json.loads(response.data.decode('utf-8'))

        assert response.status_code == 400
        assert response_json['message'] == 'Invalid email or Password'

