from os import environ
environ['SQLALCHEMY_DATABASE_URI'] = environ.get("TEST_DATABASE_URI")

from models.models import Block, Post, User, Like
from common.config import setup_config
from common.utils import generate_token
import json, pytest

class TestLike:
    @classmethod
    def setup_class(cls):
        cls.app = setup_config('test')
        from common.database import db_session

        cls.user1 = User(public=True)
        db_session.add(cls.user1)
        db_session.commit()

        cls.user2 = User(public=True)
        db_session.add(cls.user2)
        db_session.commit()

        cls.user3 = User(public=True)
        db_session.add(cls.user3)
        db_session.commit()

        block = Block(src=cls.user1.id, dst=cls.user3.id)
        db_session.add(block)
        db_session.commit()

        user1_data = dict(id=cls.user1.id, username="milos", password="milos", role="user", age=18, sex="m", region="srb", interests="sport", bio="some bio", website="https://milos.com", phone="some phone", mail="milos@mail.com", profile_image_link="https://milos.com/profile.jpg", public=cls.user1.public, taggable=True)
        user2_data = dict(id=cls.user2.id, username="milos2", password="milos2", role="user", age=18, sex="m", region="srb2", interests="sport2", bio="some bio2", website="https://milos2.com", phone="some phone2", mail="milos2@mail.com", profile_image_link="https://milos2.com/profile.jpg", public=cls.user2.public, taggable=True)
        user3_data = dict(id=cls.user3.id, username="milos3", password="milos3", role="user", age=18, sex="m", region="srb3", interests="sport3", bio="some bio3", website="https://milos3.com", phone="some phone3", mail="milos3@mail.com", profile_image_link="https://milos3.com/profile.jpg", public=cls.user3.public, taggable=True)

        cls.token_user1 = generate_token(user1_data)
        cls.token_user2 = generate_token(user2_data)
        cls.token_user3 = generate_token(user3_data)

        cls.post1 = Post(description='some nice description3', image_url='some nice image_url3', user_id=cls.user1.id)
        db_session.add(cls.post1)
        db_session.commit()

        cls.client = cls.app.test_client()


    def test_like_happy(cls):
        cls.client.get(f'/api/like/{cls.post1.id}', headers={'Authorization': f'Bearer {cls.token_user2}', 'Content-Type': 'application/json'})

        like = Like.query.filter_by(post_id=cls.post1.id, user_id=cls.user2.id, state=True)

        assert like is not None


    def test_like_sad(cls):
        like_count_before = Post.query.count()
        cls.client.get(f'/api/like/{cls.post1.id}', headers={'Authorization': f'Bearer {cls.token_user3}', 'Content-Type': 'application/json'})
        like_count_after = Post.query.count()

        assert like_count_before == like_count_after


    def test_dislike_happy(cls):
        cls.client.get(f'/api/dislike/{cls.post1.id}', headers={'Authorization': f'Bearer {cls.token_user2}', 'Content-Type': 'application/json'})

        like = Like.query.filter_by(post_id=cls.post1.id, user_id=cls.user2.id, state=False)

        assert like is not None


    def test_dislike_sad(cls):
        like_count_before = Post.query.count()
        cls.client.get(f'/api/like/{cls.post1.id}', headers={'Authorization': f'Bearer {cls.token_user3}', 'Content-Type': 'application/json'})
        like_count_after = Post.query.count()

        assert like_count_before == like_count_after