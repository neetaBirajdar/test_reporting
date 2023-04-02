# Test Reporting

Test reporting is always important part of testing. It provides an overview of which testcases are working, which ones are failing and details like what happened if logged or printed.

## Test Report with Pytest
- `pytest` is a very well known testing framework used in python test world.
- There are multiple options for reporting that can be used along with Pytest to make the results easy to read and understand.


# Example Application
To understand the reporting better, I have created a *Calculator Application* which can perform `addition`, `subtraction`, `division` and  `multiplication` with the given two input numbers.

[calculator_app/calculator.py]
- Takes only 2 numbers
- It validates the type of input values given
- It returns the valid error message

[test/test_calculator.py]
- Test all operations with valid and invalid input values

[test/conftest.py]
- Input values params
- Calculator object fixture

## Setup on your machine:

1. Clone the repo:
```
git clone git@github.com:neetaBirajdar/test_reporting.git
```

2. Create virtual env(for safety of your host env):
```
python -m venv venv
source venv/bin/activate
```

3. Install requirements:
```
pip install -r requirements.txt
```

You can run the application and test to see what it does. But its completely optional as we are more focusing on reporting.
Run the application
```
python calculator_app/calculator.py
```

Run the test on application
```
pytest test/test_calculator.py
```
