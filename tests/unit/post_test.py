from exception.exceptions import InvalidDataException
from models.models import Post
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
