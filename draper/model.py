import re
from abc import ABCMeta

from draper import Field
from draper.utils import classproperty


class Model(metaclass=ABCMeta):
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            if key in self.__class__.__dict__.keys() and issubclass(self.__class__.__dict__[key], Field):
                self.__class__.__dict__[key].value = value

    def __getattribute__(self, item):
        attribute = object.__getattribute__(self, item)
        if issubclass(attribute, Field):
            return attribute.value
        return attribute

    def __setattr__(self, key, value):
        pass


    @classproperty
    def underscore_name(cls):
        s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', cls.__name__)
        return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()
