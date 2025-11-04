import unittest
from calculator import Calculator
import pytest
class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def testadd(self):
        result = self.calc.add(100, 7)
        self.assertEqual(result, 107)
        
        result = self.calc.add(-1, 1)
        self.assertEqual(result, 0)
        
        result = self.calc.add(-1, -1)
        self.assertEqual(result, -2)

    def testsubtract(self):
        result = self.calc.subtract(100, 5)
        self.assertEqual(result, 95)
        
        result = self.calc.subtract(-1, -1)
        self.assertEqual(result, 0)

    def testmultiply(self):
        result = self.calc.multiply(7, 7)
        self.assertEqual(result, 49)
        
        result = self.calc.multiply(-1, 1)
        self.assertEqual(result, -1)

    def testdivide(self):
        result = self.calc.divide(100, 2)
        self.assertEqual(result, 50)
        
        result = self.calc.divide(-60, 30)
        self.assertEqual(result, -20)

        with self.assertRaises(ValueError):
            self.calc.divide(10, 0)
            self.calc.divide(0, 0)