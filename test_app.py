import pytest
import inspect

from app import squared

# TODO: add tests below to be run by pytest.


@pytest.mark.one
def test_squared_of_1_is_1():
    assert squared(1) == 1


@pytest.mark.ten
def test_squared_of_10_is_100():
    assert squared(10) == 100


@pytest.mark.neg_two
def test_squared_of_negative_two_is_not_negative_four():
    assert squared(-2) != -4


@pytest.mark.isfunction
def test_squared_is_a_function():
    assert inspect.isfunction(squared) is True


@pytest.mark.ret_int
def test_squared_of_20_returns_integer():
    assert type(squared(20)) is int


@pytest.mark.error
def test_squared_of_string_raises_type_error():
    with pytest.raises(TypeError):
        squared('This is sting')
