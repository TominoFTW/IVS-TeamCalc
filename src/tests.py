import unittest
from ivsmath.mathlib import MathLib

# run tests with:
# python3 -m tests


class LibTestAdd(unittest.TestCase):
    def setUp(self):
        self.lib = MathLib()

    def test_add_positive(self):
        self.assertEqual(MathLib.add(1, 2), 3)
        self.assertEqual(MathLib.add(1, 0), 1)
        self.assertEqual(MathLib.add(0, 0), 0)

    def test_add_negative(self):
        self.assertEqual(MathLib.add(-1, -2), -3)
        self.assertEqual(MathLib.add(-1, 0), -1)
        self.assertEqual(MathLib.add(0, -1), -1)

    def test_add_both(self):
        self.assertEqual(MathLib.add(-1, 2), 1)
        self.assertEqual(MathLib.add(1, -2), -1)
        self.assertEqual(MathLib.add(-1, -2), -3)

    def test_add_float(self):
        self.assertEqual(MathLib.add(1.0, 2.0), 3.0)
        self.assertEqual(MathLib.add(1.0, 0.0), 1.0)
        self.assertEqual(MathLib.add(0.0, 0.0), 0.0)


class LibTestSub(unittest.TestCase):
    def setUp(self):
        self.lib = MathLib()

    def test_sub_positive(self):
        self.assertEqual(MathLib.sub(1, 2), -1)
        self.assertEqual(MathLib.sub(1, 0), 1)
        self.assertEqual(MathLib.sub(0, 0), 0)

    def test_sub_negative(self):
        self.assertEqual(MathLib.sub(-1, -2), 1)
        self.assertEqual(MathLib.sub(-1, 0), -1)
        self.assertEqual(MathLib.sub(0, -1), 1)

    def test_sub_both(self):
        self.assertEqual(MathLib.sub(-1, 2), -3)
        self.assertEqual(MathLib.sub(1, -2), 3)
        self.assertEqual(MathLib.sub(-1, -2), 1)

    def test_sub_float(self):
        self.assertEqual(MathLib.sub(1.0, 2.0), -1.0)
        self.assertEqual(MathLib.sub(1.0, 0.0), 1.0)
        self.assertEqual(MathLib.sub(0.0, 0.0), 0.0)


class LibTestMul(unittest.TestCase):
    def setUp(self):
        self.lib = MathLib()

    def test_mul_positive(self):
        self.assertEqual(MathLib.mul(1, 2), 2)
        self.assertEqual(MathLib.mul(1, 0), 0)
        self.assertEqual(MathLib.mul(0, 0), 0)

    def test_mul_negative(self):
        self.assertEqual(MathLib.mul(-1, -2), 2)
        self.assertEqual(MathLib.mul(-1, 0), 0)
        self.assertEqual(MathLib.mul(0, -1), 0)

    def test_mul_both(self):
        self.assertEqual(MathLib.mul(-1, 2), -2)
        self.assertEqual(MathLib.mul(1, -2), -2)
        self.assertEqual(MathLib.mul(-1, -2), 2)

    def test_mul_float(self):
        self.assertEqual(MathLib.mul(1.0, 2.0), 2.0)
        self.assertEqual(MathLib.mul(1.0, 0.0), 0.0)
        self.assertEqual(MathLib.mul(0.0, 0.0), 0.0)


class LibTestDiv(unittest.TestCase):
    def setUp(self):
        self.lib = MathLib()

    def test_div_positive(self):
        self.assertEqual(MathLib.div(2, 1), 2)
        self.assertEqual(MathLib.div(0, 1), 0)
        self.assertEqual(MathLib.div(150, 5), 30)

    def test_div_negative(self):
        self.assertEqual(MathLib.div(-2, -1), 2)
        self.assertEqual(MathLib.div(0, -1), 0)
        self.assertEqual(MathLib.div(-150, -5), 30)

    def test_div_both(self):
        self.assertEqual(MathLib.div(-2, 2), -1)
        self.assertEqual(MathLib.div(2, -1), -2)
        self.assertEqual(MathLib.div(-1, -2), 0.5)

    def test_div_float(self):
        self.assertEqual(MathLib.div(1.0, 2.0), 0.5)
        self.assertEqual(MathLib.div(1.2, 1), 1.2)
        self.assertEqual(MathLib.div(5.5, 1.1), 5)

    def test_div_exception(self):
        with self.assertRaises(ValueError):
            MathLib.div(1, 0)
            MathLib.div(0, 0)

class LibTestFactorial(unittest.TestCase):
    def setUp(self):
        self.lib = MathLib()

    def test_factorial_positive(self):
        self.assertEqual(MathLib.factorial(2), 2)
        self.assertEqual(MathLib.factorial(7), 5040)
        self.assertEqual(MathLib.factorial(3), 6)

    def test_factorial_zero(self):
        self.assertEqual(MathLib.factorial(0), 1)

    def test_factorial_exception(self):
        with self.assertRaises(ValueError):
            MathLib.factorial(-5)
            MathLib.factorial(-353)
            MathLib.factorial(0.5)
            MathLib.factorial(2.8)
            MathLib.factorial(-31.7)
            MathLib.factorial(-251.432)

class LibTestPower(unittest.TestCase):
    def setUp(self):
        self.lib = MathLib()

    def test_pow_positive(self):
        self.assertEqual(MathLib.power(2, 1), 2)
        self.assertEqual(MathLib.power(0, 1), 0)
        self.assertEqual(MathLib.power(2, 0), 1)

    def test_pow_both(self):
        self.assertEqual(MathLib.power(-2, 2), 4)
        self.assertEqual(MathLib.power(-2, 3), -8)
        self.assertEqual(MathLib.power(-1, 1), -1)


class LibTestRoot(unittest.TestCase):
    def setUp(self):
        self.lib = MathLib()

    def test_root_positive(self):
        self.assertEqual(MathLib.root(2, 1), 1)
        self.assertEqual(MathLib.root(4, 16), 2)
        self.assertEqual(MathLib.root(3, 27), 3)

    def test_root_negative_root(self):
        self.assertEqual(MathLib.root(-2, 1), 1)
        self.assertEqual(MathLib.root(-2, 2), 0.70711)
        self.assertEqual(MathLib.root(-3, 125), 0.2)

    def test_root_float(self):
        self.assertEqual(MathLib.root(2, 0.5), 0.70711)
        self.assertEqual(MathLib.root(2, 2.8), 1.67332)
        self.assertEqual(MathLib.root(2, 256.253), 16.00790)

    def test_root_zero(self):
        self.assertEqual(MathLib.root(2, 0), 0)

    def test_root_exception(self):
        with self.assertRaises(ValueError):
            MathLib.root(0, 5)
            MathLib.root(2, -5)
            MathLib.root(2, -353)
            MathLib.root(2, -31.7)


class LibTestModulo(unittest.TestCase):
    def setUp(self):
        self.lib = MathLib()

    def test_mod_positive(self):
        self.assertEqual(MathLib.mod(10, 3), 1)
        self.assertEqual(MathLib.mod(20, 7), 6)
        self.assertEqual(MathLib.mod(27, 9), 0)

    def test_mod_negative(self):
        self.assertEqual(MathLib.mod(-1, 1), 0)
        self.assertEqual(MathLib.mod(-26, 5), 4)
        self.assertEqual(MathLib.mod(-256, 250), 244)

    def test_mod_exception(self):
        with self.assertRaises(ValueError):
            MathLib.mod(5, 0)
            MathLib.mod(-5, 0)
            MathLib.mod(-5.45, 2)
            MathLib.mod(5.45, 2)


if __name__ == '__main__':
    unittest.main()
