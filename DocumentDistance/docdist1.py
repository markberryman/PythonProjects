import angleMetricCalculator
import wordCounter
import wordFrequencyCalculator

# program based on assignment:
# http://ocw.mit.edu/ans7870/6/6.006/s08/lecturenotes/dd_prog1.htm
def documentDist(fileName1, fileName2, sortingAlgo):
    theWordCounter = wordCounter.MyRegexWordCounter()
    freqCounter = wordFrequencyCalculator.MyWordFrequencyCalculator()
    
    inputLines = theWordCounter.read_file(fileName1)
    wordListForFile1 = theWordCounter.count_words(inputLines)
    wordFrequencyListFile1 = list(freqCounter.calculate_word_frequency(wordListForFile1).items())
    sortingAlgo.sort_words(wordFrequencyListFile1)

    print("File {0} : {1} words, {2} distinct words".format(fileName1, len(wordListForFile1),
                                                            len(wordFrequencyListFile1)))

    inputLines = theWordCounter.read_file(fileName2)
    wordListForFile2 = theWordCounter.count_words(inputLines)
    wordFrequencyListFile2 = list(freqCounter.calculate_word_frequency(wordListForFile2).items())
    sortingAlgo.sort_words(wordFrequencyListFile2)

    print("File {0} : {1} words, {2} distinct words".format(fileName2, len(wordListForFile2),
                                                            len(wordFrequencyListFile2)))
    
    angleMetricCalc = angleMetricCalculator.AngleMetricCalculator()
    angleMetric = angleMetricCalc.calc_vector_angle(wordFrequencyListFile1, wordFrequencyListFile2)
    
    print("The distance between the documents is: {0} radians".format(round(angleMetric, 6)))


######################
# merge sort sort land
######################
def mergeSort(list):
    if (len(list) == 1):
        return list

    splitIndex = len(list) // 2
    list1 = list[:splitIndex]
    list2 = list[splitIndex:]

    return mergeSortSorter(mergeSort(list1), mergeSort(list2))

def mergeSortSorter(list1, list2):
    list1Index = 0
    list2Index = 0

    newList = []

    lengthList1 = len(list1)
    lengthList2 = len(list2)

    while ((list1Index < lengthList1) and (list2Index < lengthList2)):
        if (list1[list1Index][0] < list2[list2Index][0]):
            newList.append(list1[list1Index])
            list1Index += 1
        else:
            newList.append(list2[list2Index])
            list2Index += 1
            
    if (list1Index < lengthList1):
        newList.extend(list1[list1Index:])
    else:
        newList.extend(list2[list2Index:])

    return newList

#############################
# end of merge sort sort land
#############################
