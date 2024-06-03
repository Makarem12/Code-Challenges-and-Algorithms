# Write your test here
import pytest
from challenge02 import is_valid

def test_valid_parentheses():
    assert is_valid("()") == True
    assert is_valid("()[]{}") == True
    assert is_valid("[(hello)()]") == True

def test_invalid_parentheses():
    assert is_valid("[({}]") == False
    assert is_valid("(]") == False
    assert is_valid("([)]") == False

def test_empty_string():
    assert is_valid("") == True

def test_only_opening_brackets():
    assert is_valid("(((") == False
    assert is_valid("[[[") == False

def test_only_closing_brackets():
    assert is_valid(")))") == False
    assert is_valid("]]]") == False

if __name__ == "__main__":
    pytest.main()
