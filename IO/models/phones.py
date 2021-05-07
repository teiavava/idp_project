import datetime

from db import db
from mongoengine import StringField, FloatField


class Phone(db.Document):
    id = StringField(primary_key=True)
    name = StringField(required=True, unique=True, max_length=50)
    price = FloatField(required=False, default=0)
    stock = FloatField(required=False, default=0)

    meta = {'db_alias': 'phones-phone-db-alias'}
