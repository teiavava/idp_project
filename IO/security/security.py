import hashlib
import os
from flask_jwt import current_identity
from http import HTTPStatus

from models.user import User


def authenticate(username, password):
    print(username)
    #check for user and return
    return User.objects.filter(name=username, password=encode_password(password)).get(0)


#payload is the contents of the jwt token
def identity(payload):
    userid = payload['identity']
    return User.objects.filter(id=userid).get(0)


def encode_password(password):
    return str(hashlib.md5((password + 'IoTIC Really Rocks!!!!').encode()).hexdigest())


def is_not_admin():
    if not current_identity.role == 'admin':
        return {"error": "You must provide the admin authorization token."}, HTTPStatus.UNAUTHORIZED



def is_token_stolen(id_user):
    if not current_identity.id == id_user:
        return True