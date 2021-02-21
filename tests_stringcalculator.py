import unittest
import stringcalculator


class TestStringMethods(unittest.TestCase):

    def test_zero_args(self):
        self.assertEqual(stringcalculator.Add(""), 0)

    def test_one_args(self):
        self.assertEqual(stringcalculator.Add("3"), 3)


if __name__ == '__main__':
    unittest.main()
