from repository import favorite_repository

def delete_with_post(post_id: int):
    favorite_repository.delete_with_post(post_id)