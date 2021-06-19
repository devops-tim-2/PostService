# from common.utils import auth
from flask import Blueprint, request
# from services import post_service

post_api = Blueprint('order_api', __name__)


@post_api.route('/profile/<int:user_id>', methods=["GET"])
def get_users_posts(user_id: int):
    # result, code = auth(request.headers)
    # if code != 200:
    #     result, code

    # return post_service.get_users_posts(user_id, result)
    return "OK", 200


@post_api.route('/<int:post_id>', methods=["GET"])
def get(post_id: int):
    # result, code = auth(request.headers)
    # if code != 200:
    #     result, code

    # return post_service.get(post_id, result)
    return "OK", 200


@post_api.route('', methods=["POST"])
def create():
    # result, code = auth(request.headers)
    # if code != 200:
    #     result, code

    # data = request.get_json()
    # return post_service.create(data, result)
    return "OK", 200


@post_api.route('/like/<int:post_id>', methods=["PUT"])
def like(post_id: int):
    # result, code = auth(request.headers)
    # if code != 200:
    #     result, code

    # return post_service.like(post_id, result)
    return "OK", 200


@post_api.route('/dislike/<int:post_id>', methods=["PUT"])
def dislike(post_id: int):
    # result, code = auth(request.headers)
    # if code != 200:
    #     result, code

    # return post_service.dislike(post_id, result)
    return "OK", 200


@post_api.route('/favorite/<int:post_id>', methods=["PUT"])
def favorite(post_id: int):
    # result, code = auth(request.headers)
    # if code != 200:
    #     result, code

    # return post_service.favorite(post_id, result)
    return "OK", 200


@post_api.route('/comment', methods=["POST"])
def comment():
    # result, code = auth(request.headers)
    # if code != 200:
    #     result, code

    # data = request.get_json()
    # return post_service.comment(data, result)
    return "OK", 200


@post_api.route('/<int:post_id>', methods=["DELETE"])
def delete(post_id: int):
    # result, code = auth(request.headers)
    # if code != 200:
    #     result, code

    # return post_service.delete(post_id, result)
    return "OK", 200
