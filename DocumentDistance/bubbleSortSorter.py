import sorter

class BubbleSortSorter(sorter.Sorter):
    """Bubble sort sorting algorithm."""
    def __bubbleSortHelper(self, data):
        swappedAnElement = False;

        for i in range(len(data) - 1):
            if self.__shouldSwap(data[i][0], data[i + 1][0]):
                temp = data[i]
                data[i] = data[i + 1]
                data[i + 1] = temp
                swappedAnElement = True

        return swappedAnElement

    def __shouldSwap(self, item1, item2):
        if item1 > item2:
            return True

        return False

    def sort_words(self, wordList):
        """Sorts the words using bubble sort algorithm.
        Result is an in-place sort."""
        while self.__bubbleSortHelper(wordList) == True:
            pass
