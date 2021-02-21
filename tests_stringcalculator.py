import unittest
import stringcalculator


class TestStringMethods(unittest.TestCase):

    def test_zero_args(self):
        self.assertEqual(stringcalculator.Add(""), 0)

    def test_one_args(self):
        self.assertEqual(stringcalculator.Add("3"), 3)

    def test_one_ii_args(self):
        self.assertEqual(stringcalculator.Add("43"), 43)

    def test_two_args(self):
        self.assertEqual(stringcalculator.Add("4,3"), 7)

    def test_many_args(self):
        self.assertEqual(stringcalculator.Add("4,2,5"), 11)

    def test_jump_line(self):
        self.assertEqual(stringcalculator.Add("4,2\n5"), 11)

    def test_different_delimiter(self):
        self.assertEqual(stringcalculator.Add(":4:2\n5"), 11)    


if __name__ == '__main__':
    unittest.main()
