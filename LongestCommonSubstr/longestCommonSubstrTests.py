import longestCommonSubstr
import unittest


class CalcLongestCommonSubstrTests(unittest.TestCase):
    def test_NoCommonSubstr(self):
        s1 = "x"
        s2 = "y"
        sut = longestCommonSubstr.LongestCommonSubstr()

        actual = sut.calcLongestCommonSubstr(s1, s2)

        self.assertIsNone(actual)

    def test_CommonSubstrLength1(self):
        s1 = "x"
        s2 = "x"
        expected = "x"
        sut = longestCommonSubstr.LongestCommonSubstr()

        actual = sut.calcLongestCommonSubstr(s1, s2)

        self.assertEqual(expected, actual)

    def test_CommonSubstrLength4(self):
        s1 = "ALGORITHM"
        s2 = "ARITHMETIC"
        expected = "RITHM"
        sut = longestCommonSubstr.LongestCommonSubstr()

        actual = sut.calcLongestCommonSubstr(s1, s2)

        self.assertEqual(expected, actual)

class GenSubstringsTests(unittest.TestCase):
    def test_OneCharString(self):
        s = "x"
        expected = { "x" }
        sut = longestCommonSubstr.LongestCommonSubstr()

        actual = sut.genSubstrings(s)

        self.assertEqual(0, len(expected.difference(actual)))

    def test_TwoCharString(self):
        s = "xy"
        expected = { "x", "y", "xy" }
        sut = longestCommonSubstr.LongestCommonSubstr()

        actual = sut.genSubstrings(s)

        self.assertEqual(0, len(expected.difference(actual)))

    def test_ThreeCharString(self):
        s = "xyz"
        expected = { "x", "y", "z", "xy", "yz", "xyz" }
        sut = longestCommonSubstr.LongestCommonSubstr()

        actual = sut.genSubstrings(s)

        self.assertEqual(0, len(expected.difference(actual)))

if __name__ == '__main__':
    unittest.main()
