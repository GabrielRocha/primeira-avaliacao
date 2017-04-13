import unittest
import settings
import nama


class TestCaseNama(unittest.TestCase):

    def test_multiples_of_five(self):
        five_multiplus = [5, 10, 15, 20, 25, 30, 40, 45, 50]
        for multiplus in five_multiplus:
            self.assertEqual(nama.is_multiples(multiplus), "Nama")

    def test_multiples_of_seven(self):
        seven_multiplus = [7, 14, 21, 28, 42, 49, 56, 63, 98]
        for multiplus in seven_multiplus:
            self.assertEqual(nama.is_multiples(multiplus), "Team")

    def test_multiples_of_thirty_five(self):
        thirty_five_multiplus = [35, 70, 105]
        for multiplus in thirty_five_multiplus:
            self.assertEqual(nama.is_multiples(multiplus), "Nama Team")

    def test_nama_numbers(self):
        result = "1, 2, 3, 4, Nama, 6, Team, " \
                 "........ 33, 34, Nama Team, 36 ....., 97, Team, 99, Nama"
        self.assertEqual(nama.nama_numbers(), result)

    def test_nama_numbers_only_one_index(self):
        settings.RANGE_PRINT = (range(1, 11),)
        self.assertEqual(nama.nama_numbers(),
                         "1, 2, 3, 4, Nama, 6, Team, 8, 9, Nama")

    def test_nama_numbers_two_indexes(self):
        settings.RANGE_PRINT = (range(1, 9), range(20, 27))
        result = "1, 2, 3, 4, Nama, 6, Team, 8, " \
                 "......... Nama, Team, 22, 23, 24, Nama, 26 ........"
        self.assertEqual(nama.nama_numbers(), result)

    def test_nama_numbers_four_indexes(self):
        settings.RANGE_PRINT = (range(1, 3), range(8, 11),
                                range(13, 16), range(17, 20))
        result = "1, 2, ... 8, 9, Nama ...., " \
                 "13, Team, Nama, .... 17, 18, 19 ...."
        self.assertEqual(nama.nama_numbers(), result)
