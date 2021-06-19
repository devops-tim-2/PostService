from common.database import db
from dataclasses import dataclass, asdict


@dataclass
class Comment(db.Model):
    id: int
    text: str
    post_id: int
    user_id: int    

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    text = db.Column(db.String(300), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)


    def get_dict(self):
        return asdict(self)


    def __str__(self) -> str:
        return f'Comment: id={self.id}, text={self.text}, post_id={self.post_id}, user_id={self.user_id}'
