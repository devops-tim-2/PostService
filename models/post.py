from common.database import db
from dataclasses import dataclass, asdict


@dataclass
class Post(db.Model):
    id: int
    description: str
    image_url: str
    user_id: int

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    description = db.Column(db.String(100))
    image_url = db.Column(db.String(100), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)


    def get_dict(self):
        return asdict(self)


    def __str__(self) -> str:
        return f'Post: id={self.id}, description={self.description}, image_url={self.image_url}, user_id={self.user_id}'
