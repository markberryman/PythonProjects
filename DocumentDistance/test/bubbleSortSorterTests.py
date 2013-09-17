import bubbleSortSorter
import unittest


class BubbleSortSorterTests(unittest.TestCase):
    def test_SortsTwoElementWordList(self):
        wordTuple1 = ("a", 1)
        wordTuple2 = ("b", 1)
        wordList = [wordTuple2, wordTuple1]
        sut = bubbleSortSorter.BubbleSortSorter()

        sut.sort_words(wordList)

        self.assertEqual(wordTuple1, wordList[0])
        

if __name__ == '__main__':
    unittest.main()
