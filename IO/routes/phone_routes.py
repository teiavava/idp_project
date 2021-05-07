import sys
import os
from http import HTTPStatus

from flask import Response, request, jsonify

sys.path.append('..\\')

from http_utils.http_client import Client
from models.phones import Phone
from utils import get_new_id, phone_id_exists


def get_phones():
    phones = Phone.objects()
    return {'phones': phones}, HTTPStatus.OK


def add_phone():
    body = request.get_json()

    if not body.get('id'):
        body["id"] = get_new_id()

    phone = Phone(**body).save()
    return {'id': phone.id}, HTTPStatus.CREATED


def get_phone(id):
    phone = Phone.objects.filter(id=id).get(0)
    return {'phone': phone}, HTTPStatus.OK


def update_phone(id):
    body = request.get_json()

    Phone.objects.get(id=id).update(**body)
    return '', HTTPStatus.OK


def delete_phone(id):
    if not phone_id_exists(id):
        return {'error': 'Phone id not found.'}, HTTPStatus.NOT_FOUND

    Phone.objects.get(id=id).delete()
    return '', HTTPStatus.OK
