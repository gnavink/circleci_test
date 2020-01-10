"""
    test_calculator.py - test calculator module
                    
"""


import calculator


class TestCalculator():


    def test_addition(self):
        assert 4 == calculator.addition(2, 2)

    
    def test_subtraction(self):
        assert 1 == calculator.subtraction(4, 3)



