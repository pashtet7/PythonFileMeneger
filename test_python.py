import pytest
import math

# Тесты для встроенных функций
def test_filter():
    data = [1, 2, 3, 4, 5]
    result = list(filter(lambda x: x % 2 == 0, data))
    assert result == [2, 4]

def test_map():
    data = [1, 2, 3]
    result = list(map(lambda x: x * 2, data))
    assert result == [2, 4, 6]

def test_sorted():
    data = [3, 1, 2]
    result = sorted(data)
    assert result == [1, 2, 3]

# Тесты для функций из библиотеки math
def test_math_pi():
    assert round(math.pi, 5) == 3.14159

@pytest.mark.parametrize("num, expected", [(4, 2), (9, 3), (16, 4)])
def test_math_sqrt(num, expected):
    assert math.sqrt(num) == expected

@pytest.mark.parametrize("base, exp, expected", [(2, 3, 8), (3, 2, 9), (5, 0, 1)])
def test_math_pow(base, exp, expected):
    assert math.pow(base, exp) == expected

@pytest.mark.parametrize("a, b, expected", [(3, 4, 5), (5, 12, 13), (8, 15, 17)])
def test_math_hypot(a, b, expected):
    assert math.hypot(a, b) == expected