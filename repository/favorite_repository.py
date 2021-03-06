from models.models import Favorite
from common.database import db_session


def delete_with_post(post_id: int):
    Favorite.query.filter_by(post_id=post_id).delete()
    db_session.commit()

def get(post_id: int, user_id: int):
    return Favorite.query.filter_by(post_id=post_id, user_id=user_id).first()

def get_all(user_id: int):
    return Favorite.query.filter_by(user_id=user_id).all()


def delete(favorite_id: int):
    Favorite.query.filter_by(id=favorite_id).delete()
    db_session.commit()

def save(favorite: Favorite):
    db_session.add(favorite)
    db_session.commit()


def favorite_exists(post_id, user_id):
    return db_session.query(Favorite.query.filter(Favorite.user_id == user_id, Favorite.post_id == post_id,).exists()).scalar()
