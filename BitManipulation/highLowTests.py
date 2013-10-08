import highLow
import math
import unittest


class GetBitTests(unittest.TestCase):
    def test_Idx0(self):
        n = 0
        index = 0
        expected = False
        sut = highLow.HighLow()

        actual = sut.get_bit(n, index)

        self.assertEqual(expected, actual)

    def test_Idx1(self):
        n = 2
        index = 1
        expected = True
        sut = highLow.HighLow()

        actual = sut.get_bit(n, index)

        self.assertEqual(expected, actual)


class SetBitTests(unittest.TestCase):
    def test_SetIdx0To0(self):
        n = 0
        index = 0
        bit = 0
        expected = 0
        sut = highLow.HighLow()

        actual = sut.set_bit(n, index, bit)

        self.assertEqual(expected, actual)

    def test_SetIdx0To1(self):
        n = 0
        index = 0
        bit = 1
        expected = 1
        sut = highLow.HighLow()

        actual = sut.set_bit(n, index, bit)

        self.assertEqual(expected, actual)

    def test_SetIdx1To0(self):
        n = 2
        index = 1
        bit = 0
        expected = 0
        sut = highLow.HighLow()

        actual = sut.set_bit(n, index, bit)

        self.assertEqual(expected, actual)

    def test_SetIdx1To1(self):
        n = 1
        index = 1
        bit = 1
        expected = 3
        sut = highLow.HighLow()

        actual = sut.set_bit(n, index, bit)

        self.assertEqual(expected, actual)


class FindHigherTests(unittest.TestCase):
    def test_0Returns0(self):
        n = 0
        expected = 0
        sut = highLow.HighLow()

        actual = sut.find_higher(n)

        self.assertEqual(expected, actual)

    def test_1Returns2(self):
        n = 1
        expected = 2
        sut = highLow.HighLow()

        actual = sut.find_higher(n)

        self.assertEqual(expected, actual)

    def test_2Returns4(self):
        n = 2
        expected = 4
        sut = highLow.HighLow()

        actual = sut.find_higher(n)

        self.assertEqual(expected, actual)

    def test_3Returns5(self):
        n = 3
        expected = 5
        sut = highLow.HighLow()

        actual = sut.find_higher(n)

        self.assertEqual(expected, actual)

    def test_6Returns9(self):
        n = 6
        expected = 9
        sut = highLow.HighLow()

        actual = sut.find_higher(n)

        self.assertEqual(expected, actual)

    def test_12Returns13(self):
        n = 12
        expected = 17
        sut = highLow.HighLow()

        actual = sut.find_higher(n)

        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
