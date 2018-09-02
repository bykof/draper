from draper.db.fields.exceptions.not_valid_value_exception import NotValidValue
from abs import ABCMeta

class Field(metaclass=ABCMeta):

    def __init__(self):
        self.value = None

    @staticmethod
    def serialize(self):
        return self.value

    def deserialize(self):
        return self.value

    @abstractmethod
    def to_python(self):
        raise NotImplemented("Implement the value returned in Python enviroment to current field.")

    @staticmethod
    def is_valid(value):
        return True

    def __set__(self, instance, value):
        if self.is_valid(value):
            self.value = value
        else:
            raise NotValidValue(self.__class__, value)

    def __get__(self, instance, owner):
        return self.value
