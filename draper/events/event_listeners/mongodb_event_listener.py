from mongoengine import connect

from draper.events.event_listener import EventListener
from draper import draper


class MongoDBEventListener(EventListener):
    def listen(self):
        connection = connect(draper.draper.settings.DATABASE_NAME)
        connection.watch()
