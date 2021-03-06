from exception.exceptions import InvalidDataException, NotAccessibleException, NotFoundException
from models.models import Post
from common.utils import check
from broker.producer import publish
from service import block_service, follow_service, user_service, favorite_service, tagged_service, like_service, comment_service
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


    post_dict = post.get_dict()

    owner = user_service.get(post.user_id)

    post_dict['comments'] = [i.get_dict() for i in comment_service.get_for_post(post_id)]
    post_dict['likes'] = like_service.count_likes(post_id)
    post_dict['dislikes'] = like_service.count_dislikes(post_id)
    post_dict['liked'] = like_service.did_i_like(post_id, user)
    post_dict['disliked'] = like_service.did_i_dislike(post_id, user)
    post_dict['favorited'] = favorite_service.did_i_favorite(post_id, user)


    if (not(user and owner.id == user['id'])) and not owner.public and (not user or not follow_service.find(user['id'], post.user_id)):
        raise NotFoundException(f'Post with id {post_id} not found.')

    return post_dict

def get_users_posts(profile_id: int, user: dict, page: int, per_page: int):
    profile = user_service.get(profile_id)

    if not profile or (user and block_service.find(user['id'], profile_id)):
        raise NotFoundException(f'Profile with id {profile_id} not found.')

    posts = post_repository.get_users_posts(profile_id)
    posts = posts[(page-1)*per_page : page*per_page]

    if (not(user and profile.id == user['id'])) and not profile.public and (not user or not follow_service.find(user['id'], profile_id)):
        raise NotAccessibleException(f'Profile with id {profile_id} is private.')

    post_dicts = [post.get_dict() for post in posts]
    for post_dict in post_dicts:
        post_dict['comments'] = len(comment_service.get_for_post(post_dict['id']))
        post_dict['likes'] = like_service.count_likes(post_dict['id']) - like_service.count_dislikes(post_dict['id'])
    return post_dicts

def delete(post_id: int):
    post = post_repository.get(post_id)

    if not post:
        raise NotFoundException(f'Post with id {post_id} not found.')

    favorite_service.delete_with_post(post_id)
    tagged_service.delete_with_post(post_id)
    like_service.delete_with_post(post_id)
    comment_service.delete_with_post(post_id)

    post_repository.delete(post_id)
    publish('post.deleted', post_id)

    return True

def get_all(page: int, per_page: int):
    posts = post_repository.get_all()
    return [post.get_dict() for post in posts][(page-1)*per_page : page*per_page]

def inappropriate(post_id: int, user: dict):
    post = get(post_id, user)

    data = {
        'description': post['description'],
        'image_url': post['image_url'],
        'post_id': post['id'],
        'reporter_id': user['id']
    }

    publish('post.inappropriate', data)
