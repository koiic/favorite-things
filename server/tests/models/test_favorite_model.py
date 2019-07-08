from api.models import Favorite


class TestFavoriteModel:

    def test_new_favorite_succeeds(self, init_db, new_favorite, new_category):
        """
           GIVEN a Favorite model
           WHEN a new favorite is created
           THEN check if the favorite is created  successfully
        """
        new_category.save()
        new_favorite.category_id = new_category.id
        assert new_favorite == new_favorite.save()


    def test_single_favorite_succeeds(self, init_db, new_favorite, new_category):
        """
        GIVEN a Favorite model
        WHEN a new favorite is created
        THEN check if the favorite can be retrieved from the database
        """
        new_category.save()
        new_favorite.category_id = new_category.id
        new_favorite.save()
        assert Favorite.query.get(new_favorite.id) == new_favorite

    def test_update_favorite_succeeds(self, init_db, new_favorite, new_category):
        """
        GIVEN a Favorite model
        WHEN a new favorite is created
        THEN check if the favorite can be updated and persist in the datatbase
        """
        new_favorite.save()
        new_category.save()
        new_favorite.category_id = new_category.id
        new_favorite.update_(title="fish", rank=1)
        assert new_favorite.title == 'fish'
        assert new_favorite.rank == 1

    #
    def test_delete_a_favorite_succeeds(self, init_db, new_favorite):
        """
        GIVEN a Favorite model
        WHEN a new favorite is created
        THEN check if the favorite is deleted from the database
        """
        new_favorite.save()
        new_favorite.delete_item()

    def test_get_favorite_string_representation(self, new_favorite):
        """
        Tests to compute and assert string representation of
        a new favorite
        :param new_favorite: creates a new favorite through the model
        :return: assertion
        """
        assert repr(new_favorite) == \
            f'<Favorite {new_favorite.title}>'


