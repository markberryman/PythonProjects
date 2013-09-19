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
    
    print("File {0} : {1} words, {2} distinct words".format(fileName1, len(wordListForFile1),
                                                            len(wordFrequencyListFile1)))

    inputLines = theWordCounter.read_file(fileName2)
    wordListForFile2 = theWordCounter.count_words(inputLines)
    wordFrequencyListFile2 = list(freqCounter.calculate_word_frequency(wordListForFile2).items())
    
    print("File {0} : {1} words, {2} distinct words".format(fileName2, len(wordListForFile2),
                                                            len(wordFrequencyListFile2)))
    
    angleMetricCalc = angleMetricCalculator.AngleMetricCalculator()
    sortedWordFreqList1 = sortingAlgo.sort_words(wordFrequencyListFile1)
    sortedWordFreqList2 = sortingAlgo.sort_words(wordFrequencyListFile2)
    angleMetric = angleMetricCalc.calc_vector_angle(sortedWordFreqList1, sortedWordFreqList2)
    
    print("The distance between the documents is: {0} radians".format(round(angleMetric, 6)))
