import pytest
from calculator_app.calculator import Calculator


@pytest.fixture
def calculator() -> Calculator:
    return Calculator()


with_valid_addition_values = pytest.mark.parametrize(
    "value_1, value_2, result",
    [[10, 20, 30], [-10, 20, 10], [10, 20.5, 30.5], [10.20, 20.30, 30.50]],
)

with_invalid_addition_values = pytest.mark.parametrize(
    "value_1, value_2",
    [
        [0, "a"],
        ["a", 10.45],
        ["", -90],
        ["a", "b"],
    ],
)
