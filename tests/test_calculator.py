"""
    test_calculator.py - test calculator module
"""


import calculator


class TestCalculator():
    """
      class to test calculator
    """
    def test_addition(self):
        assert 4 == calculator.addition(2, 2)

    def test_subtraction(self):
        assert 1 == calculator.subtraction(4, 3)

    def test_multiplication(self):
        assert 100 == calculator.multiply(10, 10)
