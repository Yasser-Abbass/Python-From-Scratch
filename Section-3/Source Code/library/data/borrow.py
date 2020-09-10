from mongoengine import *
from data.subscriber import Subscriber


class Borrow(EmbeddedDocument):
    subscriber = ReferenceField(Subscriber)
    start = DateField()
    end = DateField()

