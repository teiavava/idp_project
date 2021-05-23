import sys
import os
from http import HTTPStatus
import requests
from flask import Response, request, jsonify

sys.path.append('..\\')


def get_phones():
    body = request.get_json()
    header = request.get_data()

    ret = requests.request("GET",
                           "http://io/api/phones",
                           headers={'Content-Type': 'application/json',
                                    'Authorization': request.headers['Authorization']},
                           data=str(body).replace('\'', '\"'))

    return ret.json(), ret.status_code


def get_phone(id):
    ret = requests.request("GET",
                           "http://io/api/phones/" + str(id),
                           headers={'Content-Type': 'application/json',
                                    'Authorization': request.headers['Authorization']},
                           data='')

    return ret.json(), ret.status_code


def buy_phone(id):
    body = request.get_json()

    # // check the body
    # ret = check_user_put(body)
    name = body.get('name')
    if name is None:
        return str({'error': 'The username is missing.'}), HTTPStatus.BAD_REQUEST

    ret = requests.request("PUT",
                           "http://io/api/phones/buy/" + str(id),
                           headers={'Content-Type': 'application/json',
                                    'Authorization': request.headers['Authorization']},
                           data=str(body).replace('\'', '\"'))

    return ret.json(), ret.status_code
