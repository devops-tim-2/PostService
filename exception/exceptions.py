class InvalidDataException(Exception):
    def __init__(self, message="Invalid data"):
        super().__init__(message)

class InvalidAuthException(Exception):
    def __init__(self, message="Invalid auth data"):
        super().__init__(message)

class NotFoundException(Exception):
    def __init__(self, message="Entity not found"):
        super().__init__(message)