from flask import json

from api.utilities.messages.serialization import serialization_messages
from api.utilities.messages.success import success_messages
from config import AppConfig
from tests.mocks.favorite import VALID_FAVORITE_DETAIL

BASE_URL = AppConfig.API_BASE_URL
# FAVORITE_URL = f'{BASE_URL}/favorites/<string:favorite_id>'


class TestUpdateFavoriteEndpoint():
    """ Tests endpoint for updating favorite things """

    def test_favorite_updated_with_valid_details_success(self, init_db, client, user_auth_header, new_favorite, new_category):
        """
            Should return a 200 status code with updated favorite data
            :param init_db: fixture to initialize the db
            :param client: fixture to get flask test client
            :param user_auth_header: fixture to add header data to request
            :return: assertions
        """
        # import pdb; pdb.set_trace()
        new_category.save()
        user = user_auth_header.get('user')
        new_favorite.user_id = user.id
        new_favorite.category_id = new_category.id
        new_favorite.save()
        existing_favorite = VALID_FAVORITE_DETAIL.copy()
        existing_favorite['rank'] = 2
        response = client.patch(
            f'{BASE_URL}/favorites/{new_favorite.id}', data=json.dumps(existing_favorite),
            headers=user_auth_header
        )
        response_json = json.loads(response.data.decode('utf-8'))
        favorite = response_json['data']
        assert response.status_code == 200
        assert response_json['message'] == success_messages[
            'updated'].format('Favorite')
        assert favorite['rank'] == 2
        assert 'id' in favorite
        assert type(favorite['id']) == int

