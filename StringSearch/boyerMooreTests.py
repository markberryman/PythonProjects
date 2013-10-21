import boyerMoore
import unittest


class BoyerMoore_SearchTests(unittest.TestCase):
    def test_PatternNotInText(self):
        sut = boyerMoore.BoyerMoore()
        expected = False

        actual = boyerMoore.BoyerMoore.search("x", "y")

        self.assertEqual(expected, actual)

    def test_PatternInText(self):
        sut = boyerMoore.BoyerMoore()
        expected = True

        actual = boyerMoore.BoyerMoore.search("x", "x")

        self.assertEqual(expected, actual)

    def test_PatternAtStartOfText(self):
        sut = boyerMoore.BoyerMoore()
        expected = True

        actual = boyerMoore.BoyerMoore.search("ab", "abc")

        self.assertEqual(expected, actual)

    def test_PatternInMiddleOfText(self):
        sut = boyerMoore.BoyerMoore()
        expected = True

        actual = boyerMoore.BoyerMoore.search("ab", "xyzab123")

        self.assertEqual(expected, actual)

    def test_PatternAtEndOfText(self):
        sut = boyerMoore.BoyerMoore()
        expected = True

        actual = boyerMoore.BoyerMoore.search("ab", "xyzab")

        self.assertEqual(expected, actual)

    def test_PatternPartialMatchButNotFullMatch(self):
        sut = boyerMoore.BoyerMoore()
        expected = False

        actual = boyerMoore.BoyerMoore.search("abc", "abxbc")

        self.assertEqual(expected, actual)

    def test_PatternMatchAndPartialShifting(self):
        sut = boyerMoore.BoyerMoore()
        expected = True

        actual = boyerMoore.BoyerMoore.search("abc", "abbabc")

        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()
