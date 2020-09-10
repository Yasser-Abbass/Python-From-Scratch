import flask_mongoengine as db
from mongoengine import *


class Subscriber(db.Document):
    name = StringField(required=True)
    phone = StringField(required=True)
    email = EmailField(required=True)
    address = StringField()

    meta = {
        'indexes': [
            'email',
            'phone'
        ]
    }

    def __str__(self):
        return self.name