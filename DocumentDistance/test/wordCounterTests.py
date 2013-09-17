import wordCounter
import unittest


class SimpleWordCounterTests(unittest.TestCase):
    def test_CountWordsReturnsCorrectCountOfWordsInVerne(self):
        filename = "../t1.verne.txt"
        sut = wordCounter.SimpleWordCounter()
        input = sut.read_file(filename)

        result = sut.count_words(input)

        self.assertEqual(8943, len(result))

    def test_CountWordsReturnsCorrectCountOfWordsInBobsey(self):
        filename = "../t2.bobsey.txt"
        sut = wordCounter.SimpleWordCounter()
        input = sut.read_file(filename)

        result = sut.count_words(input)

        self.assertEqual(49785, len(result))

    def test_CountWordsReturnsCorrectCountOfWordsInLewis(self):
        filename = "../t3.lewis.txt"
        sut = wordCounter.SimpleWordCounter()
        input = sut.read_file(filename)

        result = sut.count_words(input)

        self.assertEqual(182355, len(result))


if __name__ == '__main__':
    unittest.main()
