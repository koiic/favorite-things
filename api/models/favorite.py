from .base import BaseModel
from .database import db

class Favorite(BaseModel):
    """
    Model For Favorite
    """
    __tablename__ = 'favorite_things'

    title = db.Column(db.String(60), nullable=False)
    description = db.Column(db.String(200), nullable=True)
    meta_data = db.Column(db.JSON, nullable=True)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    rank = db.Column(db.Integer, default=None, nullable=True)

    def get_child_relationship(self):
        """
        Method to get all child relationships a model has. Override in the
        subclass if the model has child models.
        """
        return None

    def __repr__(self):
        return '<Favorite {}>'.format(self.title)

    @staticmethod
    def find_by_title_and_user(title, user_id):
        return Favorite.query.filter_by(title=title, user_id=user_id).first()

    @staticmethod
    def find_by_id_and_user(favorite_id, user_id):
        return Favorite.query.filter_by(id=favorite_id, user_id=user_id, deleted=False).first()

    @staticmethod
    def get_all_favorite(user_id):
        return Favorite.query.filter_by(user_id=user_id, deleted=False).all()

    @staticmethod
    def find_ranking_by_category_and_user(category_id, user_id, rank):
        return Favorite.query.filter_by(category_id=category_id, user_id=user_id, rank=rank).first()

    @staticmethod
    def get_ranks(rank):
        return Favorite.query.filter(Favorite.rank >= rank).all()

    # @staticmethod
    # def update_ranks(new_rank, previous_rank):
    #     ranks = Favorite.query.filter(Favorite.rank >= new_rank).all()
    #     if new_rank > previous_rank:
    #         substract_from_ranks(ranks)
    #     add_to_ranks(ranks)

    @staticmethod
    def get_last_favorite_in_category(**kwargs):
        last_favorite_thing = Favorite.query.filter(
            Favorite.user_id == kwargs['user_id'],
            Favorite.category_id == kwargs['category_id'])\
            .order_by(Favorite.rank.desc()).first()
        if not last_favorite_thing:
            kwargs['rank'] = 1

        if ('id' in kwargs and last_favorite_thing
                and kwargs['rank'] > last_favorite_thing.rank):  # noqa
            kwargs['rank'] = last_favorite_thing.rank

        if ('id' not in kwargs and last_favorite_thing
                and kwargs['rank'] > last_favorite_thing.rank):  # noqa
            kwargs['rank'] = last_favorite_thing.rank + 1
        return kwargs['rank']

    @staticmethod
    def reorder_favorite_things_on_create(**kwargs):

        return Favorite.query.filter(
            Favorite.user_id == kwargs['user_id'],
            Favorite.category_id == kwargs['category_id'],
            Favorite.rank >= kwargs['rank']
        ).update({
            Favorite.rank: Favorite.rank + 1},  synchronize_session=False
        )

    @staticmethod
    def reorder_favorite_things_on_update(**kwargs):
        if 'id' in kwargs:
            favorite_thing = kwargs['favorite_things']
            if favorite_thing.rank < kwargs['rank']:
                Favorite.query.filter(
                    Favorite.user_id == kwargs['user_id'],
                    Favorite.category_id == kwargs['category_id'],
                    Favorite.rank > favorite_thing.rank,
                    Favorite.rank <= kwargs['rank'],
                    Favorite.id != kwargs['id']
                ).update({
                    Favorite.rank: Favorite.rank - 1
                }, synchronize_session=False)
            elif favorite_thing.rank > kwargs['rank']:
                Favorite.query.filter(
                    Favorite.user_id == kwargs['user_id'],
                    Favorite.category_id == kwargs['category_id'],
                    Favorite.rank < favorite_thing.rank,
                    Favorite.rank >= kwargs['rank'],
                    Favorite.id != kwargs['id']
                ).update({
                    Favorite.rank: Favorite.rank + 1
                }, synchronize_session=False)


    @staticmethod
    def reorder_deleted_favorite_things(**kwargs):
        favorite_thing = kwargs['favorite_things']
        if favorite_thing.rank < kwargs['rank']:
            Favorite.query.filter(
                Favorite.user_id == kwargs['user_id'],
                Favorite.category_id == kwargs['category_id'],
                Favorite.rank > favorite_thing.rank,
                Favorite.rank <= kwargs['rank'],
                Favorite.id != kwargs['id']
            ).update({
                Favorite.rank: Favorite.rank - 1
            }, synchronize_session=False)

    # soft delete a favorite thing
    @staticmethod
    def delete_favorite_thing(id):
        favorite = Favorite.query.get(id)
        if favorite:
            favorite.deleted = True
        db.session.commit()

    @staticmethod
    def get_by_category(category_id, user_id):
        return Favorite.query.filter_by(category_id=category_id, user_id=user_id, deleted=False).all()
