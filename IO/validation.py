import re
from http import HTTPStatus
from coolname import generate_slug

from utils import (user_email_exists, user_exists, user_id_exists)

email_regex = r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
password_regex = r'[A-Za-z0-9@#_*!.,/$%^&+=]{4,}'

# #################################################################################################
# USER
# #################################################################################################


def check_user_post(body):
    name = body.get('name')
    password = body.get('password')
    email = body.get('email')

    if not name:
        return str({'error': 'The username is missing.'}), HTTPStatus.BAD_REQUEST

    if not isinstance(name, str):
        return str({'error': 'The username is invalid.'}), HTTPStatus.BAD_REQUEST

    if user_exists(name):
        return str({'error': 'The username already exists.'}), HTTPStatus.BAD_REQUEST

    if not password:
        return str({'error': 'The password is missing.'}), HTTPStatus.BAD_REQUEST

    if (not isinstance(password, str)) or (not re.fullmatch(password_regex, password)):
        return str({'error': 'The password format is invalid. It must contain at least 8 symbols.'}), HTTPStatus.BAD_REQUEST

    if not email:
        return str({'error': 'The email address is missing.'}), HTTPStatus.BAD_REQUEST

    if (not isinstance(email, str)) or (not re.search(email_regex, email)):
        return str({'error': 'The email format is invalid.'}), HTTPStatus.BAD_REQUEST

    if user_email_exists(email):
        return str({'error': 'The email was already associated with another account.'}), HTTPStatus.BAD_REQUEST

    return None


def check_user_put(body, id):
    if not user_id_exists(id):
        return str({'error': 'The user id does not exist.'}), HTTPStatus.NOT_FOUND

    password = body.get('password')

    if (not isinstance(password, str)) or (not re.fullmatch(password_regex, password)):
        return str({'error': 'The password format is invalid. It must contain at least 8 symbols.'}), HTTPStatus.BAD_REQUEST

    return None
