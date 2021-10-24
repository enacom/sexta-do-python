import unittest
from sexta_of_python.example_classes import Calculator


class TestCalculator(unittest.TestCase):
    def add_test(self):
        # Test won't run because it's name does not begins with test_
        self.assertEqual(Calculator.add(20, 5), 50)

    def test_add(self):
        self.assertEqual(Calculator.add(20, 5), 25)
        # self.assertEqual(Calculator.add(-5, 5), 1)
        self.assertEqual(Calculator.add(-5, 5), 0)

    def test_subtraction(self):
        self.assertEqual(Calculator.subtraction(20, 5), 15)

    def test_multiply(self):
        self.assertEqual(Calculator.multiply(20, 5), 100)

    def test_divide(self):
        self.assertEqual(Calculator.divide(20, 5), 4)
        # self.assertRaises(ValueError, Calculator.divide, 5, 0)
        self.assertRaises(ValueError, Calculator.divide, 5, 1)

    def test_power(self):
        calc = Calculator()
        self.assertEqual(calc.power(2, 5), 32)


if __name__ == '__main__':
    unittest.main()
