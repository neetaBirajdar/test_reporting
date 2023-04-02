# Calculator which takes 2 values of type in int or float and gives the result.
# Gives error if there are invalid values given

type_error_message = "Failed: Input values type is not in [int, float]"


class Calculator:

    # Validates the input value types and returns True or False
    def input_type_validator(self, value_1, value_2) -> bool:
        input_is_number = False
        if isinstance(value_1, int | float) and isinstance(value_2, int | float):
            input_is_number = True
        return input_is_number

    # Add given two values and returns result
    def addition(self, value_1, value_2) -> int | str:
        given_valid_inputs = self.input_type_validator(value_1, value_2)
        if given_valid_inputs is not True:
            return type_error_message
        return value_1 + value_2

    # Subtract given two values and returns result
    def subtraction(self, value_1, value_2) -> int | str:
        given_valid_inputs = self.input_type_validator(value_1, value_2)
        if given_valid_inputs is not True:
            return type_error_message
        return value_1 - value_2


def call_calculator():
    cal = Calculator()

    # check the values if you want
    value_1 = 10
    value_2 = 20

    # Check for functionality
    addition_result = cal.addition(value_1, value_2)
    print(f"\nAddition:     {value_1} + {value_2} -> {addition_result}")

    # Check for functionality
    subtraction_result = cal.subtraction(value_1, value_2)
    print(f"Subtraction:  {value_1} - {value_2} -> {subtraction_result}")


# call and verify if calculator works
call_calculator()
