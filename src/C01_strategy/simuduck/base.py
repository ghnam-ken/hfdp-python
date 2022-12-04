from abc import ABCMeta, abstractmethod


class QuackBehavior(metaclass=ABCMeta):
    @abstractmethod
    def quack(self):
        pass


class FlyBehavior(metaclass=ABCMeta):
    @abstractmethod
    def fly(self):
        pass


class Duck(metaclass=ABCMeta):
    def __init__(
        self,
        quack_behavior: QuackBehavior,
        fly_behavior: FlyBehavior
    ):
        self._quack_behavior = quack_behavior
        self._fly_behavior = fly_behavior

    @property
    def quack_behavior(self):
        return self._quack_behavior

    @property
    def fly_behavior(self):
        return self._fly_behavior

    @quack_behavior.setter
    def quack_behavior(self, quack_behavior: QuackBehavior):
        self._quack_behavior = quack_behavior

    @fly_behavior.setter
    def fly_behavior(self, fly_behavior: FlyBehavior):
        self._fly_behavior = fly_behavior

    @abstractmethod
    def display(self):
        pass

    def perform_quack(self):
        self._quack_behavior.quack()

    def perform_fly(self):
        self._fly_behavior.fly()

    def swim(self):
        print("All ducks float, even decoys!")
