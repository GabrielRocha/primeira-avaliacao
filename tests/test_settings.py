from settings import RANGE_PRINT, MULTIPLES
import unittest


class TestCaseSettings(unittest.TestCase):

    def test_first_index_variable_of_range_print(self):
        for number in [1, 2, 3, 4, 5, 6, 7]:
            self.assertIn(number, RANGE_PRINT[0])

    def test_second_index_variable_of_range_print(self):
        for number in [33, 34, 35, 36]:
            self.assertIn(number, RANGE_PRINT[1])

    def test_third_index_variable_of_range_print(self):
        for number in [97, 98, 99, 100]:
            self.assertIn(number, RANGE_PRINT[2])

    def test_multples_default_keys(self):
        keys = [5, 7, 35]
        self.assertEqual(keys, sorted(MULTIPLES.keys()))

    def test_multiples_of_five(self):
        self.assertEqual(MULTIPLES.get(5), "Nama")

    def test_multiples_of_five_seven(self):
        self.assertEqual(MULTIPLES.get(7), "Team")

    def test_multiples_of_thirty_five(self):
        self.assertEqual(MULTIPLES.get(35), "Nama Team")
