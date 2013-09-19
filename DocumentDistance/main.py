#import bubbleSortSorter
#import combSortSorter
import mergeSortSorter
import docdist1

#docdist1.documentDist("t1.verne.txt", "t2.bobsey.txt", bubbleSortSorter.BubbleSortSorter())
#docdist1.documentDist("t1.verne.txt", "t2.bobsey.txt", combSortSorter.CombSortSorter())
#docdist1.documentDist("t1.verne.txt", "t2.bobsey.txt", mergeSortSorter.MergeSortSorter())

docdist1.documentDist("t2.bobsey.txt", "t3.lewis.txt", mergeSortSorter.MergeSortSorter())

input('Press Enter to exit')
