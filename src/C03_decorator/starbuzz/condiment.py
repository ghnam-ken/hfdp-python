from .base import Beverage, CondimentDecorator


class Mocha(CondimentDecorator):
    def __init__(self, beverage: Beverage):
        super().__init__(beverage, "mocha", 0.20)


class Whip(CondimentDecorator):
    def __init__(self, beverage: Beverage):
        super().__init__(beverage, "whip", 0.10)


class Soy(CondimentDecorator):
    def __init__(self, beverage: Beverage):
        super().__init__(beverage, "soy", 0.30)
