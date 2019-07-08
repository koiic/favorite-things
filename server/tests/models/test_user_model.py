from api.models import User


class TestUserModel:

    def test_new_user_succeeds(self, init_db, new_user):
        """
           GIVEN a User model
           WHEN a new User is created
           THEN check if the user is created  successfully
        """
        assert new_user == new_user.save()


    def test_single_user_succeeds(self, init_db, new_user):
        """
          GIVEN a User model
          WHEN a new User is created
          THEN check if the user can be retrieved from the database
        """
        new_user.save()
        assert User.query.get(new_user.id) == new_user

    def test_update_user_succeeds(self, init_db, new_user):
        """
          GIVEN a User model
          WHEN a new User is created
          THEN check if the user can be updated and persist in the datatbase
        """
        new_user.save()
        new_user.update_(name='phillip', email='phillip@gmail.com')
        assert new_user.name == 'phillip'
        assert new_user.email == 'phillip@gmail.com'


    def test_delete_a_user_succeeds(self, init_db, new_user):
        """
          GIVEN a User model
          WHEN a new User is created
          THEN check if the user is deleted from the database
        """
        new_user.save()
        new_user.delete_item()

    def test_get_user_string_representation(self, new_user):
        """
        Tests to compute and assert string representation of
        a new user
        :param new_user: creates a new user through the model
        :return: assertion
        """
        assert repr(new_user) == \
            f'<User {new_user.email}>'


