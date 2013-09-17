class WordFrequencyCalculator(object):
    """Abstract class for tallying word frequencies
    from a list of words."""
    def calculate_word_frequency(self, wordList):
        raise NotImplementedError()


class MyWordFrequencyCalculator(WordFrequencyCalculator):
    def calculate_word_frequency(self, wordList):
        """Returns a dictionary of (word, word count)
        for the list of words provided."""
        freqDict = {}

        for word in wordList:
            if (word in freqDict):
                freqDict[word] = freqDict[word] + 1
            else:
                freqDict[word] = 1

        return freqDict