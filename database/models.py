from db import db


class Movie(db.Document):

    # pylint: disable=no-member
    name = db.StringField(required=True, unique=True)
    casts = db.ListField(db.StringField(), required=True)
    genres = db.ListField(db.StringField(), required=True)
