import Fibonacci
import unittest

from Fibonacci import *


class TestFibonacci(unittest.TestCase):
    def setUp(self):
        self.fib = fibonacci_dp

    def test_base_cases(self):
        self.assertEqual(self.fib(1), 1)
        self.assertEqual(self.fib(2), 1)

    def test_small_n(self):
        self.assertEqual(self.fib(12), 144)

    def test_large_n(self):
        self.assertEqual(self.fib(100), 354224848179261915075)


if __name__ == "__main__":
    unittest.main()
