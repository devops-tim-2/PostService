from models.models import Post
from common.database import db_session

def delete_by_id(id):
    Post.query.filter_by(id=id).delete()
    db_session.commit()
