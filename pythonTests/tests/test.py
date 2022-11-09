import pytest
from app.calculator import Calculator
class TestClac:
    def setup(self):
        self.calc = Calculator
    def test_multiply_calculate_correctly(self):
        assert self.calc.multiply(self, 2, 2) == 4
    def test_multiply_failed(self):
        with pytest.raises(AssertionError):
            assert self.calc.multiply(self, 2, 2) == 5
    def test_adding_calculate_correctly(self):
        assert self.calc.adding(self,1,1)==2
    def test_adding_calculate_incorrrect(self):
        with pytest.raises(AssertionError):
            assert self.calc.adding(self,1,1)==3
    def test_division_calculate_correctly(self):
        assert self.calc.division(self,4,2)==2
    def test_division_calculate_incorrect(self):
        with pytest.raises(AssertionError):
            assert self.calc.division(self,4,2)==1
    def test_subtraction_calculate_correctly(self):
        assert self.calc.subtraction(self, 4,2)==2
    def test_subtraction_calculate_incorrect(self):
        with pytest.raises(AssertionError):
            assert self.calc.subtraction(self,4,2)==0

    def test_zero_division(self):
        with pytest.raises(ZeroDivisionError):
            self.calc.division(self, 1, 0)
