from .conftest import with_valid_addition_values, with_invalid_addition_values


@with_valid_addition_values
def test_addition_with_valid_values(calculator, value_1, value_2, result):
    assert calculator.addition(value_1, value_2) == result
    print(f"value_1: {value_1}\nvalue_2: {value_2}\nRESULT: {result}")


@with_invalid_addition_values
def test_addition_with_invalid_values(calculator, value_1, value_2):
    result = calculator.addition(value_1, value_2)
    assert "Failed" in result
    print(f"value_1: {value_1}\nvalue_2: {value_2}\nRESULT: {result}")
