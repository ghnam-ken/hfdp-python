from abc import abstractmethod

from .base import Observer, DisplayElement
from .weather_data import WeatherData, Data, DEFAULT_VALUE


class Display(Observer, DisplayElement):
    def __init__(self, weather_data: WeatherData):
        self._weather_data = weather_data
        self._weather_data.register_observer(self)
        self._current_data = Data()

    def update(self, data: Data):
        self._current_data = data
        self.display()

    def display(self):
        print(f'[{self.__class__.__name__}]')
        self.display_info()

    @abstractmethod
    def display_info():
        pass

    def __del__(self):
        self._weather_data.remove_observer(self)


class CurrentConditionDisplay(Display):
    def display_info(self):
        print(
            f'- temperature: {self._current_data.temperature}\n'
            f'- humidity: {self._current_data.humidity}\n'
            f'- pressure: {self._current_data.pressure}\n'
        )


class StatisticsDisplay(Display):
    def __init__(self, weather_data: WeatherData):
        super().__init__(weather_data)
        self._temps = []

    def update(self, data: Data):
        self._temps.append(data.temperature)
        super().update(data)

    def display_info(self):
        max_temp = max(self._temps)
        min_temp = min(self._temps)
        avg_temp = sum(self._temps) / len(self._temps)
        print(
            f'- max temperature: {max_temp}\n'
            f'- min temperature: {min_temp}\n'
            f'- avg temperature: {avg_temp}\n'
        )

    def reset(self):
        self._temps = []


class ForecastDisplay(Display):
    def __init__(self, weather_data: WeatherData):
        super().__init__(weather_data)
        self._curr_pressure = DEFAULT_VALUE
        self._prev_pressure = DEFAULT_VALUE

    def update(self, data: Data):
        self._prev_pressure = self._curr_pressure
        self._curr_pressure = data.pressure
        super().update(data)

    def display_info(self):
        if self._curr_pressure > self._prev_pressure:
            print('Improving weather on the way!\n')
        elif self._curr_pressure == self._prev_pressure:
            print('More of the same\n')
        elif self._curr_pressure < self._prev_pressure:
            print('Watch out for cooler, rainy weather\n')
        else:
            print('No forecast available\n')
