from mongoengine import Document, EmbeddedDocument, EmbeddedDocumentListField, EmbeddedDocumentField, StringField, IntField, DateTimeField
from datetime import datetime

class Time(EmbeddedDocument):
    hrs = IntField(required=True)
    min = IntField(required=True)

class Forcast(EmbeddedDocument):
    time = EmbeddedDocumentField(Time, required=True)
    temp = IntField(required = True)
    condition = StringField(required = True)

class Weather(Document):
    location = StringField(required = True)
    date = DateTimeField()
    forcast = EmbeddedDocumentListField(Forcast)

    meta={
        "collection": "weather"
    }
