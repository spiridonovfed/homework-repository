from homework11.hw2 import *


def morning_discount(order):
    ...


def elder_discount(order):
    ...


def student_discount(order):
    ...


def test_from_example_1():
    order_1 = Order(100, morning_discount)
    assert order_1.final_price() == 50


def test_from_example_2():
    order_2 = Order(100, elder_discount)
    assert order_2.final_price() == 10


def test_student_discount():
    order_3 = Order(100, student_discount)
    assert order_3.final_price() == 85
