from utils import get_new_id, phone_id_exists
from models.user import User
from models.phones import Phone
from http_utils.http_client import Client
import sys
import os
from http import HTTPStatus
from validation import check_phone_post, check_phone_put, check_phone_buy
from flask import Response, request, jsonify

sys.path.append('..\\')


def get_phones():
    phones = Phone.objects()
    return {'phones': phones}, HTTPStatus.OK


def add_phone():
    body = request.get_json()
    resp = check_phone_post(body)

    if resp:
        return resp

    if not body.get('id'):
        body["id"] = get_new_id()

    phone = Phone(**body).save()
    return {'id': phone.id}, HTTPStatus.CREATED


def get_phone(id):
    phone = Phone.objects.filter(id=id).get(0)

    return {'phone': phone}, HTTPStatus.OK


def update_phone(id):
    body = request.get_json()
    resp = check_phone_put(body, id)

    if resp:
        return resp

    Phone.objects.get(id=id).update(**body)
    return 'The phone informations were updated.', HTTPStatus.OK


def delete_phone(id):
    if not phone_id_exists(id):
        return {'error': 'Phone id not found.'}, HTTPStatus.NOT_FOUND

    Phone.objects.get(id=id).delete()
    return '', HTTPStatus.OK


def buy_phone(id):
    body = request.get_json()
    username = body.get("username")

    resp = check_phone_buy(body, id)
    if resp:
        return resp

    phone = Phone.objects.filter(id=id).get(0)
    stock = phone.stock

    user = User.objects.filter(name=username).get(0)
    cash = user.cash

    if cash < phone.price:
        return {'error': 'Too expensive.'}, HTTPStatus.NOT_FOUND
    else:
        cash -= phone.price

    if stock == 0:
        return {'error': 'Empty stock.'}, HTTPStatus.NOT_FOUND
    else:
        stock -= 1

    new_stock = {'stock': stock}
    Phone.objects.get(id=id).update(**new_stock)

    new_cash = {'cash': cash}
    user = User.objects.get(name=username).update(**new_cash)

    return {'phone': Phone.objects.filter(id=id).get(0)}, HTTPStatus.OK
