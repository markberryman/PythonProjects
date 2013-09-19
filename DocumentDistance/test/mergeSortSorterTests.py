import mergeSortSorter
import unittest


class SortWordsTests(unittest.TestCase):
    def test_SortsOneElementWordList(self):
        wordTuple1 = ("a", 1)
        wordList = [wordTuple1]
        sut = mergeSortSorter.MergeSortSorter()

        result = sut.sort_words(wordList)

        self.assertEqual(wordTuple1, result[0])
        
    def test_SortsTwoElementWordList(self):
        wordTuple1 = ("a", 1)
        wordTuple2 = ("b", 1)
        wordList = [wordTuple2, wordTuple1]
        sut = mergeSortSorter.MergeSortSorter()

        result = sut.sort_words(wordList)

        self.assertEqual(wordTuple1, result[0])

    def test_SortsThreeElementWordList(self):
        wordTuple1 = ("a", 1)
        wordTuple2 = ("b", 1)
        wordTuple3 = ("c", 1)
        wordList = [wordTuple3, wordTuple2, wordTuple1]
        sut = mergeSortSorter.MergeSortSorter()

        result = sut.sort_words(wordList)

        self.assertEqual(wordTuple1, result[0])
        self.assertEqual(wordTuple2, result[1])
        self.assertEqual(wordTuple3, result[2])

    def test_SortsFiveElementWordList(self):
        wordTuple1 = ("a", 1)
        wordTuple2 = ("b", 1)
        wordTuple3 = ("c", 1)
        wordTuple4 = ("d", 1)
        wordTuple5 = ("e", 1)        
        wordList = [wordTuple5, wordTuple4, wordTuple3, wordTuple2, wordTuple1]
        sut = mergeSortSorter.MergeSortSorter()

        result = sut.sort_words(wordList)

        self.assertEqual(wordTuple1, result[0])
        self.assertEqual(wordTuple2, result[1])
        self.assertEqual(wordTuple3, result[2])
        self.assertEqual(wordTuple4, result[3])
        self.assertEqual(wordTuple5, result[4])

if __name__ == '__main__':
    unittest.main()
