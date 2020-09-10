from mongoengine import *
from data.student import Student


class Course(Document):
    name = StringField(required=True, max_length=255)
    max_students = IntField(min_value=10, max_value=40)
    students = ListField(ReferenceField(Student))

    meta = {
        'index': 'name'
    }

    def __str__(self):
        return self.name