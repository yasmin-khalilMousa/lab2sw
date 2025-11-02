import pytest 

from file import SimpleMath


def test_add():
    assert SimpleMath.add(3, 4) == 7


def test_subtract():
    assert SimpleMath.subtract(10, 6) == 4


def test_multiply():
    assert SimpleMath.multiply(7, 6) == 42


def test_divide():
    assert SimpleMath.divide(9, 3) == 3


def test_divide_by_zero():
    with pytest.raises(ValueError):
        SimpleMath.divide(1, 0)
