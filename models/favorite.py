from common.database import db
from dataclasses import dataclass, asdict


@dataclass
class Favorite(db.Model):
    id: int
    post_id: int
    user_id: int

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)


    def get_dict(self):
        return asdict(self)


    def __str__(self) -> str:
        return f'Favorite: id={self.id}, post_id={self.post_id}, user_id={self.user_id}'
