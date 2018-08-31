

class NotValidValue(Exception):
    def __init__(self, field, value):
        self.field = field
        self.value = value

    def __str__(self):
        return f'Value for field {self.field.__name__} is not valid'
