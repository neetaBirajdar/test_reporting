from .conftest import with_invalid_values, with_valid_values
import pytest
import allure


@with_valid_values
@allure.testcase("Test addition with valid input values")
def test_addition_with_valid_values(calculator, value_1, value_2):
    expected_result = value_1 + value_2
    assert calculator.addition(value_1, value_2) == expected_result
    print(
        f"Addition:\nvalue_1: {value_1}\nvalue_2: {value_2}\nRESULT: {expected_result}"
    )


@with_invalid_values
@allure.testcase("Test addition with invalid input values")
def test_addition_with_invalid_values(calculator, value_1, value_2):
    result = calculator.addition(value_1, value_2)
    assert "Failed" in result
    print(f"Addition:\nvalue_1: {value_1}\nvalue_2: {value_2}\nRESULT: {result}")


@with_valid_values
@allure.testcase("Test subtraction with valid input values")
def test_subtraction_with_valid_values(calculator, value_1, value_2):
    expected_result = value_1 - value_2
    assert calculator.subtraction(value_1, value_2) == expected_result
    print(
        f"Subtraction:\nvalue_1: {value_1}\nvalue_2: {value_2}\nRESULT: {expected_result}"
    )


@with_invalid_values
@allure.testcase("Test subtraction with invalid input values")
def test_subtraction_with_invalid_values(calculator, value_1, value_2):
    result = calculator.subtraction(value_1, value_2)
    assert "Failed" in result
    print(f"Subtraction:\nvalue_1: {value_1}\nvalue_2: {value_2}\nRESULT: {result}")


@with_valid_values
@allure.testcase("Test division with valid input values")
def test_division_with_valid_values(calculator, value_1, value_2):
    expected_result = value_1 / value_2
    assert calculator.division(value_1, value_2) == expected_result
    print(
        f"Division:\nvalue_1: {value_1}\nvalue_2: {value_2}\nRESULT: {expected_result}"
    )


@with_invalid_values
@allure.testcase("Test division with invalid input values")
def test_division_with_invalid_values(calculator, value_1, value_2):
    result = calculator.division(value_1, value_2)
    assert "Failed" in result
    print(f"Division:\nvalue_1: {value_1}\nvalue_2: {value_2}\nRESULT: {result}")


@allure.testcase("Test division with divide_by_zero")
def test_division_with_divide_by_zero(calculator):
    value_1 = 100
    value_2 = 0
    result = calculator.division(value_1, value_2)
    assert "Failed" in result
    print(f"Division:\nvalue_1: {value_1}\nvalue_2: {value_2}\nRESULT: {result}")


@with_valid_values
@allure.testcase("Test multiplication with valid values")
def test_multiplication_with_valid_values(calculator, value_1, value_2):
    expected_result = value_1 * value_2
    assert calculator.multiplication(value_1, value_2) == expected_result
    print(
        f"Multiplication:\nvalue_1: {value_1}\nvalue_2: {value_2}\nRESULT: {expected_result}"
    )


@with_invalid_values
@allure.testcase("Test multiplication with invalid values")
def test_multiplication_with_invalid_values(calculator, value_1, value_2):
    result = calculator.multiplication(value_1, value_2)
    assert "Failed" in result
    print(f"Multiplication:\nvalue_1: {value_1}\nvalue_2: {value_2}\nRESULT: {result}")


@pytest.mark.xfail(reason="XPass")
@allure.testcase("Test multiplication with zero: xPass")
def test_with_multiplication_with_zero(calculator):
    value_1 = 0
    value_2 = 20
    expected_result = value_1 * value_2
    assert calculator.multiplication(value_1, value_2) == expected_result
    print(
        f"Multiplication:\nvalue_1: {value_1}\nvalue_2: {value_2}\nRESULT: {expected_result}"
    )

@pytest.mark.xfail(reason="Fails")
@allure.testcase("Test division : xfailed")
def test_division_failed(calculator):
    value_1 = 10
    value_2 = 0
    result=calculator.multiplication(value_1, value_2)
    assert "Failed" in result
    print(f"Multiplication:\nvalue_1: {value_1}\nvalue_2: {value_2}\nRESULT: {result}")


@pytest.mark.xfail(reason="Fails")
@allure.testcase("Test subtraction with float type: failed")
def test_result_type_check(calculator):
    value_1 = 10.0
    value_2 = 20.0
    expected_result = int(value_1 - value_2)
    assert type(calculator.subtraction(value_1, value_2)) == type(expected_result)
    print(
        f"Subtraction:\nvalue_1: {value_1}\nvalue_2: {value_2}\nRESULT: {expected_result}"
    )


@pytest.mark.skip
@allure.testcase("Test division with result zero: skipped")
def test_with_result_zero(calculator):
    value_1 = 0
    value_2 = 20
    expected_result = value_1 / value_2
    assert calculator.division(value_1, value_2) == expected_result
    print(
        f"Division:\nvalue_1: {value_1}\nvalue_2: {value_2}\nRESULT: {expected_result}"
    )
