import combSortSorter
import unittest


class CombSortSorterTests(unittest.TestCase):
    def test_SortsOneElementWordList(self):
        wordTuple1 = ("a", 1)
        wordList = [wordTuple1]
        sut = combSortSorter.CombSortSorter()

        sut.sort_words(wordList)

        self.assertEqual(wordTuple1, wordList[0])
        
    def test_SortsTwoElementWordList(self):
        wordTuple1 = ("a", 1)
        wordTuple2 = ("b", 1)
        wordList = [wordTuple2, wordTuple1]
        sut = combSortSorter.CombSortSorter()

        sut.sort_words(wordList)

        self.assertEqual(wordTuple1, wordList[0])

    def test_SortsFiveElementWordList(self):
        wordTuple1 = ("a", 1)
        wordTuple2 = ("b", 1)
        wordTuple3 = ("c", 1)
        wordTuple4 = ("d", 1)
        wordTuple5 = ("e", 1)        
        wordList = [wordTuple5, wordTuple4, wordTuple3, wordTuple2, wordTuple1]
        sut = combSortSorter.CombSortSorter()

        sut.sort_words(wordList)

        self.assertEqual(wordTuple1, wordList[0])


if __name__ == '__main__':
    unittest.main()
