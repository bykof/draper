

class Settings:
    def __init__(self, **kwargs):
        self.DATABASE_NAME = 'draper'
        self.DATABASE_HOST = 'localhost'
        self.DATABASE_PORT = 27017

        for key, value in kwargs.items():
            setattr(self, key, value)
