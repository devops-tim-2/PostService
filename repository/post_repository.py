from models.models import Post
from common.database import db_session

def create(post: Post):
    db_session.add(post)
    db_session.commit()

def get(post_id: int) -> Post:
    return Post.query.get(post_id)

def get_users_posts(user_id: int):
    return Post.query.filter_by(user_id=user_id).order_by(Post.id.desc()).all()

def get_all():
    return Post.query.order_by(Post.id.desc()).all()

def delete(post_id: int):
    Post.query.filter_by(id=post_id).delete()
    db_session.commit()
