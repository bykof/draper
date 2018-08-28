import re
from abc import ABCMeta

import rethinkdb
from rethinkdb.ast import Table

from draper import draper
from draper import fields
from draper.object_set import ObjectSet
from draper.utils import classproperty


class Model(metaclass=ABCMeta):

    id = fields.Field()

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            class_dict = self.__class__.__dict__

            if (
                key in class_dict.keys() and
                isinstance(class_dict[key], fields.Field)
            ):
                class_dict[key].value = value

    def __getattribute__(self, item):
        attribute = object.__getattribute__(self, item)

        if isinstance(attribute, fields.Field):
            return attribute.value
        return attribute

    def __setattr__(self, key, value):
        if key in self.__dict__ and isinstance(object.__getattribute__(self, key), fields.Field):
            object.__getattribute__(self, key).value = value
        else:
            object.__setattr__(self, key, value)

    @classproperty
    def objects(cls):
        return ObjectSet(cls)

    @classproperty
    def underscore_name(cls):
        s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', cls.__name__)
        return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()

    @classproperty
    def table_name(cls):
        return f'{cls.underscore_name}s'

    @classproperty
    def table(cls) -> Table:
        return rethinkdb.db(draper.draper.settings.DATABASE_NAME).table(cls.table_name)

    def to_dict(self):
        return_dict = {}

        for key, value in self.__class__.__dict__.items():
            if isinstance(value, fields.Field) and key != 'id':
                return_dict[key] = value.value
        return return_dict

    def create(self):
        result = self.table.insert(self.to_dict()).run()
        self.id = result['generated_keys'][0]

    def update(self):
        self.table.get(self.id).update(self.to_dict()).run()

    def save(self):
        if self.id:
            self.update()
        else:
            self.create()

    def delete(self):
        self.table.get(self.id).update(self.to_dict()).run()
