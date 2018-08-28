

class Field:
    def __init__(self, default=None):
        self.__value = default

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        self.__value = value
