from common.database import db
from dataclasses import dataclass, asdict


@dataclass
class Like:
    id: int
    post_id: int
    user_id: int
    state: bool

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    state = db.Column(db.Boolean, nullable=False)

    def get_dict(self):
        return asdict(self)


    def __str__(self) -> str:
        return f'Like: id={self.id}, post_id={self.post_id}, user_id={self.user_id}, state={self.state}'
