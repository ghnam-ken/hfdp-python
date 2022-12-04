from dataclasses import dataclass
from typing import List

from .base import Subject, Observer

DEFAULT_VALUE = float('nan')


@dataclass
class Data:
    temperature: float = DEFAULT_VALUE
    humidity: float = DEFAULT_VALUE
    pressure: float = DEFAULT_VALUE


class WeatherData(Subject):
    def __init__(self):
        self._observers: List[Observer] = []
        self._data = Data()

    def register_observer(self, observer: Observer):
        self._observers.append(observer)

    def remove_observer(self, observer: Observer):
        self._observers.remove(observer)

    def notify_observers(self):
        for observer in self._observers:
            observer.update(self._data)

    def measurements_changed(self):
        self.notify_observers()

    def set_measurements(self, data: Data):
        self._data = data
        self.measurements_changed()
