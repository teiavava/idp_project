import os
from datetime import timedelta
from http import HTTPStatus

from flask.json import JSONEncoder

from flask import Flask, request
from flask_cors import CORS

import phones_routes


app = Flask(__name__)

CORS(app, resources={r"/api/*": {"origins": "*"}})

app.secret_key = 'hiiamyoursecret'

@app.route('/api/phones', methods=['GET'])
def get_phones():
    return phones_routes.get_phones()


@app.route('/api/phones/<id>', methods=['GET'])
def get_phone(id):
    return phones_routes.get_phone(id)


@app.route('/api/phones/<id>', methods=['PUT'])
def buy_phone(id):
    return phones_routes.buy_phone(id)


if __name__ == '__main__':
    ENVIRONMENT_DEBUG = os.environ.get("APP_DEBUG", True)
    app.run(host='0.0.0.0', port=5000, debug=ENVIRONMENT_DEBUG)
