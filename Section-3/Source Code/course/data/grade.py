from mongoengine import *


class Grade(EmbeddedDocument):
    course = ReferenceField('Course')
    grade = FloatField()
