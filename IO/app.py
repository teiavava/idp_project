import os
from datetime import timedelta
from http import HTTPStatus

from flask.json import JSONEncoder
import datetime

from flask import Flask, request
from flask_cors import CORS
from flask_jwt import JWT, jwt_required, current_identity

import routes.user_routes
import routes.phone_routes

from db import initialize_db
from security.security import (
    authenticate,
    identity,
    is_not_admin,
    is_token_stolen
    )


app = Flask(__name__)

cors = CORS(app, resources={r"/io/*": {"origins": "*"}})

app.secret_key = 'hiiamyoursecret'

app.config['JWT_EXPIRATION_DELTA'] = timedelta(seconds=36000)

jwt = JWT(app, authenticate, identity)

DB_URL = "mongodb+srv://teia:portocala01@clusterteia.esisk.mongodb.net"

app.config['MONGODB_SETTINGS'] = [
    {
        'ALIAS': 'phones-user-db-alias',
        'host': DB_URL + "/IDP"
    },
    {
        'ALIAS': 'phones-phone-db-alias',
        'host': DB_URL + "/IDP"
    }
]

# app.config['MONGODB_SETTINGS'] = {
#     'db': 'db',
#     'host': 'mongodb',
#     'port': 27017
# }

initialize_db(app)


# #################################################################################################
# USERS
# #################################################################################################


@app.route('/api/users/<id>', methods=['GET'])
@jwt_required()
def get_user(id):
    if is_token_stolen(id):
        return {"error": "The authorization token does not belong to you."}, HTTPStatus.UNAUTHORIZED
    return routes.user_routes.get_user(id)


@app.route('/api/users', methods=['GET'])
@jwt_required()
def get_users():
    ret = is_not_admin()
    if ret:
        return ret
    return routes.user_routes.get_users()


@app.route('/api/users/login', methods=['POST'])
def login_user():
    return routes.user_routes.login_user()


@app.route('/api/users', methods=['POST'])
def add_user():
    return routes.user_routes.add_user()


@app.route('/api/users/<id>', methods=['PUT'])
@jwt_required()
def update_user(id):
    if is_token_stolen(id):
        return {"error": "The authorization token does not belong to you."}, HTTPStatus.UNAUTHORIZED

    return routes.user_routes.update_user(id)


@app.route('/api/users/<id>', methods=['DELETE'])
@jwt_required()
def delete_user(id):
    if is_token_stolen(id):
        return {"error": "The authorization token does not belong to you."}, HTTPStatus.UNAUTHORIZED

    return routes.user_routes.delete_user(id)


# #################################################################################################
# PHONES-ADMIN
# #################################################################################################


@app.route('/api/phones/<id>', methods=['GET'])
@jwt_required()
def get_phone(id):
    return routes.phone_routes.get_phone(id)


@app.route('/api/phones', methods=['GET'])
@jwt_required()
def get_phones():
    return routes.phone_routes.get_phones()


@app.route('/api/phones', methods=['POST'])
@jwt_required()
def add_phone():
    ret = is_not_admin()
    if ret:
        return ret
    return routes.phone_routes.add_phone()


@app.route('/api/phones/<id>', methods=['PUT'])
@jwt_required()
def update_phone(id):
    ret = is_not_admin()
    if ret:
        return ret
    return routes.phone_routes.update_phone(id)


@app.route('/api/phones/<id>', methods=['DELETE'])
@jwt_required()
def delete_phone(id):
    ret = is_not_admin()
    if ret:
        return ret
    return routes.phone_routes.delete_phone(id)


@app.route('/api/phones/buy/<id>', methods=['PUT'])
@jwt_required()
def buy_phone(id):
    return routes.phone_routes.buy_phone(id)


if __name__ == '__main__':
    ENVIRONMENT_DEBUG = os.environ.get("APP_DEBUG", True)
    ENVIRONMENT_PORT = os.environ.get("APP_PORT", 80)
    app.run(host='0.0.0.0', port=80, debug=ENVIRONMENT_DEBUG)
