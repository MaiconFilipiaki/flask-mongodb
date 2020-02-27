from .db import db


class User(db.Document):
    name = db.StringField(required=True)
    email = db.EmailField(required=True)
    password = db.StringField(required=True)


class Movie(db.Document):
    name = db.StringField()
    user = db.ReferenceField('User')
