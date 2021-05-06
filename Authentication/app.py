import os
from datetime import timedelta
from http import HTTPStatus

from flask.json import JSONEncoder

from flask import Flask, request
from flask_cors import CORS

import user_routes


app = Flask(__name__)

cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

app.secret_key = 'hiiamyoursecret'


@app.route('/api/users/<id>', methods=['GET'])
def get_user(id):
    return routes.user_routes.get_user(id)


@app.route('/api/users', methods=['GET'])
def get_users():
    return routes.user_routes.get_users()


@app.route('/api/users/login', methods=['POST'])
def login_user():
    return routes.user_routes.login_user()


@app.route('/api/users', methods=['POST'])
def add_user():
    return routes.user_routes.add_user()


@app.route('/api/users/<id>', methods=['PUT'])
def update_user(id):
    return routes.user_routes.update_user(id)


@app.route('/api/users/<id>', methods=['DELETE'])
def delete_user(id):
    return routes.user_routes.delete_user(id)


if __name__ == '__main__':
    ENVIRONMENT_DEBUG = os.environ.get("APP_DEBUG", True)
    ENVIRONMENT_PORT = os.environ.get("APP_PORT", 5001)
    app.run(host='0.0.0.0', port=5001, debug=ENVIRONMENT_DEBUG)
