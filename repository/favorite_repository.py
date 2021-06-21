from models.models import Favorite
from common.database import db_session


def delete_with_post(post_id: int):
    Favorite.query.filter_by(post_id=post_id).delete()
    db_session.commit()