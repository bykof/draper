from mongoengine import Document


class Model(Document):
    meta = {
        'abstract': True,
    }

