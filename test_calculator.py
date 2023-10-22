import unittest
from calculator import Calculator


class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)
        self.assertEqual(self.calc.add(-1, -1), -2)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(3, 1), 2)
        self.assertEqual(self.calc.subtract(-1, -1), 0)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(3, 3), 9)
        self.assertEqual(self.calc.multiply(-1, 3), -3)

    def test_divide(self):
        self.assertEqual(self.calc.divide(6, 2), 3)
        self.assertEqual(self.calc.divide(5, 2), 2.5)
        with self.assertRaises(ValueError):
            self.calc.divide(1, 0)

    def test_power(self):
        self.assertEqual(self.calc.power(2, 3), 8)
        self.assertEqual(self.calc.power(5, 0), 1)
        self.assertEqual(self.calc.power(3, 2), 9)
        self.assertEqual(self.calc.power(-2, 3), -8)

    def test_modulus(self):
        self.assertEqual(self.calc.modulus(7, 2), 1)
        self.assertEqual(self.calc.modulus(10, 3), 1)
        with self.assertRaises(ValueError):
            self.calc.modulus(1, 0)

    def test_floor_divide(self):
        self.assertEqual(self.calc.floor_divide(7, 2), 3)
        self.assertEqual(self.calc.floor_divide(10, 3), 3)
        with self.assertRaises(ValueError):
            self.calc.floor_divide(1, 0)


if __name__ == "__main__":
    unittest.main()
