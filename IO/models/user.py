import datetime

from db import db
from mongoengine import StringField, EmailField, BooleanField, ListField

class User(db.Document):
    id = StringField(primary_key=True)
    name = StringField(required=True, unique=True, max_length=50)
    password = StringField(required=True, max_length=50)
    email = EmailField(required=True, unique=True, max_length=50)
    role = StringField(required=False, max_length=50, default='user')

    meta = {'db_alias': 'idp-user-db-alias'}
