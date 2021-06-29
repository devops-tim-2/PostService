from models.models import Comment
from repository import comment_repository
from service import post_service

def delete_with_post(post_id: int):
    comment_repository.delete_with_post(post_id)

def comment(post_id: int, comment_data: dict, user: dict):
    post_service.get(post_id, user)

    comment = Comment(text=comment_data['text'], post_id=post_id, user_id=user['id'])

    comment_repository.save(comment)