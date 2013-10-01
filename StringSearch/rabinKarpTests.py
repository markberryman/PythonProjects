import rabinKarp
import unittest


class AsciiSumRollingHashTests(unittest.TestCase):
    def test_ComputesHashOfStringIfLastStringEmpty(self):
        sut = rabinKarp.RabinKarp()

        actual = sut.ascii_sum_rolling_hash(None, 0, "A")

        self.assertEqual(65, actual)

    def test_ComputesHashOfSingleCharString(self):
        sut = rabinKarp.RabinKarp()

        actual = sut.ascii_sum_rolling_hash("A", 65, "B")

        self.assertEqual(66, actual)

    def test_ComputesHashOfTwoCharString(self):
        sut = rabinKarp.RabinKarp()

        actual = sut.ascii_sum_rolling_hash("AB", 131, "BC")

        self.assertEqual(133, actual)


class ContainsStringTests(unittest.TestCase):
    def test_ReturnsFalseIfNotContainsForSingleCharStrings(self):
        s1 = "A"
        s2 = "B"

        sut = rabinKarp.RabinKarp()
        actual = sut.contains_string(s1, s2)

        self.assertFalse(actual)

    def test_ReturnsFalseIfNotContainsForMultiCharStrings(self):
        s1 = "AB"
        s2 = "BC"

        sut = rabinKarp.RabinKarp()
        actual = sut.contains_string(s1, s2)

        self.assertFalse(actual)

    def test_ReturnsFalseIfStringToSearchForLargerThanStringToSearchIn(self):
        s1 = "AB"
        s2 = "B"

        sut = rabinKarp.RabinKarp()
        actual = sut.contains_string(s1, s2)

        self.assertFalse(actual)

    def test_ReturnsTrueIfStringContainedForSingleCharStrings(self):
        s1 = "A"
        s2 = "A"

        sut = rabinKarp.RabinKarp()
        actual = sut.contains_string(s1, s2)

        self.assertTrue(actual)

    def test_ReturnsTrueIfStringContainedForMultiCharStrings(self):
        s1 = "AB"
        s2 = "BAB"

        sut = rabinKarp.RabinKarp()
        actual = sut.contains_string(s1, s2)

        self.assertTrue(actual)


if __name__ == '__main__':
    unittest.main()
