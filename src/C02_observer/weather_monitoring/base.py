from abc import ABCMeta, abstractmethod


class Observer(metaclass=ABCMeta):
    @abstractmethod
    def update(self, data: object):
        pass


class Subject(metaclass=ABCMeta):
    @abstractmethod
    def register_observer(self, observer: Observer):
        pass

    @abstractmethod
    def remove_observer(self, observer: Observer):
        pass

    @abstractmethod
    def notify_observers(self):
        pass


class DisplayElement(metaclass=ABCMeta):
    @abstractmethod
    def display(self):
        pass
