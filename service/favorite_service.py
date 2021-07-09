from repository import favorite_repository
from service import post_service
from models.models import Favorite

def delete_with_post(post_id: int):
    favorite_repository.delete_with_post(post_id)

def favorite(post_id: int, user: dict):
    post_service.get(post_id, user)

    favorite = favorite_repository.get(post_id, user['id'])
    
    if favorite:
        favorite_repository.delete(favorite.id)
    else:
        favorite = Favorite(post_id=post_id, user_id=user['id'])

        favorite_repository.save(favorite)

    return True


def did_i_favorite(post_id, user):
    return favorite_repository.favorite_exists(post_id, user['id'])

def get_all(user):
    return [i.get_dict() for i in favorite_repository.get_all(user['id'])]
