'''
tutorial: https://www.youtube.com/watch?v=EgpLj86ZHFQ&t=553s

libraries: pip install pytest, pip install pytest-mock
explanation:
    one test per file to be tested
    if main.py, test_main.py, prefix test_ indicates pytest
    this is the file to test main.py.
To run a test: on the console type - pytest test_main.py

Unit test: oriented to test small units of code like functions
so we can isolate errors or debugging code.

Test driven development: write tests before writing code.

Make independent tests, one test per functionality.

fixture: run before every step. like setup
'''

# Example 1
from main import get_weather

# def test_get_weather():
#     assert get_weather(21) == "hot"
#     assert get_weather(30) == "hot"
#     assert get_weather(30) != "cold"
    

# Example 2
from main import add, divide
import pytest

def test_add():
    assert add(2, 3) == 5, "2 + 3 should be 5"
    assert add(-1, 1) == 0, "-1 + 1 should be 0"
    assert add(0, 0) == 0, "0 + 0 should be 0"
    
def test_divide():
    with pytest.raises(ValueError, match = "Cannot divide by zero"):
        divide(10, 0)