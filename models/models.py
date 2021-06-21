from dataclasses import dataclass, asdict

from sqlalchemy import Column, Integer, String, Boolean, \
     ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Model = declarative_base(name='Model')

@dataclass
class Block(Model):
    __tablename__ = 'block'
    id: int
    src: int
    dst: int

    id = Column(Integer, primary_key=True)
    src = Column(Integer, ForeignKey('user_profile.id'), nullable=False)
    dst = Column(Integer, ForeignKey('user_profile.id'), nullable=False)


    def get_dict(self):
        return asdict(self)


    def __str__(self) -> str:
        return f'Block: id={self.id}'


@dataclass
class Comment(Model):
    __tablename__ = 'comment'
    id: int
    text: str
    post_id: int
    user_id: int    

    id = Column(Integer, primary_key=True, autoincrement=True)
    text = Column(String(300), nullable=False)
    post_id = Column(Integer, ForeignKey('post.id'), nullable=False)
    user_id = Column(Integer, ForeignKey('user_profile.id'), nullable=False)


    def get_dict(self):
        return asdict(self)


    def __str__(self) -> str:
        return f'Comment: id={self.id}, text={self.text}, post_id={self.post_id}, user_id={self.user_id}'


@dataclass
class Favorite(Model):
    __tablename__ = 'favorite'
    id: int
    post_id: int
    user_id: int

    id = Column(Integer, primary_key=True, autoincrement=True)
    post_id = Column(Integer, ForeignKey('post.id'), nullable=False)
    user_id = Column(Integer, ForeignKey('user_profile.id'), nullable=False)


    def get_dict(self):
        return asdict(self)


    def __str__(self) -> str:
        return f'Favorite: id={self.id}, post_id={self.post_id}, user_id={self.user_id}'


@dataclass
class Follow(Model):
    __tablename__ = 'follow'
    id: int
    mute: bool
    src: int
    dst: int

    id = Column(Integer, primary_key=True)
    mute = Column(Boolean, nullable=False)
    src = Column(Integer, ForeignKey('user_profile.id'), nullable=False)
    dst = Column(Integer, ForeignKey('user_profile.id'), nullable=False)


    def get_dict(self):
        return asdict(self)


    def __str__(self) -> str:
        return f'Follow: id={self.id}'


@dataclass
class Like(Model):
    __tablename__ = 'like'
    id: int
    post_id: int
    user_id: int
    state: bool

    id = Column(Integer, primary_key=True, autoincrement=True)
    post_id = Column(Integer, ForeignKey('post.id'), nullable=False)
    user_id = Column(Integer, ForeignKey('user_profile.id'), nullable=False)
    state = Column(Boolean, nullable=False)

    def get_dict(self):
        return asdict(self)


    def __str__(self) -> str:
        return f'Like: id={self.id}, post_id={self.post_id}, user_id={self.user_id}, state={self.state}'


@dataclass
class Post(Model):
    __tablename__ = 'post'
    id: int
    description: str
    image_url: str
    user_id: int

    id = Column(Integer, primary_key=True, autoincrement=True)
    description = Column(String(100))
    image_url = Column(String(100), nullable=False)
    user_id = Column(Integer, ForeignKey('user_profile.id'), nullable=False)


    def get_dict(self):
        return asdict(self)


    def __str__(self) -> str:
        return f'Post: id={self.id}, description={self.description}, image_url={self.image_url}, user_id={self.user_id}'


@dataclass
class Tagged(Model):
    __tablename__ = 'tagged'
    id: int
    post_id: int
    user_id: int

    id = Column(Integer, primary_key=True, autoincrement=True)
    post_id = Column(Integer, ForeignKey('post.id'), nullable=False)
    user_id = Column(Integer, ForeignKey('user_profile.id'), nullable=False)


    def get_dict(self):
        return asdict(self)


    def __str__(self) -> str:
        return f'Tagged: id={self.id}, post_id={self.post_id}, user_id={self.user_id}'


@dataclass
class User(Model):
    __tablename__ = 'user_profile'
    id: int
    public: bool

    id = Column(Integer, primary_key=True)
    public = Column(Boolean, nullable=False)
    

    def get_dict(self):
        return asdict(self)


    def __str__(self) -> str:
        return f'User: id={self.id}, public={self.public}'
