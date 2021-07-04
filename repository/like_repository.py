from models.models import Like
from common.database import db_session

def count_likes(post_id):
    return len(Like.query.filter_by(post_id=post_id,state=True).all())

def count_dislikes(post_id):
    return len(Like.query.filter_by(post_id=post_id,state=False).all())
    
def like_exists(post_id, user_id):
    return db_session.query(Like.query.filter(Like.user_id == user_id, Like.post_id == post_id, Like.state == True).exists()).scalar()

def dislike_exists(post_id, user_id):
    return db_session.query(Like.query.filter(Like.user_id == user_id, Like.post_id == post_id, Like.state == False).exists()).scalar()


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