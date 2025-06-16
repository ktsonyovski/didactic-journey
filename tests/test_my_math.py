"""Unit tests for the MyMath class providing basic mathematical operations."""
# pylint: disable=missing-function-docstring
import pytest
from my_math.my_math import MyMath

class TestMyMath:
    """
    Test suite for the MyMath class.

    This class contains unit tests for all static methods in the MyMath class,
    covering addition, subtraction, multiplication, and division operations.
    Each test checks a specific scenario to ensure correct functionality.
    """

    # Tests for add
    def test_add_positive_numbers(self):
        assert MyMath.add(2, 3) == 5

    def test_add_negative_and_positive(self):
        assert MyMath.add(-1, 1) == 0

    def test_add_zeros(self):
        assert MyMath.add(0, 0) == 0

    # Tests for substract
    def test_substract_positive(self):
        assert MyMath.substract(5, 3) == 2

    def test_substract_result_negative(self):
        assert MyMath.substract(0, 1) == -1

    def test_substract_both_negative(self):
        assert MyMath.substract(-2, -2) == 0

    # Tests for multiply
    def test_multiply_positive(self):
        assert MyMath.multiply(2, 3) == 6

    def test_multiply_negative_and_positive(self):
        assert MyMath.multiply(-1, 5) == -5

    def test_multiply_by_zero(self):
        assert MyMath.multiply(0, 100) == 0

    # Tests for divide
    def test_divide_positive(self):
        assert MyMath.divide(6, 3) == 2

    def test_divide_negative_by_positive(self):
        assert MyMath.divide(-10, 2) == -5

    def test_divide_result_float(self):
        assert MyMath.divide(5, 2) == 2.5

    def test_divide_by_zero_raises(self):
        with pytest.raises(ZeroDivisionError):
            MyMath.divide(1, 0)
