"""
You are given the following code:

class Order:
    morning_discount = 0.25

    def __init__(self, price):
        self.price = price

    def final_price(self):
        return self.price - self.price * self.morning_discount

Make it possible to use different discount programs.
Hint: use strategy behavioural OOP pattern.
https://refactoring.guru/design-patterns/strategy

Example of the result call:

def morning_discount(order):
    ...

def elder_discount(order):
    ...

order_1 = Order(100, morning_discount)
assert order_1.final_price() == 50

order_2 = Order(100, elder_discount)
assert order_2.final_price() == 10
"""
from abc import ABCMeta, abstractmethod


def to_camel_case(snake_str):
    components = snake_str.split("_")
    # We capitalize the first letter of each component except the first one
    # with the 'title' method and join them together.
    return "".join(x.title() for x in components)


#####################################################


class DiscountStrategy(metaclass=ABCMeta):
    """Abstract class for different discount strategies"""

    @property
    @abstractmethod
    def discount(self) -> float:
        pass


class MorningDiscount(DiscountStrategy):
    discount = 0.5


class ElderDiscount(DiscountStrategy):
    discount = 0.9


class StudentDiscount(DiscountStrategy):
    discount = 0.15


class Order:
    """Class takes initial price and discount_strategy function,
    that has a name corresponding to one of the determined DiscountStrategy classes.
    final_price method returns final price after discount application"""

    def __init__(self, price, discount_strategy):
        # find corresponding DiscountStrategy class by name of a function passed in
        strategy_class_name = to_camel_case(discount_strategy.__qualname__)
        strategy = globals()[strategy_class_name]

        self.price = price
        self.discount = strategy.discount

    def final_price(self):
        return self.price - self.price * self.discount
