from models.models import Post
from common.database import db

def delete_by_id(id):
    Post.query.filter_by(id=id).delete()
    db.session.commit()
