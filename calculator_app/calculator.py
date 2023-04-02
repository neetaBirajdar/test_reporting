# Calculator which takes 2 values of type in int or float and gives the result.
# Gives error if there are invalid values given


class Calculator:
    def addition(self, value_1, value_2) -> int | str:
        # Add given two values and returns result

        if isinstance(value_1, int | float) and isinstance(value_2, int | float):
            # checks the type of value_1, value_2
            result = value_1 + value_2
        else:
            # returns failed message when the value type are int or float
            result = "Failed: Input values type is not in [int, float]"

        return result


def call_calculator():
    cal = Calculator()

    # check the values if you want
    value_1 = 10
    value_2 = 20

    # Check for functionality
    addition_result = cal.addition(value_1, value_2)
    print(f"\nAddition:  {value_1} + {value_2} -> {addition_result}")


# call and verify if calculator works
call_calculator()
