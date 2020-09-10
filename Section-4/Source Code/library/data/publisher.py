import flask_mongoengine as db
from mongoengine import *


class Publisher(db.Document):
    name = StringField()
    founded = DateField()
    location = StringField()

    meta = {
        'index': 'name'
    }