from draper.db.fields import Field


class StringField(Field):
    @staticmethod
    def value_is_valid(value):
        return isinstance(value, str)
