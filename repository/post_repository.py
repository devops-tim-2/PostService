from models.models import Post
from common.database import db_session

def create(post: Post):
    db_session.add(post)
    db_session.commit()

def get(post_id: int) -> Post:
    return Post.query.get(post_id)

def delete_by_id(id):
    Post.query.filter_by(id=id).delete()
    db_session.commit()
