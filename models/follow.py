from common.database import db
from dataclasses import dataclass, asdict


@dataclass
class Follow(db.Model):
    id: int
    src_user_id: int
    dst_user_id: int

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    src_user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    dst_user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)


    def get_dict(self):
        return asdict(self)


    def __str__(self) -> str:
        return f'Follow: id={self.id}, src_user_id={self.src_user_id}, dst_user_id={self.dst_user_id}'
