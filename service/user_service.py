from models.models import User
from repository import user_repository

def get(user_id: int) -> User:
    return user_repository.get(user_id)