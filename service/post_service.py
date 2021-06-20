from models.models import Post
from common.utils import check
from broker.producer import publish
from repository import post_repository

def create(post_data: dict, user: dict) -> Post:
    if check(post_data):
        return 'Some of the values are None, empty value or non-positive value', 400

    post = Post(description=post_data['description'], image_url=post_data['image_url'], user_id=user['id'])

    post_repository.create(post)
    publish('post.created', post)
    publish('post.published', post)

    return post.get_dict(), 200

def delete(id):
    post_repository.delete_by_id(id)
    publish('post.deleted', id)