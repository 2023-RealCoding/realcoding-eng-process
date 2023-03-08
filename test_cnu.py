import unittest

import cnu


class TestSample(unittest.TestCase):

    def test_fibonacci(self):
        self.assertEqual(cnu.fibonacci(0), 0)
        self.assertEqual(cnu.fibonacci(1), 1)
        self.assertEqual(cnu.fibonacci(2), 1)
        self.assertEqual(cnu.fibonacci(3), 2)
        self.assertEqual(cnu.fibonacci(4), 3)
        self.assertEqual(cnu.fibonacci(9), 34)

    def test_factorial(self):
        self.assertEqual(cnu.factorial(1), 1)
        self.assertEqual(cnu.factorial(2), 2)
        self.assertEqual(cnu.factorial(3), 6)
        self.assertEqual(cnu.factorial(4), 24)
        self.assertEqual(cnu.factorial(5), 120)


if __name__ == '__main__':
    unittest.main()
