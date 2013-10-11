import stringProblems
import unittest


class IsAllUniqueCharsTests(unittest.TestCase):
    def test_ReturnsTrueWhenStringIsAllUniqueChars(self):
        expected = True
        s = "abc"

        actual = stringProblems.StringProblems.is_all_unique_chars(s)
        
        self.assertEqual(expected, actual)

    def test_ReturnsFalseWhenStringIsNotAllUniqueChars(self):
        expected = False
        s = "abcdefa"

        actual = stringProblems.StringProblems.is_all_unique_chars(s)
        
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()
