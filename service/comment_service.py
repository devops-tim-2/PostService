from repository import comment_repository

def delete_with_post(post_id: int):
    comment_repository.delete_with_post(post_id)