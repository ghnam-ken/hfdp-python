from typing import Type

import pytest

from C03_decorator.starbuzz.base import Beverage, CondimentDecorator
from C03_decorator.starbuzz.beverage import Espresso, HouseBlend
from C03_decorator.starbuzz.condiment import Mocha, Whip, Soy


BEVERAGE_LIST = [Espresso, HouseBlend]

CONDIMENT_LIST = [Mocha, Whip, Soy]


def check_price(
    beverage: Beverage,
    beverage_cls: Type[Beverage],
    condiment_cls: Type[CondimentDecorator] = None,
    second_condiment_cls: Type[CondimentDecorator] = None
):
    intermediate_beverage = beverage_cls()
    price = intermediate_beverage.price
    if condiment_cls:
        intermediate_beverage = condiment_cls(intermediate_beverage)
        price += intermediate_beverage.price
    if second_condiment_cls:
        intermediate_beverage = second_condiment_cls(intermediate_beverage)
        price += intermediate_beverage.price
    assert beverage.cost() == price


def check_description(
    beverage: Beverage,
    beverage_cls: Type[Beverage],
    condiment_cls: Type[CondimentDecorator] = None,
    second_condiment_cls: Type[CondimentDecorator] = None
):
    intermediate_beverage = beverage_cls()
    descriptions = [intermediate_beverage.description]
    if condiment_cls:
        intermediate_beverage = condiment_cls(intermediate_beverage)
        descriptions.append(intermediate_beverage.description)
    if second_condiment_cls:
        intermediate_beverage = second_condiment_cls(intermediate_beverage)
        descriptions.append(intermediate_beverage.description)
    descriptions.reverse()
    assert beverage.get_description() == " ".join(descriptions)


@pytest.fixture(params=BEVERAGE_LIST)
def beverage_cls(request):
    return request.param


@pytest.fixture(params=CONDIMENT_LIST)
def condiment_cls(request):
    return request.param


@pytest.fixture(params=CONDIMENT_LIST)
def second_condiment_cls(request):
    return request.param


def test_beverage(beverage_cls: Type[Beverage]):
    beverage = beverage_cls()
    check_description(beverage, beverage_cls)
    check_price(beverage, beverage_cls)


def test_beverage_with_one_condiment(
    beverage_cls: Type[Beverage], condiment_cls: Type[CondimentDecorator]
):
    beverage = condiment_cls(beverage_cls())
    check_description(beverage, beverage_cls, condiment_cls)
    check_price(beverage, beverage_cls, condiment_cls)


def test_beverage_with_two_condiment(
    beverage_cls: Type[Beverage],
    condiment_cls: Type[CondimentDecorator],
    second_condiment_cls: Type[CondimentDecorator],
):
    beverage = second_condiment_cls(condiment_cls(beverage_cls()))
    check_description(beverage, beverage_cls, condiment_cls, second_condiment_cls)
    check_price(beverage, beverage_cls, condiment_cls, second_condiment_cls)
