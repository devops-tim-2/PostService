from models.models import Like
from common.database import db_session


def delete_with_post(post_id: int):
    Like.query.filter_by(post_id=post_id).delete()
    db_session.commit()

def get(post_id: int, user_id: int):
    return Like.query.filter_by(post_id=post_id, user_id=user_id).first()

def delete(like_id: int):
    Like.query.filter_by(id=like_id).delete()
    db_session.commit()

def save(like: Like):
    db_session.add(like)
    db_session.commit()