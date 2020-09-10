from mongoengine import *
from data.grade import Grade


class Student(Document):
    first_name = StringField(required=True, max_length=50)
    last_name = StringField(required=True, max_length=50)
    email = EmailField(unique=True)
    degree = EmbeddedDocumentListField(Grade)

    meta = {
        'indexes': [
            'first_name',
            'last_name',
            'email'
        ]
    }

    def __str__(self):
        return self.first_name + " " + self.last_name
