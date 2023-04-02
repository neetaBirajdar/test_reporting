from .conftest import with_invalid_values, with_valid_values
import pytest


@with_valid_values
def test_addition_with_valid_values(calculator, value_1, value_2):
    expected_result = value_1 + value_2
    assert calculator.addition(value_1, value_2) == expected_result
    print(f"value_1: {value_1}\nvalue_2: {value_2}\nRESULT: {expected_result}")


@with_invalid_values
def test_addition_with_invalid_values(calculator, value_1, value_2):
    result = calculator.addition(value_1, value_2)
    assert "Failed" in result
    print(f"value_1: {value_1}\nvalue_2: {value_2}\nRESULT: {result}")


@with_valid_values
def test_subtraction_with_valid_values(calculator, value_1, value_2):
    expected_result = value_1 - value_2
    assert calculator.subtraction(value_1, value_2) == expected_result
    print(f"value_1: {value_1}\nvalue_2: {value_2}\nRESULT: {expected_result}")


@with_invalid_values
def test_subtraction_with_invalid_values(calculator, value_1, value_2):
    result = calculator.subtraction(value_1, value_2)
    assert "Failed" in result
    print(f"value_1: {value_1}\nvalue_2: {value_2}\nRESULT: {result}")


@with_valid_values
def test_division_with_valid_values(calculator, value_1, value_2):
    expected_result = value_1 / value_2
    assert calculator.division(value_1, value_2) == expected_result
    print(f"value_1: {value_1}\nvalue_2: {value_2}\nRESULT: {expected_result}")


@with_invalid_values
def test_division_with_invalid_values(calculator, value_1, value_2):
    result = calculator.division(value_1, value_2)
    assert "Failed" in result
    print(f"value_1: {value_1}\nvalue_2: {value_2}\nRESULT: {result}")


def test_division_with_divide_by_zero(calculator):
    value_1 = 100
    value_2 = 0
    result = calculator.division(value_1, value_2)
    assert "Failed" in result
    print(f"value_1: {value_1}\nvalue_2: {value_2}\nRESULT: {result}")


@with_valid_values
def test_multiplication_with_valid_values(calculator, value_1, value_2):
    expected_result = value_1 * value_2
    assert calculator.multiplication(value_1, value_2) == expected_result
    print(f"value_1: {value_1}\nvalue_2: {value_2}\nRESULT: {expected_result}")


@with_invalid_values
def test_multiplication_with_invalid_values(calculator, value_1, value_2):
    result = calculator.multiplication(value_1, value_2)
    assert "Failed" in result
    print(f"value_1: {value_1}\nvalue_2: {value_2}\nRESULT: {result}")
