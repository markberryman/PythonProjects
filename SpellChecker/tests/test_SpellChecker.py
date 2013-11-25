import spellChecker
import unittest


class Test_TrimWordList(unittest.TestCase):
    def test_TrimByWordSize(self):
        word_list = { "a", "aa" }
        word = "a"
        expected = { "a" }

        actual = spellChecker.SpellChecker.trim_word_list(word, word_list)

        self.assertEqual(expected, actual)

    def test_TrimWordStartingWithConsonant(self):
        word_list = { "b", "c" }
        word = "b"
        expected = { "b" }

        actual = spellChecker.SpellChecker.trim_word_list(word, word_list)

        self.assertEqual(expected, actual)

    def test_TrimWordStartingWithVowel(self):
        word_list = { "a", "c" }
        word = "e"
        expected = { "a" }

        actual = spellChecker.SpellChecker.trim_word_list(word, word_list)

        self.assertEqual(expected, actual)


class Test_CreateSuggestions(unittest.TestCase):
    def test_WordWithSingleVowelChar(self):
        word_to_check = "a"
        expected = { "a", "e", "i", "o", "u" }

        actual = spellChecker.SpellChecker.create_suggestions(word_to_check)

        self.assertEqual(expected, actual)

    def test_WordWithTwoRepeatedChars(self):
        word_to_check = "xx"
        expected = { "xx", "x" }

        actual = spellChecker.SpellChecker.create_suggestions(word_to_check)

        self.assertEqual(expected, actual)

    def test_WordWithOneVowelAndTwoRepeatedChars(self):
        word_to_check = "axx"
        expected = { "axx", "ax", "exx", "ex", "ixx", "ix", "oxx", "ox", "uxx", "ux" }

        actual = spellChecker.SpellChecker.create_suggestions(word_to_check)

        self.assertEqual(expected, actual)


class Test_CreateRepeatedLettersVariationsHelper(unittest.TestCase):
    def test_WordWithTwoRepeatedLetters(self):
        word_to_check = "xx"
        expected = { "x" }
        
        actual = spellChecker.SpellChecker.create_repeated_letters_variations_helper(
            word_to_check, 1, 2)

        self.assertEqual(expected, actual)

    def test_WordWithThreeRepeatedLetters(self):
        word_to_check = "xxx"
        expected = { "x", "xx" }
        
        actual = spellChecker.SpellChecker.create_repeated_letters_variations_helper(
            word_to_check, 2, 3)

        self.assertEqual(expected, actual)

    def test_WordWithTwoRepeatedLettersNonRepeatedCharsAfter(self):
        word_to_check = "xxA"
        expected = { "xA" }
        
        actual = spellChecker.SpellChecker.create_repeated_letters_variations_helper(
            word_to_check, 1, 2)

        self.assertEqual(expected, actual)

    def test_WordWithTwoRepeatedLettersNonRepeatedCharsBeforeAndAfter(self):
        word_to_check = "AxxB"
        expected = { "AxB" }
        
        actual = spellChecker.SpellChecker.create_repeated_letters_variations_helper(
            word_to_check, 2, 2)

        self.assertEqual(expected, actual)


class Test_CreateRepeatedLettersVariations(unittest.TestCase):
    def test_WordWithNoRepeatedLetters(self):
        word_to_check = "x"
        expected = { "x" }

        actual = spellChecker.SpellChecker.create_repeated_letters_variations(
            word_to_check)

        self.assertEqual(expected, actual)

    def test_WordWithOneSequenceOfTwoRepeatedLetters(self):
        word_to_check = "xx"
        expected = { "x", "xx" }

        actual = spellChecker.SpellChecker.create_repeated_letters_variations(
            word_to_check)

        self.assertEqual(expected, actual)

    def test_WordWithOneSequenceOfTwoRepeatedLettersFollowedByNonRepeatingLetters(self):
        word_to_check = "xxA"
        expected = { "xA", "xxA" }

        actual = spellChecker.SpellChecker.create_repeated_letters_variations(
            word_to_check)

        self.assertEqual(expected, actual)

    def test_WordWithTwoSequencesOfRepeatedLetters(self):
        word_to_check = "xxyy"
        expected = { "xyy", "xxyy", "xxy", "xy" }

        actual = spellChecker.SpellChecker.create_repeated_letters_variations(
            word_to_check)

        self.assertEqual(expected, actual)

    def test_WordWithTwoSequencesOfRepeatedLettersAndNonRepeatedCharsMixedIn(self):
        word_to_check = "AxxByyC"
        expected = { "AxByyC", "AxxByyC", "AxxByC", "AxByC" }

        actual = spellChecker.SpellChecker.create_repeated_letters_variations(
            word_to_check)

        self.assertEqual(expected, actual)


class Test_CreateVowelVariationsHelper(unittest.TestCase):
    def test_WordWithOneVowel(self):
        word = "XaY"
        expected = { "XaY", "XeY", "XiY", "XoY", "XuY" }

        actual = spellChecker.SpellChecker.create_vowel_variations_helper(word, 1)

        self.assertEqual(expected, actual)


class Test_CreateVowelVariations(unittest.TestCase):
    def test_WordWithNoVowels(self):
        word = "x"
        expected = { "x" }

        actual = spellChecker.SpellChecker.create_vowel_variations(word)

        self.assertEqual(expected, actual)

    def test_WordWithJustOneVowel(self):
        word = "a"
        expected = { "a", "e", "i", "o", "u" }

        actual = spellChecker.SpellChecker.create_vowel_variations(word)

        self.assertEqual(expected, actual)

    def test_WordWithOneVowelConsonantsTrailing(self):
        word = "ax"
        expected = { "ax", "ex", "ix", "ox", "ux" }

        actual = spellChecker.SpellChecker.create_vowel_variations(word)

        self.assertEqual(expected, actual)

    def test_WordWithOneVowelConsonantsBefore(self):
        word = "xa"
        expected = { "xa", "xe", "xi", "xo", "xu" }

        actual = spellChecker.SpellChecker.create_vowel_variations(word)

        self.assertEqual(expected, actual)
    
    def test_WordWithTwoVowels(self):
        word = "ae"
        expected = { "aa", "ae", "ai", "ao", "au",
                     "ea", "ee", "ei", "eo", "eu",
                     "ia", "ie", "ii", "io", "iu",
                     "oa", "oe", "oi", "oo", "ou",
                     "ua", "ue", "ui", "uo", "uu" }

        actual = spellChecker.SpellChecker.create_vowel_variations(word)

        self.assertEqual(expected, actual)


class Test_CheckWord(unittest.TestCase):
    def test_ReturnsWordWhenOnlyCaseDiffers(self):
        word_dict = { "Ab" }
        word = "ab"
        expected = "Ab"

        actual = spellChecker.SpellChecker.check_word(word, word_dict)

        self.assertEqual(expected, actual)
    
    def test_ReturnsNoneWhenWordDiffersByMoreThanCase(self):
        word_dict = { "a" }
        word = "b"
        expected = None

        actual = spellChecker.SpellChecker.check_word(word, word_dict)

        self.assertEqual(expected, actual)
            

if __name__ == '__main__':
    unittest.main()
