import flask_mongoengine as db
from mongoengine import *


class Subscriber(db.Document):
    first_name = StringField(required=True, max_length=50)
    last_name = StringField(required=True, max_length=50)
    email = EmailField(unique=True)
    address = StringField(max_length=255)
    ssn = StringField()

    meta = {
        'indexes': [
            'first_name',
            'last_name',
            'email',
            'address',
            'ssn',
        ]
    }