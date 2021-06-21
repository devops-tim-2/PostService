from repository import block_repository

def find(user_id1: int, user_id2: int) -> bool:
    return block_repository.find(user_id1, user_id2)