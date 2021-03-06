from mongoengine import *
from data.borrow import Borrow
from data.publisher import Publisher
import datetime


class Book(Document):
    title = StringField(required=True, max_length=255)
    author = ListField(StringField())
    pages = IntField()
    publish_date = DateField(default=datetime.datetime.today)
    publisher = ReferenceField(Publisher, reverse_delete_rule=CASCADE)
    borrowing_history = EmbeddedDocumentListField(Borrow)

    meta = {
        'indexes': [
            'title',
            'author'
    ]
    }
