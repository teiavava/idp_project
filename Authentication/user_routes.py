import sys
import os
from http import HTTPStatus
import requests
from flask import Response, request, jsonify
sys.path.append('..\\')


def get_users():
    ret = requests.request("GET",
                           "http://io/api/users",
                           headers={'Content-Type': 'application/json'},
                           data=str(body).replace('\'', '\"'))

    return ret.json(), ret.status_code


def login_user():
    body = request.get_json()

    ret = requests.request("POST",
                           "http://io/api/users/login",
                           headers={'Content-Type': 'application/json'},
                           data=str(body).replace('\'', '\"'))

    return ret.json(), ret.status_code


def add_user():
    body = request.get_json()

    ret = requests.request("POST",
                           "http://io/api/users",
                           headers={'Content-Type': 'application/json'},
                           data=str(body).replace('\'', '\"'))

    return ret.json(), ret.status_code


def get_user(id):
    ret = requests.request("GET",
                           "http://io/api/users/" + str(id),
                           headers={'Content-Type': 'application/json'},
                           data='')

    return ret.json(), ret.status_code


def update_user(id):
    body = request.get_json()

    ret = requests.request("PUT",
                           "http://io/api/users/" + str(id),
                           headers={'Content-Type': 'application/json'},
                           data=str(body).replace('\'', '\"'))

    return ret.json(), ret.status_code


def delete_user(id):
    ret = requests.request("DELETE",
                           "http://io/api/users/" + str(id),
                           headers={'Content-Type': 'application/json'},
                           data='')

    return ret.json(), ret.status_code
