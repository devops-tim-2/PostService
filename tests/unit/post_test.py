from exception.exceptions import InvalidDataException, NotFoundException
from models.models import Post, User
from service import post_service
import pytest


def test_create_ok(mocker):
    data = {
        "description": "Some nice description",
        "image_url": "https://somenicewebsite.com/image.jpg"
    }

    user = {
        'id': 1
    }
    
    expected = Post(**data, user_id=user['id'])

    mocker.patch('service.post_service.post_repository.create', return_value=expected)

    actual = post_service.create(data, user)

    assert expected.get_dict()==actual


def test_create_empty_value():
    data = {
        "description": "Some nice description 2",
        "image_url": ""
    }

    user = {
        'id': 2
    }

    with pytest.raises(InvalidDataException) as e:
        post_service.create(data, user)


def test_get_ok(mocker):
    data = {
        "id": 1,
        "description": "Some nice description",
        "image_url": "https://somenicewebsite.com/image.jpg",
        "user_id": 1
    }

    user_data = {
        'id': 1,
        'public': True
    }
    
    expected = Post(**data)
    user = User(**user_data)

    mocker.patch('service.post_service.post_repository.get', return_value=expected)
    mocker.patch('service.post_service.user_service.get', return_value=user)

    actual = post_service.get(data['id'], user_data)

    
    for i in expected.get_dict():
        assert expected.get_dict()[i] == actual[i]


def test_get_not_found(mocker):
    user = {
        'id': 1
    }

    mocker.patch('service.post_service.post_repository.get', return_value=None)

    with pytest.raises(NotFoundException) as e:
        post_service.get(1, user)


def test_get_users_posts_ok(mocker):
    profile_data = {
        "id": 1,
        "public": True
    }

    user_data = {
        "id": 2
    }

    profile = User(**profile_data)
    expected = [Post(id=1, description='post list description 1', image_url='post list image url 1', user_id=profile_data['id']), Post(id=2, description='post list description 2', image_url='post list image url 2', user_id=profile_data['id'])]

    mocker.patch('service.post_service.user_service.get', return_value=profile)
    mocker.patch('service.post_service.block_service.find', return_value=False)
    mocker.patch('service.post_service.post_repository.get_users_posts', return_value=expected)

    actual = post_service.get_users_posts(profile_data['id'], user_data)
    expected = [post.get_dict() for post in expected]

    assert len(actual) == len(expected)



def test_get_users_posts_with_block(mocker):
    profile_data = {
        "id": 1,
        "public": True
    }

    user_data = {
        "id": 2
    }

    profile = User(**profile_data)
    
    mocker.patch('service.post_service.user_service.get', return_value=profile)
    mocker.patch('service.post_service.block_service.find', return_value=True)
    
    with pytest.raises(NotFoundException) as e:
        post_service.get_users_posts(profile_data['id'], user_data)
