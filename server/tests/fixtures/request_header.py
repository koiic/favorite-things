import pytest
from server.tests.generate_test_token import generate_test_token
@pytest.fixture(scope='module')
def request_header():
    return {
        'Content-Type': 'Application/Json',
        'Accept': 'Application/Json'
    }


@pytest.fixture(scope='module')
def user_auth_header(new_user):
    user = new_user.save()
    return {
        'Authorization': f'Bearer {generate_test_token(user)}',
        'user': user,
        'Content-Type': 'Application/Json',
        'Accept': 'Application/Json'
    }