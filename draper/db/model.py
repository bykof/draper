

class Model:

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def serialize(self):
        pass

    def deserialize(self, data):
        pass

    def save(self):
        pass

    def create(self):
        pass

    def update(self):
        pass

    def delete(self):
        pass
