from exception.exceptions import NotFoundException
from models.models import Like
from service import like_service
import pytest


def test_like_ok(mocker):
    user_data = {
        "id": 1
    }

    owner_data = {
        "id": 2,
        "public": True
    }

    post_data = {
        "id": 1,
        "description": "Some nice description",
        "image_url": "https://somenicewebsite.com/image.jpg",
        "user_id": owner_data["id"]
    }

    mocker.patch('service.like_service.post_service.get', return_value=post_data)
    mocker.patch('service.like_service.like_repository.get', return_value=None)

    like_service.like(post_data['id'], user_data)

    like = Like.query.filter_by(post_id=post_data['id'], user_id=user_data['id'], state=True)

    assert like is not None


def test_like_post_not_found(mocker):
    user_data = {
        "id": 1
    }

    mocker.patch('service.like_service.post_service.post_repository.get', return_value=None)

    with pytest.raises(NotFoundException):
        like_service.like(1, user_data)


def test_dislike_ok(mocker):
    user_data = {
        "id": 1
    }

    owner_data = {
        "id": 2,
        "public": True
    }

    post_data = {
        "id": 1,
        "description": "Some nice description",
        "image_url": "https://somenicewebsite.com/image.jpg",
        "user_id": owner_data["id"]
    }

    mocker.patch('service.like_service.post_service.get', return_value=post_data)
    mocker.patch('service.like_service.like_repository.get', return_value=None)

    like_service.dislike(post_data['id'], user_data)

    like = Like.query.filter_by(post_id=post_data['id'], user_id=user_data['id'], state=False)

    assert like is not None


def test_dislike_post_not_found(mocker):
    user_data = {
        "id": 1
    }

    mocker.patch('service.like_service.post_service.post_repository.get', return_value=None)

    with pytest.raises(NotFoundException):
        like_service.dislike(1, user_data)