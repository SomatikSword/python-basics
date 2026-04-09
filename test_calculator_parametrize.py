import pytest
from Calculator import add, subtract, multiply, divide


@pytest.mark.parametrize("a, b, expected", [
    (5, 3, 8),
    (0, 0, 0),
    (-1, 1, 0),
    (100, 50, 150),
    (-10, -5, -15),
    (6, 9, 15),
    (2, 4, 6),
    (3, 13, 16),
])
def test_add_parametrize(a, b, expected):
    assert add(a, b) == expected


@pytest.mark.parametrize("a, b, expected", [
    (10, 4, 6),
    (5, 5, 0),
    (0, 10, -10),
    (100, 30, 70),
])
def test_subtract_parametrize(a, b, expected):
    assert subtract(a, b) == expected


@pytest.mark.parametrize("a, b, expected", [
    (7, 6, 42),
    (5, 0, 0),
    (-2, 3, -6),
    (10, 10, 100),
])
def test_multiply_parametrize(a, b, expected):
    assert multiply(a, b) == expected


@pytest.mark.parametrize("a, b, expected", [
    (20, 4, 5.0),
    (10, 2, 5.0),
    (100, 4, 25.0),
])
def test_divide_parametrize(a, b, expected):
    assert divide(a, b) == expected


def test_divide_by_zero():
    assert divide(10, 0) == "Ошибка: деление на ноль"