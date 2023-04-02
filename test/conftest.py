import pytest
from calculator_app.calculator import Calculator


@pytest.fixture
def calculator() -> Calculator:
    return Calculator()


with_valid_values = pytest.mark.parametrize(
    "value_1, value_2",
    [[10, 20], [-10, 20], [10, 20.5], [10.20, 20.30], [0, 0], [-30, -30]],
)

with_invalid_values = pytest.mark.parametrize(
    "value_1, value_2",
    [
        [0, "a"],
        ["a", 10.45],
        ["", -90],
        ["a", "b"],
    ],
)
