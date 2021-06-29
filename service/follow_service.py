from repository import follow_repository

def find(user_id1: int, user_id2: int) -> bool:
    return user_id1 == user_id2 or follow_repository.find(user_id1, user_id2)