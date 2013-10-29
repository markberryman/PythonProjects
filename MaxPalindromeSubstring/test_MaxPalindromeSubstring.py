import maxPalindromeSubstring
import unittest

class MaxPalindromeSubstringTest(unittest.TestCase):
    def test_SingleCharString(self):
        s = "x"
        expected = "x"

        actual = maxPalindromeSubstring.find_max_palindrome_substring(s)

        self.assertEqual(expected, actual)

    def test_TwoCharStringThatHasPalindrome(self):
        s = "xx"
        expected = "xx"

        actual = maxPalindromeSubstring.find_max_palindrome_substring(s)

        self.assertEqual(expected, actual)

    def test_ThreeCharStringThatHasTwoCharPalindromeAtEnd(self):
        s = "Yxx"
        expected = "xx"

        actual = maxPalindromeSubstring.find_max_palindrome_substring(s)

        self.assertEqual(expected, actual)

    def test_FourCharStringThatHasTwoCharPalindromeInMiddle(self):
        s = "YxxZ"
        expected = "xx"

        actual = maxPalindromeSubstring.find_max_palindrome_substring(s)

        self.assertEqual(expected, actual)

    def test_FourCharStringThatHasTwoCharPalindromeAtFront(self):
        s = "xxYZ"
        expected = "xx"

        actual = maxPalindromeSubstring.find_max_palindrome_substring(s)

        self.assertEqual(expected, actual)

    def test_SixCharStringThatHasFourCharPalindromeInMiddle(self):
        s = "AxxxxB"
        expected = "xxxx"

        actual = maxPalindromeSubstring.find_max_palindrome_substring(s)

        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
