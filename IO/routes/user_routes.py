import sys
import os
from http import HTTPStatus

from flask import Response, request, jsonify

sys.path.append('..\\')

from http_utils.http_client import Client
from models.user import User
from security.security import encode_password
from utils import get_new_id, user_id_exists
from validation import check_user_post, check_user_put


def get_users():
    users = User.objects()

    return {'users': users}, HTTPStatus.OK


def login_user():
    # import ipdb; ipdb.set_trace()
    body = request.get_json()
    username = body.get('username')
    password = body.get('password')

    encoded_password = encode_password(password)

    users = User.objects.filter(name=username, password=encoded_password)

    if len(users) == 0:
        return str({'error': 'Invalid credentials.'}), HTTPStatus.UNAUTHORIZED

    user = users[0]

    access_token = Client.generate_auth_token(username=username,
                                              password=password)
    if access_token is None:
        return str({'error': 'Something went wrong with the authentication service.'}), HTTPStatus.SERVICE_UNAVAILABLE

    return {
        '_id': user.id,
        'access_token': access_token}, HTTPStatus.CREATED


def add_user():
    body = request.get_json()
    body['name'] = body.get('username')
    del body['username']

    resp = check_user_post(body)

    if resp:
        return resp

    if not body.get('id'):
        body["id"] = get_new_id()

    password = body["password"]
    del body["password"]
    body["password"] = encode_password(password)

    user = User(**body).save()

    access_token = Client.generate_auth_token(username=user.name,
                                              password=password)
    if access_token is None:
        return str({'error': 'Something went wrong with the authentication service.'}), HTTPStatus.SERVICE_UNAVAILABLE

    return {
        '_id': user.id,
        'access_token': access_token}, HTTPStatus.CREATED


def get_user(id):
    user = User.objects.filter(id=id).get(0)

    return {'user': user}, HTTPStatus.OK


def update_user(id):
    body = request.get_json()
    resp = check_user_put(body, id)
    body['name'] = body.get('username')
    del body['username']

    if resp:
        return resp

    password = body.get('password')
    del body["password"]
    body["password"] = encode_password(password)

    User.objects.get(id=id).update(**body)
    return '', HTTPStatus.OK


def delete_user(id):
    if not user_id_exists(id):
        return {'error': 'User id not found.'}, HTTPStatus.NOT_FOUND

    User.objects.get(id=id).delete()
    return '', HTTPStatus.OK
