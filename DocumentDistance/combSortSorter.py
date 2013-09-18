import bubbleSortSorter
import sorter


class CombSortSorter(sorter.Sorter):
    """Sorter using comb sort algorithm."""
    # comb sort explained - http://en.wikipedia.org/wiki/Comb_sort
    # in short, variant of bubble wort whereby instead of
    # comparing two elements that are next to each other (gap of 1),
    # we compare paris of elements that are further apart
    # this helps w/ input scenarios where small values are at the
    # end of the list which tanks the perf of bubble sort

    def sort_words(self, wordTuples):
        shrinkFactor = 1.333
        dataLength = len(wordTuples)
        gap = int(dataLength / shrinkFactor)

        if (gap < 1):
            gap = 1

        while (gap != 1):
            i = 0

            while ((i + gap) < dataLength):
                if (wordTuples[i][0] > wordTuples[i + gap][0]):
                    temp = wordTuples[i]
                    wordTuples[i] = wordTuples[i + gap]
                    wordTuples[i + gap] = temp

                i += 1            

            gap = int(gap / shrinkFactor)

        # we were reduced to bubble sort for this last pass
        bubbleSortSorter.BubbleSortSorter().sort_words(wordTuples)