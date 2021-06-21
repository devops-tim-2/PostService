from os import environ
environ['SQLALCHEMY_DATABASE_URI'] = environ.get("TEST_DATABASE_URI")

from models.models import Post
from common.config import setup_config
from common.utils import generate_token
import json


class TestPost:
    @classmethod
    def setup_class(cls):
        cls.app = setup_config('test')
        from common.database import db_session

        cls.user_data = dict(id=1, username="milos", password="milos", role="user", age=18, sex="m", region="srb", interests="sport", bio="some bio", website="https://milos.com", phone="some phone", mail="milos@mail.com", profile_image_link="https://milos.com/profile.jpg", public=True, taggable=True)
        cls.token = generate_token(cls.user_data)

        cls.post = Post(description='some nice description3', image_url='some nice image_url3', user_id=cls.user_data['id'])
        db_session.add(cls.post)
        db_session.commit()

        cls.client = cls.app.test_client()


    def test_create_happy(cls):
        post_count_before = Post.query.count()

        post_data = dict(description='some nice description', image_url='some nice image_url')
        create_response = cls.client.post('/api', data=json.dumps(post_data), headers={'Authorization': f'Bearer {cls.token}', 'Content-Type': 'application/json'}).get_json()
        post_db = Post.query.get(create_response['id'])

        post_count_after = Post.query.count()

        assert post_count_after == post_count_before + 1
        assert post_db.description == post_data['description']
        assert post_db.image_url == post_data['image_url']
        assert post_db.user_id == cls.user_data['id']


    def test_create_sad(cls):
        post_count_before = Post.query.count()

        post_data = dict(description='some nice description 2', image_url='')
        create_response = cls.client.post('/api', data=json.dumps(post_data), headers={'Authorization': f'Bearer {cls.token}', 'Content-Type': 'application/json'}).get_json()
        
        post_count_after = Post.query.count()

        assert post_count_after == post_count_before


    def test_get_happy(cls):
        get_response = cls.client.get(f'/api/{cls.post.id}', headers={'Authorization': f'Bearer {cls.token}', 'Content-Type': 'application/json'}).get_json()
        print('HAPPY:', get_response)
        assert get_response['id'] == cls.post.id


    def test_get_sad(cls):
        get_response = cls.client.get(f'/api/{2}', headers={'Authorization': f'Bearer {cls.token}', 'Content-Type': 'application/json'}).get_json()
        print('SAD:', get_response)
        assert get_response['id'] == cls.post.id
