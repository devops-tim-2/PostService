from models.models import Follow
from common.database import db_session


def find(user_id1: int, user_id2: int) -> bool:
    return bool(Follow.query.filter_by(src=user_id1, dst=user_id2).first())