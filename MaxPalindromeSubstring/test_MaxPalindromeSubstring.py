import maxPalindromeSubstring
import unittest

class MaxPalindromeSubstringTest(unittest.TestCase):
    # even length palindrome tests
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

    # odd length palindrome tests
    def test_ThreeCharStringThatHasThreeCharPalindrome(self):
        s = "xxx"
        expected = "xxx"

        actual = maxPalindromeSubstring.find_max_palindrome_substring(s)

        self.assertEqual(expected, actual)

    def test_FourCharStringThatHasThreeCharPalindromeAtEnd(self):
        s = "Axxx"
        expected = "xxx"

        actual = maxPalindromeSubstring.find_max_palindrome_substring(s)

        self.assertEqual(expected, actual)

    def test_FourCharStringThatHasThreeCharPalindromeAtFront(self):
        s = "xxxA"
        expected = "xxx"

        actual = maxPalindromeSubstring.find_max_palindrome_substring(s)

        self.assertEqual(expected, actual)

    def test_FiveCharStringThatHasThreeCharPalindromeInMiddle(self):
        s = "AxxxB"
        expected = "xxx"

        actual = maxPalindromeSubstring.find_max_palindrome_substring(s)

        self.assertEqual(expected, actual)

    # strings w/ a mix of even and odd length palindromes
    def test_StringWithOddLengthPalindromeAsLargest(self):
        s = "ABBAracecarABA"
        expected = "racecar"

        actual = maxPalindromeSubstring.find_max_palindrome_substring(s)

        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
