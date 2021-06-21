from exception.exceptions import InvalidDataException, NotFoundException
from models.models import Post
from common.utils import check
from broker.producer import publish
from service import block_service, follow_service, user_service
from repository import post_repository

def create(post_data: dict, user: dict):
    if check(post_data):
        raise InvalidDataException('Some of the values are None, empty value or non-positive value')

    post = Post(description=post_data['description'], image_url=post_data['image_url'], user_id=user['id'])

    post_repository.create(post)
    publish('post.created', post.get_dict())
    publish('post.published', post.get_dict())

    return post.get_dict()

def get(post_id: int, user: dict):
    post = post_repository.get(post_id)

    if not post or (user and block_service.find(user['id'], post.user_id)):
        raise NotFoundException(f'Post with id {post_id} not found.')

    owner = user_service.get(post.user_id)

    if user and owner.id == user['id']:
        return post.get_dict()

    if not owner.public:
        if not user or not follow_service.find(user['id'], post.user_id):
            raise NotFoundException(f'Post with id {post_id} not found.')

    return post.get_dict()

def delete(id):
    post_repository.delete_by_id(id)
    publish('post.deleted', id)