import pytest
from app.calculator import Calculator


class TestCalc:
    def setup(self):
        self.culc = Calculator

    def test_multiply_culculate_correctly(self):
        assert self.culc.multiplay(self, 2, 2) == 4

    def test_division_culculate_correctly(self):
        assert self.culc.division(self, 8, 2) == 4

    def test_subtraction_culculate_correctly(self):
        assert self.culc.subtraction(self, 8, 2) == 6

    def test_adding_culculate_correctly(self):
        assert self.culc.adding(self, 8, 2) == 10

