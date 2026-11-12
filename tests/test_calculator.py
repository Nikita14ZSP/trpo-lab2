import unittest

from calculator import add, divide, multiply, power, subtract


class CalculatorTests(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)

    def test_subtract(self):
        self.assertEqual(subtract(10, 4), 6)
        self.assertEqual(subtract(4, 10), -6)

    def test_multiply(self):
        self.assertEqual(multiply(3, 4), 12)
        self.assertEqual(multiply(-3, 4), -12)
        self.assertEqual(multiply(5, 0), 0)

    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)
        self.assertEqual(divide(-10, 2), -5)

    def test_divide_fraction(self):
        self.assertAlmostEqual(divide(7, 2), 3.5)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            divide(1, 0)

    def test_power(self):
        self.assertEqual(power(2, 3), 8)
        self.assertEqual(power(-2, 3), -8)

    def test_power_zero(self):
        self.assertEqual(power(5, 0), 1)

    def test_power_negative(self):
        self.assertAlmostEqual(power(2, -2), 0.25)

    def test_power_zero_negative(self):
        with self.assertRaises(ZeroDivisionError):
            power(0, -1)


if __name__ == "__main__":
    unittest.main()
