from exception.exceptions import InvalidAuthException, InvalidDataException, NotAccessibleException, NotFoundException
from flask_restful import Resource, reqparse
from flask import request
from common.utils import auth
from service import post_service, like_service, favorite_service, comment_service

post_parser = reqparse.RequestParser()
post_parser.add_argument('Authorization', type=str, location='headers', required=True)
post_parser.add_argument('description', type=str, help='Description for post')
post_parser.add_argument('image_url', type=str, help='Image url for post')
 
comment_parser = reqparse.RequestParser()
comment_parser.add_argument('Authorization', type=str, location='headers', required=True)
comment_parser.add_argument('text', type=str, help='Text of the comment')

 
class PostResource(Resource):
    def __init__(self):
        # To be implemented.
        pass
 
    def get(self, post_id):        
        try:
            if not request.headers.has_key('Authorization'):
                return post_service.get(post_id, None), 200
            else:
                token = request.headers['Authorization'].split(' ')[1]
                user = auth(token)

                return post_service.get(post_id, user), 200
        except InvalidAuthException as e:
            return str(e), 401
        except NotFoundException as e:
            return str(e), 404

    def delete(self, post_id):
        try:
            if not request.headers.has_key('Authorization'):
                return 'Forbidden, unauthorized atempt.', 403
            else:
                token = request.headers['Authorization'].split(' ')[1]
                user = auth(token)

                if post_service.get(post_id, user)['user_id'] != user['id']:
                    return 'You can\'t delete someone else\'s post.', 401

                return post_service.delete(post_id), 200
        except InvalidAuthException as e:
            return str(e), 401
        except NotFoundException as e:
            return str(e), 404
        except InvalidDataException as e:
            return str(e), 400
 
class PostListResource(Resource):
    def __init__(self):
        # To be implemented.
        pass
 
    def get(self):
        page = int(request.args.get('page')) if request.args.get('page') else 1
        per_page = int(request.args.get('per_page')) if request.args.get('per_page') else 10

        return post_service.get_all(page, per_page)
        
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
        page = int(request.args.get('page')) if request.args.get('page') else 1
        per_page = int(request.args.get('per_page')) if request.args.get('per_page') else 10

        try:
            if not request.headers.has_key('Authorization'):
                return post_service.get_users_posts(user_id, None, page, per_page), 200
            else:
                token = request.headers['Authorization'].split(' ')[1]
                user = auth(token)

                return post_service.get_users_posts(user_id, user, page, per_page), 200
        except InvalidAuthException as e:
            return str(e), 401
        except NotFoundException as e:
            return str(e), 404
        except NotAccessibleException as e:
            return str(e), 400
 
class LikeResource(Resource):
    def __init__(self):
        # To be implemented.
        pass
 
    def get(self, post_id):
        try:
            if not request.headers.has_key('Authorization'):
                return 'Forbidden, unauthorized atempt.', 403
            else:
                token = request.headers['Authorization'].split(' ')[1]
                user = auth(token)

                return like_service.like(post_id, user), 200
        except InvalidAuthException as e:
            return str(e), 401
        except NotFoundException as e:
            return str(e), 404

class DislikeResource(Resource):
    def __init__(self):
        # To be implemented.
        pass
 
    def get(self, post_id):
        try:
            if not request.headers.has_key('Authorization'):
                return 'Forbidden, unauthorized atempt.', 403
            else:
                token = request.headers['Authorization'].split(' ')[1]
                user = auth(token)

                return like_service.dislike(post_id, user), 200
        except InvalidAuthException as e:
            return str(e), 401
        except NotFoundException as e:
            return str(e), 404

class FavoriteResource(Resource):
    def __init__(self):
        # To be implemented.
        pass
 
    def get(self, post_id):
        try:
            if not request.headers.has_key('Authorization'):
                return 'Forbidden, unauthorized atempt.', 403
            else:
                token = request.headers['Authorization'].split(' ')[1]
                user = auth(token)

                return favorite_service.favorite(post_id, user), 200
        except InvalidAuthException as e:
            return str(e), 401
        except NotFoundException as e:
            return str(e), 404
 
 
class CommentResource(Resource):
    def __init__(self):
        # To be implemented.
        pass
 
    def post(self, post_id):
        args = comment_parser.parse_args()
        token = args['Authorization'].split(' ')[1]
        del args['Authorization']

        try:
            user = auth(token)

            return comment_service.comment(post_id, args, user), 200
        except InvalidAuthException as e:
            return str(e), 401
        except (InvalidDataException, NotAccessibleException) as e:
            return str(e), 400
        except NotFoundException as e:
            return str(e), 404
 