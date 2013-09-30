import longestCommonSubstr
import unittest


class GenSubstringsTests(unittest.TestCase):
    def test_OneCharString(self):
        s = "x"
        expected = { "x" }
        sut = longestCommonSubstr.LongestCommonSubstr()

        actual = sut.genSubstrings(s)

        self.assertEqual(0, len(actual.difference(expected)))


if __name__ == '__main__':
    unittest.main()
