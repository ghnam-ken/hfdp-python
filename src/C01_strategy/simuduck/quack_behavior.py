from .base import QuackBehavior


class Quack(QuackBehavior):
    def quack(self):
        print("Quack")


class Squeak(QuackBehavior):
    def quack(self):
        print("Squeak")


class MuteQuack(QuackBehavior):
    def quack(self):
        print("<< Silence >>")
