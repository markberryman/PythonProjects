import stringProblems
import unittest


class RemoveDupes(unittest.TestCase):
    def test_NoneString(self):
        s = None
        expected = None

        actual = stringProblems.StringProblems.remove_dupes(s)

        self.assertEqual(expected, actual)

    def test_OneCharString(self):
        s = ['a']
        expected = ['a']

        actual = stringProblems.StringProblems.remove_dupes(s)

        self.assertEqual(expected, actual)

    def test_TwoCharStringNoDupes(self):
        s = ['a', 'b']
        expected = ['a', 'b']

        actual = stringProblems.StringProblems.remove_dupes(s)

        self.assertEqual(expected, actual)

    def test_TwoCharStringWithDupes(self):
        s = ['a', 'a']
        expected = ['a']

        actual = stringProblems.StringProblems.remove_dupes(s)

        self.assertEqual(expected, actual)

    def test_ThreeCharStringAllDupes(self):
        s = ['a', 'a', 'a']
        expected = ['a']

        actual = stringProblems.StringProblems.remove_dupes(s)

        self.assertEqual(expected, actual)

    def test_FourCharStringStringWithPairOfDupes(self):
        s = ['a', 'a', 'b', 'b']
        expected = ['a', 'b']

        actual = stringProblems.StringProblems.remove_dupes(s)

        self.assertEqual(expected, actual)

    def test_LongStringWithSpreadOutDupes(self):
        s = ['a', 'b', 'c', 'b', 'a', 'c', 'd', 'a']
        expected = ['a', 'b', 'c', 'd']

        actual = stringProblems.StringProblems.remove_dupes(s)

        self.assertEqual(expected, actual)


class ReverseString(unittest.TestCase):
    def test_ReversesOneCharString(self):
        s = ['a']
        expected = ['a']
        
        stringProblems.StringProblems.reverse_string(s)

        self.assertEqual(expected, s)

    def test_ReversesTwoCharString(self):
        s = ['a', 'b']
        expected = ['b', 'a']
        
        stringProblems.StringProblems.reverse_string(s)

        self.assertEqual(expected, s)


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
