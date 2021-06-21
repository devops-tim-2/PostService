from models.models import Comment
from common.database import db_session


def delete_with_post(post_id: int):
    Comment.query.filter_by(post_id=post_id).delete()
    db_session.commit()