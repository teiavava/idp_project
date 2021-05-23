import os
from datetime import timedelta
from http import HTTPStatus

from flask.json import JSONEncoder

from flask import Flask, request
from flask_cors import CORS

import admin_routes


app = Flask(__name__)

CORS(app, resources={r"/api/*": {"origins": "*"}})

app.secret_key = 'hiiamyoursecret'

@app.route('/api/phones', methods=['GET'])
def get_phones():
    return admin_routes.get_phones()

@app.route('/api/phones', methods=['POST'])
def add_phone():
    return admin_routes.add_phone()


@app.route('/api/phones/<id>', methods=['PUT'])
def update_phone(id):
    return admin_routes.update_phone(id)


@app.route('/api/phones/<id>', methods=['DELETE'])
def delete_phone(id):
    return admin_routes.delete_phone(id)



if __name__ == '__main__':
    ENVIRONMENT_DEBUG = os.environ.get("APP_DEBUG", True)
    app.run(host='0.0.0.0', port=80, debug=ENVIRONMENT_DEBUG)
