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


class HeatIndexDisplay(Display):
    def display_info(self):
        t = self._current_data.temperature
        rh = self._current_data.humidity
        index = self.compute_heat_index(t, rh)
        print(f'Heat index: {index:.2f}\n')

    def compute_heat_index(self, t, rh):
        return (
            (
                16.923 + (0.185212 * t) + (5.37941 * rh) - (0.100254 * t * rh)
                + (0.00941695 * (t * t)) + (0.00728898 * (rh * rh))
                + (0.000345372 * (t * t * rh)) - (0.000814971 * (t * rh * rh))
                + (0.0000102102 * (t * t * rh * rh)) - (0.000038646 * (t * t * t))
                + (0.0000291583 * (rh * rh * rh)) + (0.00000142721 * (t * t * t * rh))
                + (0.000000197483 * (t * rh * rh * rh))
                - (0.0000000218429 * (t * t * t * rh * rh))
                + 0.000000000843296 * (t * t * rh * rh * rh)
            )
            - (0.0000000000481975 * (t * t * t * rh * rh * rh))
        )
