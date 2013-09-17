import math
import wordCounter
import wordFrequencyCalculator

# program based on assignment:
# http://ocw.mit.edu/ans7870/6/6.006/s08/lecturenotes/dd_prog1.htm
def documentDist(fileName1, fileName2, sortingAlgo):
    theWordCounter = wordCounter.MyRegexWordCounter()
    freqCounter = wordFrequencyCalculator.MyWordFrequencyCalculator()
    
    inputLines = theWordCounter.read_file(fileName1)
    wordListForFile1 = theWordCounter.count_words(inputLines)
    wordFrequencyListFile1 = freqCounter.calculate_word_frequency(wordListForFile1)
    sortingAlgo.sort_words(list(wordFrequencyListFile1.items()))

    print("File {0} : {1} words, {2} distinct words".format(fileName1, len(wordListForFile1),
                                                            len(wordFrequencyListFile1)))

    inputLines = theWordCounter.read_file(fileName2)
    wordListForFile2 = theWordCounter.count_words(inputLines)
    wordFrequencyListFile2 = freqCounter.calculate_word_frequency(wordListForFile2)
    sortingAlgo.sort_words(list(wordFrequencyListFile2.items()))

    print("File {0} : {1} words, {2} distinct words".format(fileName2, len(wordListForFile2),
                                                            len(wordFrequencyListFile2)))
    
    #angleMetric = calculateAngleMetric(wordFrequencyListFile1, wordFrequencyListFile2)
    
    #print("The distance between the documents is: {0} radians".format(angleMetric))


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

#####################
# comb sort sort land
#####################
def combSort(data):
    shrinkFactor = 1.333
    dataLength = len(data)
    gap = int(dataLength / shrinkFactor)
    swapped = True

    while (((gap == 1) and (swapped == False)) == False):
        swapped = False
        i = 0
        while ((i + gap) < dataLength):
            if (data[i][0] > data[i + gap][0]):
                temp = data[i]
                data[i] = data[i + gap]
                data[i + gap] = temp
                swapped = True
            i += 1            

        gap = int(gap / shrinkFactor)
        if (gap < 1):
            gap = 1

############################
# end of comb sort sort land
############################

# d1 . d2 = summation across w of d1(w)*d2(w) where w is a common word
def calculateDotProductOfWordlists(wordList1, wordList2):
    result = 0
    
    #for wordFrequencyFromList1 in wordList1:
    #    for wordFrequencyFromList2 in wordList2:
    #        if wordFrequencyFromList1[0] == wordFrequencyFromList2[0]:
    #            result = result + (wordFrequencyFromList1[1] * wordFrequencyFromList2[1])

    # surprisingly, i'm not getting much perf benefit from this slightly
    # optimized processing of the word lists compared to the simple nested
    # for loop above
    wordList1Index = 0
    wordList2Index = 0

    wordList1Length = len(wordList1)
    wordList2Length = len(wordList2)

    while ((wordList1Index < wordList1Length) and (wordList2Index < wordList2Length)):
        wordFrequency1 = wordList1[wordList1Index]
        wordFrequency2 = wordList2[wordList2Index]
        if (wordFrequency1[0] == wordFrequency2[0]):
            result = result + (wordFrequency1[1] * wordFrequency2[1])
            wordList1Index += 1
            wordList2Index += 1
        else:
            if (wordFrequency1[0] < wordFrequency2[0]):
                wordList1Index += 1
            else:
                wordList2Index += 1

    return result


def calculateDistanceMetric(wordList1, wordList2):
    result = calculateDotProductOfWordlists(wordList1, wordList2)

    return result

# the magnitude (or length) or a wordlist is the square root of the dot product
# of the wordlist with itself
def calculateMagnitude(wordList1):
    result = math.sqrt(calculateDotProductOfWordlists(wordList1, wordList1))
    return result

# The angle between the vectors D1 and D2 (the wordlists) gives an indication of overlap 
# between the 2 documents. Mathematically this angle is expressed as:
# arccos((D1 . D2) / ||D1|| * ||D2||)
def calculateAngleMetric(wordList1, wordList2):
    distanceMetric = calculateDistanceMetric(wordList1, wordList2)
    wordList1Magnitude = calculateMagnitude(wordList1)
    wordList2Magnitude = calculateMagnitude(wordList2)

    tempresult = distanceMetric / (wordList1Magnitude * wordList2Magnitude)
    # rounding to 15 digits after the decimal point to keep the value range
    # within -1 <= x <= 1; run in to values just outside this range when
    # dealing with identical documents or documents with no common words
    result = math.acos(round(tempresult, 15))

    return result
