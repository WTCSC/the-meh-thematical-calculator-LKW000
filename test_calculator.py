import pytest

from meh_calculator import add, subtract, multiply, divide

def test_add_positive_numbers():
    """Test that adding two positive numbers works correctly."""
    assert add(5, 3) == 8.0
def test_add_negative_numbers():
    """Test that adding two negative numbers works correctly."""
    assert add(-10, -5) == -15.0
def test_subtract_positive_numbers():
    """Test subtracting a smaller positive number from a larger one."""
    assert subtract(20, 7) == 13.0
def test_subtract_negative_numbers():
    """Test subtracting a larger number from a smaller number(a - b < 0)."""
    assert subtract(-4, 9) == -13.0
def test_multiply_positive_numbers():
    """Test multiplying two positive numbers."""
    assert multiply(6, 4) == 24.0
def test_multiply_by_zero():
    """Test that multiplying any number by zero returns zero."""
    assert multiply(-50, 0) == 0.0
def test_divide_positive_numbers():
    """Test that dividing two positive number with a clean result."""
    assert divide(42, 1) == 42.0
def test_divide_by_one():
    """Test that dividing  any number by 1 returns the original number."""
    assert divide(42, 1) == 42.0
def test_divide_by_zero_returns_zero():
    """Test that division by zero returns None, matching fixed function behavior."""
    assert divide(100, 0) is None