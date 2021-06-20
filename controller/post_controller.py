from exception.exceptions import InvalidAuthException, InvalidDataException
from flask_restful import Resource, reqparse
from common.utils import auth
from service import post_service

post_parser = reqparse.RequestParser()
post_parser.add_argument('Authorization', type=str, location='headers', required=True)
post_parser.add_argument('description', type=str, help='Description for post')
post_parser.add_argument('image_url', type=str, help='Image url for post')
 
comment_parser = reqparse.RequestParser()
comment_parser.add_argument('text', type=str, help='Text of the comment')

 
class PostResource(Resource):
    def __init__(self):
        # To be implemented.
        pass
 
    def get(self, post_id):
        # To be implemented.
        pass

    def delete(self, post_id):
        # To be implemented.
        pass
 
class PostListResource(Resource):
    def __init__(self):
        # To be implemented.
        pass
 
    def post(self):
        args = post_parser.parse_args()
        token = args['Authorization'].split(' ')[1]
        del args['Authorization']

        try:
            user = auth(token)

            return post_service.create(args, user), 200
        except InvalidAuthException as e:
            return str(e), 401
        except InvalidDataException as e:
            return str(e), 400
 
class ProfileResource(Resource):
    def __init__(self):
        # To be implemented.
        pass
 
    def get(self, user_id):
        # To be implemented.
        pass
 
class LikeResource(Resource):
    def __init__(self):
        # To be implemented.
        pass
 
    def get(self, post_id):
        # To be implemented.
        pass

class DislikeResource(Resource):
    def __init__(self):
        # To be implemented.
        pass
 
    def get(self, post_id):
        # To be implemented.
        pass

class FavoriteResource(Resource):
    def __init__(self):
        # To be implemented.
        pass
 
    def get(self, post_id):
        # To be implemented.
        pass
 
 
class CommentResource(Resource):
    def __init__(self):
        # To be implemented.
        pass
 
    def post(self, post_id):
        # To be implemented.
        pass
 