from models.models import User

def get(user_id: int) -> User:
    return User.query.get(user_id)