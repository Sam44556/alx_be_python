import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Create a calculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_add(self):
        """Test addition method."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, -1), -2)
        self.assertEqual(self.calc.add(0, 5), 5)

    def test_subtract(self):
        """Test subtraction method."""
        self.assertEqual(self.calc.subtract(10, 4), 6)
        self.assertEqual(self.calc.subtract(0, 4), -4)
        self.assertEqual(self.calc.subtract(-3, -3), 0)

    def test_multiply(self):
        """Test multiplication method."""
        self.assertEqual(self.calc.multiply(3, 4), 12)
        self.assertEqual(self.calc.multiply(0, 100), 0)
        self.assertEqual(self.calc.multiply(-2, 3), -6)

    def test_divide(self):
        """Test division method."""
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertEqual(self.calc.divide(7, -1), -7)
        self.assertEqual(self.calc.divide(0, 5), 0)
    
    def test_divide_by_zero(self):
        """Test division by zero returns None."""
        self.assertIsNone(self.calc.divide(5, 0))

if __name__ == '__main__':
    unittest.main()
