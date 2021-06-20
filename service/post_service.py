from broker.producer import publish
from repository import post_repository

def delete(id):
    post_repository.delete_by_id(id)
    publish('post.deleted', id)