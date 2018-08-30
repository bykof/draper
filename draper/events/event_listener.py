from abc import ABCMeta, abstractmethod


class EventListener(metaclass=ABCMeta):

    @abstractmethod
    def listen(self):
        pass

    def start_as_thread(self):
        pass

    def start_as_process(self):
        pass
