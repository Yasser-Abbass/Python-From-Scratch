from mongoengine import *


class Publisher(Document):
    name = StringField()
    founded = DateField()
    location = StringField()

    meta = {
        'index': 'name'
    }