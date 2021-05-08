import re
from http import HTTPStatus
from coolname import generate_slug

from utils import (user_email_exists, user_exists,
                   user_id_exists, phone_id_exists, phone_exists)

email_regex = r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
password_regex = r'[A-Za-z0-9@#_*!.,/$%^&+=]{4,}'

# #################################################################################################
# USER
# #################################################################################################


def check_user_post(body):
    name = body.get('name')
    password = body.get('password')
    email = body.get('email')

    if name is None:
        return str({'error': 'The username is missing.'}), HTTPStatus.BAD_REQUEST

    if not isinstance(name, str):
        return str({'error': 'The username is invalid.'}), HTTPStatus.BAD_REQUEST

    if user_exists(name):
        return str({'error': 'The username already exists.'}), HTTPStatus.BAD_REQUEST

    if password is None:
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


def check_user_get(id):
    if not user_id_exists(id):
        return str({'error': 'The user id does not exist.'}), HTTPStatus.NOT_FOUND

# #################################################################################################
# PHONE
# #################################################################################################


def check_phone_post(body):
    name = body.get('name')
    stock = body.get('stock')
    price = body.get('price')

    if name is None:
        return str({'error': 'The phone name is missing.'}), HTTPStatus.BAD_REQUEST

    if phone_exists(name):
        return str({'error': 'This phone already exist.'}), HTTPStatus.BAD_REQUEST

    if not isinstance(name, str):
        return str({'error': 'The username is invalid.'}), HTTPStatus.BAD_REQUEST

    if price is None:
        return str({'error': 'The price is missing.'}), HTTPStatus.BAD_REQUEST

    if ((not isinstance(price, int)) and (price)) or (price < 0):
        return str({'error': 'The price is invalid.'}), HTTPStatus.BAD_REQUEST

    if stock is None:
        return str({'error': 'The stock is missing.'}), HTTPStatus.BAD_REQUEST

    if ((not isinstance(stock, int)) and (stock)) or (stock < 0):
        return str({'error': 'The stock is invalid.'}), HTTPStatus.BAD_REQUEST

    return None


def check_phone_put(body, id):
    name = body.get('name')
    stock = body.get('stock')
    price = body.get('price')

    if not phone_id_exists(id):
        return str({'error': 'The user id does not exist.'}), HTTPStatus.NOT_FOUND

    if not isinstance(name, str):
        return str({'error': 'The username is invalid.'}), HTTPStatus.BAD_REQUEST

    if (not isinstance(price, int)) or (price < 0):
        return str({'error': 'The price is invalid.'}), HTTPStatus.BAD_REQUEST

    if (not isinstance(stock, int)) or (stock < 0):
        return str({'error': 'The stock is invalid.'}), HTTPStatus.BAD_REQUEST

    return None


def check_phone_buy(body, id):
    name = body.get('username')

    if not phone_id_exists(id):
        return str({'error': 'The phone id does not exist.'}), HTTPStatus.NOT_FOUND

    if not user_exists(name):
        return str({'error': 'The username does not exist.'}), HTTPStatus.BAD_REQUEST

    return None


def check_phone_get(id):
    if not phone_id_exists(id):
        return str({'error': 'The phone id does not exist.'}), HTTPStatus.NOT_FOUND
