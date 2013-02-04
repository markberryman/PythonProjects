import math
import profile
import re

# program based on assignment:
# http://ocw.mit.edu/ans7870/6/6.006/s08/lecturenotes/dd_prog1.htm
def documentDist(fileName1, fileName2):
    wordListForFile1 = generateWordList(fileName1)
    wordFrequencyListFile1 = generateWordFrequenciesForFile(wordListForFile1)
    sortWordFrequencyList(wordFrequencyListFile1)

    print "File {0} : {1} words, {2} distinct words".format(fileName1, len(wordListForFile1),
                                                            len(wordFrequencyListFile1))

    wordListForFile2 = generateWordList(fileName2)
    wordFrequencyListFile2 = generateWordFrequenciesForFile(wordListForFile2)
    sortWordFrequencyList(wordFrequencyListFile2)

    print "File {0} : {1} words, {2} distinct words".format(fileName2, len(wordListForFile2),
                                                            len(wordFrequencyListFile2))
    
    angleMetric = calculateAngleMetric(wordFrequencyListFile1, wordFrequencyListFile2)
    
    print "The distance between the documents is: {0} radians".format(angleMetric)

def generateWordList(fileName):
    file = open(fileName, "r")
    
    wordList = []

    for line in file:
        wordsInLine = re.findall(r"[\w]+", line.lower())
        wordList = wordList + wordsInLine

    return wordList

def generateWordFrequenciesForFile(wordList):
    wordFrequencyList = []

    for word in wordList:
        foundWord = False

        for wordFrequency in wordFrequencyList:
            if wordFrequency[0] == word:
                wordFrequency[1] += 1
                foundWord = True

        if foundWord == False:
            wordFrequencyList = wordFrequencyList + [[word, 1]]    

    return wordFrequencyList

def sortWordFrequencyList(wordFrequencyList):
    bubbleSortCount = 0

    while bubbleSort(wordFrequencyList) == True:
        bubbleSortCount += 1

    return wordFrequencyList

##################
# bubble sort land
##################
def bubbleSort(data):
    swappedAnElement = False;

    for i in range(len(data) - 1):
        if shouldSwap(data[i][0], data[i + 1][0]):
            temp = data[i]
            data[i] = data[i + 1]
            data[i + 1] = temp
            swappedAnElement = True

    return swappedAnElement

def shouldSwap(item1, item2):
    if item1 > item2:
        return True

    return False

#########################
# end of bubble sort land
#########################

# d1 . d2 = summation across w of d1(w)*d2(w) where w is a common word
def calculateDotProductOfWordlists(wordList1, wordList2):
    result = 0
    
    for wordFrequencyFromList1 in wordList1:
        for wordFrequencyFromList2 in wordList2:
            if wordFrequencyFromList1[0] == wordFrequencyFromList2[0]:
                result = result + (wordFrequencyFromList1[1] * wordFrequencyFromList2[1])

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

# Expected test results
#File t1.verne.txt : 1057 lines, 8943 words, 2150 distinct words
#File t2.bobsey.txt : 6667 lines, 49785 words, 3354 distinct words
#The distance between the documents is: 0.582949 (radians)