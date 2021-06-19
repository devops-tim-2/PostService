from werkzeug import datastructures
from common.result import Result
from models.user import User
from os import environ
from services import user_service
from datetime import datetime
import jwt


def check(obj: dict) -> bool:
    return not obj or any(prop is None or ((type(prop) is list or type(prop) is str) and len(prop) == 0) or ((type(prop) is int or type(prop) is float) and prop < 1) for prop in list(obj.values()))


def auth(headers: datastructures.Headers) -> Result:
    if not headers.has_key('Authorization'):
        return Result('Forbidden, unauthorized atempt.', 403).get_dict()

    token = headers['Authorization'].split(' ')[1]
    try:
        payload = jwt.decode(token, environ.get('JWT_SECRET'), environ.get('JWT_ALGORITHM'))
    except:
        return Result('Forbidden, invalid authentication.', 401).get_dict()

    exp = payload['exp']
    if datetime.now() > datetime.fromtimestamp(exp / 1000.0):
        return Result('Forbidden, authorization token has expired.', 401).get_dict()

    return user_service.get_by_username(payload['username'])
