import pytest
from calculator import Calculator

calculator = Calculator()


def test_sum_positive_nums():
    calculator = Calculator()
    res = calculator.sum(4, 5)
    assert res == 9


def test_sum_negative_nums():
    calculator = Calculator()
    res = calculator.sum(-4, -5)
    assert res == -9


def test_sum_positive_and_negative_nums():
    calculator = Calculator()
    res = calculator.sum(-4, 5)
    assert res == 1


def test_sum_float_nums():
    calculator = Calculator()
    res = calculator.sum(4.4, 5.5)
    assert res == 9.9


def test_sum_zero_nums():
    calculator = Calculator()
    res = calculator.sum(10, 0)
    assert res == 10


def test_div_positive():
    calculator = Calculator()
    res = calculator.div(10, 2)
    assert res == 5


def test_div_by_zero():
    calculator = Calculator()
    with pytest.raises(ArithmeticError):
        calculator.div(10, 0)


def test_avg_empty_list():
    calculator = Calculator()
    numbers = []
    res = calculator.avg(numbers)
    assert res == 0


def test_avg_positive():
    calculator = Calculator()
    numbers = [1, 3, 5, 7, 9]
    res = calculator.avg(numbers)
    assert res == 5

# res = calculator.div(10, 0)
# assert res == None

# print("Finish")
