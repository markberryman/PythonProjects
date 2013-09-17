import wordFrequencyCalculator
import unittest


class CalculateWordFrequencyTests(unittest.TestCase):
    def test_WordListWithNoRepeats(self):
        wordList = ["a", "b"]
        sut = wordFrequencyCalculator.MyWordFrequencyCalculator()

        result = sut.calculate_word_frequency(wordList)

        self.assertEqual(2, len(result))
        self.assertEqual(1, result["a"])
        self.assertEqual(1, result["b"])

    def test_WordListWithRepeats(self):
        wordList = ["a", "b", "a"]
        sut = wordFrequencyCalculator.MyWordFrequencyCalculator()

        result = sut.calculate_word_frequency(wordList)

        self.assertEqual(2, len(result))
        self.assertEqual(2, result["a"])
        self.assertEqual(1, result["b"])

if __name__ == '__main__':
    unittest.main()
