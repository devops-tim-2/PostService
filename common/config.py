from os import environ
from typing import Tuple
from flask_cors import CORS
from flask.app import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect
from flask_restful import Api
from common.database import db
from models.models import Block, Comment, Favorite, Follow, Like, Post, Tagged, User
from controller.post_controller import PostResource, PostListResource, ProfileResource, LikeResource, DislikeResource, FavoriteResource, CommentResource


DevConfig = {
    'DEBUG': True,
    'DEVELOPMENT': True,
    'SQLALCHEMY_DATABASE_URI': f'{environ.get("DB_TYPE")}+{environ.get("DB_DRIVER")}://{environ.get("DB_USER")}:{environ.get("DB_PASSWORD")}@{environ.get("DB_HOST")}/{environ.get("DB_NAME")}',
    'SQLALCHEMY_ECHO': True,
    'SQLALCHEMY_TRACK_MODIFICATIONS': False
}


ProdConfig = {}


TestConfig = {
    'DEBUG': False,
    'DEVELOPMENT': True,
    'SQLALCHEMY_DATABASE_URI': f'{environ.get("TEST_DATABASE_URI")}',
    'SQLALCHEMY_ECHO': True,
    'SQLALCHEMY_TRACK_MODIFICATIONS': False
}


config: dict = {
    'dev': DevConfig,
    'prod': ProdConfig,
    'test': TestConfig
}


def setup_config(cfg_name: str) -> Tuple[Flask, SQLAlchemy]:
    app = Flask(__name__)

    if environ.get('ENABLE_CSRF') == 1:
        app.config['SECRET_KEY'] = environ.get('SECRET_KEY')
        app.config['WTF_CSRF_SECRET_KEY'] = environ.get('WTF_CSRF_SECRET_KEY')
        csrf = CSRFProtect()
        csrf.init_app(app)
        
    CORS(app, resources={r"/*": {"origins": "http://localhost:3000", "send_wildcard": "False"}})

    api = Api(app)

    
    api.add_resource(PostResource, '/api/<post_id>')
    api.add_resource(PostListResource, '/api')
    api.add_resource(ProfileResource, '/api/profile/<user_id>')
    api.add_resource(LikeResource, '/api/like/<post_id>')
    api.add_resource(DislikeResource, '/api/dislike/<post_id>')
    api.add_resource(FavoriteResource, '/api/favorite/<post_id>')
    api.add_resource(CommentResource, '/api/comment/<post_id>')

    cfg = config.get(cfg_name)
    for key in cfg.keys():
        app.config[key] = cfg[key]

    app.app_context().push()
    db.init_app(app)

    with app.app_context():
        db.create_all()

    if cfg_name == 'test':
        Block.query.delete()
        Comment.query.delete()
        Favorite.query.delete()
        Follow.query.delete()
        Like.query.delete()
        Tagged.query.delete()
        Post.query.delete()
        User.query.delete()

    return app, db
