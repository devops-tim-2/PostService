from models.models import Like
from repository import like_repository
from service import post_service

def count_likes(post_id):
    return like_repository.count_likes(post_id)

def count_dislikes(post_id):
    return like_repository.count_dislikes(post_id)
    
def did_i_like(post_id, user):
    return like_repository.like_exists(post_id, user['id'])

def did_i_dislike(post_id, user):
    return like_repository.dislike_exists(post_id, user['id'])

def delete_with_post(post_id: int):
    like_repository.delete_with_post(post_id)

def like(post_id: int, user: dict):
    post_service.get(post_id, user)

    like = like_repository.get(post_id, user['id'])
    if not like:
        like = Like(post_id=post_id, user_id=user['id'], state=True)
    
        like_repository.save(like)
    else:
        state = like.state

        like_repository.delete(like.id)
        if not state:
            like = Like(post_id=post_id, user_id=user['id'], state=True)
        
            like_repository.save(like)

    return True

def dislike(post_id: int, user: dict):
    post_service.get(post_id, user)

    like = like_repository.get(post_id, user['id'])
    if not like:
        like = Like(post_id=post_id, user_id=user['id'], state=False)
    
        like_repository.save(like)
    else:
        state = like.state

        like_repository.delete(like.id)
        if state:
            like = Like(post_id=post_id, user_id=user['id'], state=False)
        
            like_repository.save(like)

    return True
