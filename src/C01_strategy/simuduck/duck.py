from .base import Duck
from .fly_behavior import FlyWithWings, FlyNoWay
from .quack_behavior import Quack, Squeak, MuteQuack


class MallardDuck(Duck):
    def __init__(self):
        super().__init__(Quack(), FlyWithWings())

    def display(self):
        print("I'm a real Mallard duck")


class RubberDuck(Duck):
    def __init__(self):
        super().__init__(Squeak(), FlyNoWay())

    def display(self):
        print("I'm a rubber duck")


class DecoyDuck(Duck):
    def __init__(self):
        super().__init__(MuteQuack(), FlyNoWay())

    def display(self):
        print("I'm a decoy duck")
