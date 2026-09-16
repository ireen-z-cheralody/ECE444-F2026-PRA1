import unittest
from utils import reversed, formatter


class TestReversed(unittest.TestCase):

    def test_reversed_string(self):
        with self.assertRaises(TypeError):
            reversed("123")

    def test_reversed_float(self):
        with self.assertRaises(TypeError):
            reversed(123.45)

    def test_reversed_integer(self):
        self.assertEqual(reversed(12345), 54321)


class TestFormatter(unittest.TestCase):

    def test_formatter_string(self):
        with self.assertRaises(TypeError):
            formatter("10")

    def test_formatter_float(self):
        with self.assertRaises(TypeError):
            formatter(10.5)

    def test_formatter_integer(self):
        self.assertEqual(formatter(10), ("1010", "12"))


if __name__ == "__main__":
    unittest.main()
