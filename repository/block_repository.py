from models.models import Block
from common.database import db_session


def find(user_id1: int, user_id2: int) -> bool:
    return bool(Block.query.filter_by(src=user_id1, dst=user_id2).first()) or\
           bool(Block.query.filter_by(src=user_id2, dst=user_id1).first())
