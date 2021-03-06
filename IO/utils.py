from models.phones import Phone
from models.user import User
from http import HTTPStatus
import uuid
import datetime
import json


# #################################################################################################
# USERS
# #################################################################################################

"""
Generate new unique id for the newly-created user/device/sensor/data.
Returns: hex
"""


def get_new_id():
    return uuid.uuid4().hex


"""
Checks if the user with the name <name>
exists in the database.
Returns: bool
"""


def user_exists(username):
    return len(User.objects.filter(name=username)) != 0


"""
Checks if the user with the id <_id>
exists in the database.
Returns: bool
"""


def user_id_exists(_id):
    return len(User.objects.filter(id=_id)) != 0


"""
Checks if the user with the email <email>
exists in the database.
Returns: bool
"""


def user_email_exists(email):
    return len(User.objects.filter(email=email)) != 0


"""
Checks if the phone with the name <phone_name> 
exists in the database.
Returns: bool
"""


def phone_exists(username):
    return len(Phone.objects.filter(name=username)) != 0


"""
Checks if the user with the id <_id>
exists in the database.
Returns: bool
"""


def phone_id_exists(_id):
    return len(Phone.objects.filter(id=_id)) != 0


"""
Gen the user with the id <_id>.
If the id does not exist in the database, return None.
Returns: User or None
"""


def get_user_by_id(_id):
    if user_id_exists(_id):
        return User.objects.filter(id=_id)[0]
    else:
        return None
