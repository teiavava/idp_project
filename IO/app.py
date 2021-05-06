import os
from datetime import timedelta
from http import HTTPStatus

from flask.json import JSONEncoder
import datetime

from flask import Flask, request
from flask_cors import CORS
from flask_jwt import JWT, jwt_required, current_identity

import routes.user_routes

from db import initialize_db
from security.security import (
    authenticate,
    identity,
    is_not_admin,
    is_token_stolen
    )


app = Flask(__name__)

cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

app.secret_key = 'hiiamyoursecret'

app.config['JWT_EXPIRATION_DELTA'] = timedelta(seconds=36000)

jwt = JWT(app, authenticate, identity)

DB_URL = "mongodb+srv://teia:portocala01@clusterteia.esisk.mongodb.net"

app.config['MONGODB_SETTINGS'] = [
    {
        'ALIAS': 'idp-user-db-alias',
        'host': DB_URL + "/idp-user"
    }
]

initialize_db(app)


@app.route('/api/health')
# @jwt_required()
def health_check():
    return {'message': 'Healthy'}, HTTPStatus.OK


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
# @check_admin_credentials
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


if __name__ == '__main__':
    ENVIRONMENT_DEBUG = os.environ.get("APP_DEBUG", True)
    ENVIRONMENT_PORT = os.environ.get("APP_PORT", 80)
    app.run(host='0.0.0.0', port=80, debug=ENVIRONMENT_DEBUG)
