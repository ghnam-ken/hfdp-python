from .base import Beverage


class Espresso(Beverage):
    def __init__(self):
        super().__init__("espresso", 1.99)


class HouseBlend(Beverage):
    def __init__(self):
        super().__init__("house blend", 0.89)
