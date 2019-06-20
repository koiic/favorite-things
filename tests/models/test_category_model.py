from api.models import Category


class TestCategoryModel:

    def test_new_category_succeeds(self, init_db, new_category):
        """
           GIVEN a User model
           WHEN a new User is created
           THEN check if the user is created  successfully
        """
        assert new_category == new_category.save()


    def test_single_category_succeeds(self, init_db, new_category):
        """
          GIVEN a User model
          WHEN a new User is created
          THEN check if the user can be retrieved from the database
        """
        new_category.save()
        assert Category.query.get(new_category.id) == new_category

    def test_update_category_succeeds(self, init_db, new_category):
        """
          GIVEN a User model
          WHEN a new User is created
          THEN check if the user can be updated and persist in the datatbase
        """
        new_category.save()
        new_category.update_(type="playing")
        assert new_category.type == 'playing'


    def test_delete_a_category_succeeds(self, init_db, new_category):
        """
          GIVEN a User model
          WHEN a new User is created
          THEN check if the user is deleted from the database
        """
        new_category.save()
        new_category.delete()

    def test_get_category_string_representation(self, new_category):
        """
        Tests to compute and assert string representation of
        a new user
        :param new_user: creates a new user through the model
        :return: assertion
        """
        assert repr(new_category) == \
            f'<Category {new_category.type}>'


