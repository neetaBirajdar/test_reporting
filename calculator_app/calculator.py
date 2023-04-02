# Calculator which takes 2 values of type in int or float and gives the result.
# Gives error if there are invalid values given

type_error_message = "Failed: Input values type is not in [int, float]"
divide_by_zero_error_message = "Failed: Division by zero"


class Calculator:

    # Validates the input value types and returns True or False
    def input_type_validator(self, value_1, value_2) -> bool:
        input_is_number = False
        if isinstance(value_1, int | float) and isinstance(value_2, int | float):
            input_is_number = True
        return input_is_number

    # Add two numbers
    def addition(self, value_1, value_2) -> int | str:
        given_valid_inputs = self.input_type_validator(value_1, value_2)
        if given_valid_inputs is not True:
            return type_error_message
        return value_1 + value_2

    # Subtract two numbers
    def subtraction(self, value_1, value_2) -> int | str:
        given_valid_inputs = self.input_type_validator(value_1, value_2)
        if given_valid_inputs is not True:
            return type_error_message
        return value_1 - value_2

    # Multiply two numbers
    def multiplication(self, value_1, value_2) -> int | str:
        given_valid_inputs = self.input_type_validator(value_1, value_2)
        if given_valid_inputs is not True:
            return type_error_message
        return value_1 * value_2

    # Divide two numbers
    def division(self, value_1, value_2) -> int | str:
        given_valid_inputs = self.input_type_validator(value_1, value_2)
        if given_valid_inputs is not True:
            return type_error_message
        try:
            return value_1 / value_2
        except Exception:
            return divide_by_zero_error_message


def call_calculator():
    cal = Calculator()

    # change the values if you want
    value_1 = 10
    value_2 = 0

    # Check for functionality
    result = cal.addition(value_1, value_2)
    print(f"\nAddition:     {value_1} + {value_2} -> {result}")

    result = cal.subtraction(value_1, value_2)
    print(f"Subtraction:  {value_1} - {value_2} -> {result}")

    result = cal.division(value_1, value_2)
    print(f"Division:     {value_1} / {value_2} -> {result}")

    result = cal.multiplication(value_1, value_2)
    print(f"Multiplication: {value_1} * {value_2} -> {result}")


# call and verify if calculator works
call_calculator()
