import bubbleSortSorter
import docdist1

# Expected test results
#File t1.verne.txt : 1057 lines, 8943 words, 2150 distinct words
#File t2.bobsey.txt : 6667 lines, 49785 words, 3354 distinct words
#The distance between the documents is: 0.582949 (radians)

docdist1.documentDist("t1.verne.txt", "t2.bobsey.txt", bubbleSortSorter.BubbleSortSorter())

input('Press Enter to exit')
