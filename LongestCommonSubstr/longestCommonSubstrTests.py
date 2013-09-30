import longestCommonSubstr
import unittest


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
