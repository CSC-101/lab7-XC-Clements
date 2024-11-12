from convert import str_to_float
import unittest

class TestCases(unittest.TestCase):
    def test_str_to_float_1(self):
        self.assertEqual(str_to_float('123'), 123.0)
    def test_str_to_float_2(self):
        self.assertEqual(str_to_float('Hello!'), None)


if __name__ == '__main__':
    unittest.main()

