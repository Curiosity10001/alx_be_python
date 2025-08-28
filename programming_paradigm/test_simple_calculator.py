import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    
    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(1, -6), -5)
        
    def test_subtraction(self):
        """Test the subtract method."""
        self.assertEqual(self.calc.subtract(9, 3), 6)
        self.assertEqual(self.calc.subtract(-1, 1), -2)
        self.assertEqual(self.calc.subtract(8, 8), 0)

    def test_multiply(self):
        """Test the multiply method."""
        self.assertEqual(self.calc.multiply(11, 3), 33)
        self.assertEqual(self.calc.multiply(-1, 1), -1)
        self.assertEqual(self.calc.multiply(8, 0), 0) 
        
    def test_divide(self):
        """Test the divide method."""
        self.assertEqual(self.calc.divide(33, 3), 11)
        self.assertEqual(self.calc.divide(-1, 1), -1)
        self.assertIsNone(self.calc.divide(8, 0))