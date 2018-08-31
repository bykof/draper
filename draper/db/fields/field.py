from draper.db.fields.exceptions.not_valid_value_exception import NotValidValue


class Field:
    def __init__(self):
        self.value = None

    @staticmethod
    def serialize(self):
        return self.value

    def deserialize(self):
        return self.value

    @staticmethod
    def value_is_valid(value):
        return True

    def __set__(self, instance, value):
        if self.value_is_valid(value):
            self.value = value
        else:
            raise NotValidValue(self.__class__, value)

    def __get__(self, instance, owner):
        return self.value
