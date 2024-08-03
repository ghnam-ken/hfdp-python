class Beverage():
    def __init__(self, description: str, price: float):
        self.description = description
        self.price = price

    def get_description(self) -> str:
        return self.description

    def cost(self) -> float:
        return self.price


class CondimentDecorator(Beverage):
    def __init__(self, beverage: Beverage, description: str, price: float):
        super().__init__(description, price)
        self.beverage = beverage

    def cost(self):
        return super().cost() + self.beverage.cost()

    def get_description(self) -> str:
        return " ".join([super().get_description(), self.beverage.get_description()])
