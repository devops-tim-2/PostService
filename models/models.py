from common.database import db
from dataclasses import dataclass, asdict


@dataclass
class Block(db.Model):
    id: int
    src_user_id: int
    dst_user_id: int

    id = db.Column(db.Integer, primary_key=True)
    src_user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    dst_user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)


    def get_dict(self):
        return asdict(self)


    def __str__(self) -> str:
        return f'Block: id={self.id}, src_user_id={self.src_user_id}, dst_user_id={self.dst_user_id}'


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


@dataclass
class Follow(db.Model):
    id: int
    src_user_id: int
    dst_user_id: int

    id = db.Column(db.Integer, primary_key=True)
    src_user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    dst_user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)


    def get_dict(self):
        return asdict(self)


    def __str__(self) -> str:
        return f'Follow: id={self.id}, src_user_id={self.src_user_id}, dst_user_id={self.dst_user_id}'


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


@dataclass
class Tagged(db.Model):
    id: int
    post_id: int
    user_id: int

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)


    def get_dict(self):
        return asdict(self)


    def __str__(self) -> str:
        return f'Tagged: id={self.id}, post_id={self.post_id}, user_id={self.user_id}'


@dataclass
class User(db.Model):
    id: int

    id = db.Column(db.Integer, primary_key=True)
    

    def get_dict(self):
        return asdict(self)


    def __str__(self) -> str:
        return f'User: id={self.id}'
