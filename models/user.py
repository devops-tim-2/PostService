from enum import unique
from common.database import db
from dataclasses import dataclass, asdict


@dataclass
class User(db.Model):
    id: int

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    

    def get_dict(self):
        return asdict(self)


    def __str__(self) -> str:
        return f'User: id={self.id}'
