import sys
import os
from http import HTTPStatus
import requests
from flask import Response, request, jsonify

sys.path.append('..\\')


def get_phones():
    ret = requests.request("GET",
                           "http://io/api/phones",
                           headers={'Content-Type': 'application/json'},
                           data=str(body).replace('\'', '\"'))

    return ret.json(), ret.status_code


def add_phone():
    body = request.get_json()

    ret = requests.request("POST",
                           "http://io/api/phones",
                           headers={'Content-Type': 'application/json'},
                           data=str(body).replace('\'', '\"'))

    return ret.json(), ret.status_code


def get_phone(id):
    ret = requests.request("GET",
                           "http://io/api/phones/" + str(id),
                           headers={'Content-Type': 'application/json'},
                           data='')

    return ret.json(), ret.status_code


def update_phone(id):
    body = request.get_json()

    ret = requests.request("PUT",
                           "http://io/api/phones/" + str(id),
                           headers={'Content-Type': 'application/json'},
                           data=str(body).replace('\'', '\"'))

    return ret.json(), ret.status_code


def delete_phone(id):
    ret = requests.request("DELETE",
                           "http://io/api/phones/" + str(id),
                           headers={'Content-Type': 'application/json'},
                           data='')

    return ret.json(), ret.status_code
