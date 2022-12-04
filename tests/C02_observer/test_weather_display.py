from typing import Tuple

import pytest

from C02_observer.weather_monitoring.display import (
    CurrentConditionDisplay,
    StatisticsDisplay,
    ForecastDisplay,
)
from C02_observer.weather_monitoring.weather_data import (
    WeatherData,
    Data,
)

DISPLAY_CLASSES = [
    CurrentConditionDisplay,
    StatisticsDisplay,
    ForecastDisplay
]

DATA = [
    Data(temperature=80, humidity=65, pressure=30.4),
    Data(temperature=82, humidity=70, pressure=29.2),
    Data(temperature=78, humidity=90, pressure=29.2),
]

EXPECTED_CURRENT_CONDITION_DISPLAY = [
    "[CurrentConditionDisplay]\n"
    "- temperature: 80\n"
    "- humidity: 65\n"
    "- pressure: 30.4\n",

    "[CurrentConditionDisplay]\n"
    "- temperature: 82\n"
    "- humidity: 70\n"
    "- pressure: 29.2\n",

    "[CurrentConditionDisplay]\n"
    "- temperature: 78\n"
    "- humidity: 90\n"
    "- pressure: 29.2\n",
]

EXPECTED_STATISTICS_DISPLAY = [
    "[StatisticsDisplay]\n"
    "- max temperature: 80\n"
    "- min temperature: 80\n"
    "- avg temperature: 80.0\n",

    "[StatisticsDisplay]\n"
    "- max temperature: 82\n"
    "- min temperature: 80\n"
    "- avg temperature: 81.0\n",

    "[StatisticsDisplay]\n"
    "- max temperature: 82\n"
    "- min temperature: 78\n"
    "- avg temperature: 80.0\n",
]

EXPECTED_FORECAST_DISPLAY = [
    "[ForecastDisplay]\n"
    "No forecast available\n",

    "[ForecastDisplay]\n"
    "Watch out for cooler, rainy weather\n",

    "[ForecastDisplay]\n"
    "More of the same\n",
]

TASK = zip(
    DATA,
    EXPECTED_CURRENT_CONDITION_DISPLAY,
    EXPECTED_STATISTICS_DISPLAY,
    EXPECTED_FORECAST_DISPLAY
)


@pytest.fixture(scope='module')
def weather_data() -> WeatherData:
    weather_data = WeatherData()
    for display_cls in DISPLAY_CLASSES:
        display_cls(weather_data)
    return weather_data


@pytest.fixture(params=TASK)
def task(request) -> Data:
    return request.param


def test_display(weather_data: WeatherData, task: Tuple[Data, ...], capsys):
    data = task[0]
    weather_data.set_measurements(data)
    captured = capsys.readouterr()
    for expected in task[1:]:
        assert expected in captured.out
