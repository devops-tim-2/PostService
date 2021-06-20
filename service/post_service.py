from exception.exceptions import InvalidDataException
from models.models import Post
from common.utils import check
from broker.producer import publish
from repository import post_repository

def create(post_data: dict, user: dict):
    if check(post_data):
        raise InvalidDataException('Some of the values are None, empty value or non-positive value')

    post = Post(description=post_data['description'], image_url=post_data['image_url'], user_id=user['id'])

    post_repository.create(post)
    publish('post.created', post.get_dict())
    publish('post.published', post.get_dict())

    return post.get_dict()

def delete(id):
    post_repository.delete_by_id(id)
    publish('post.deleted', id)