import math


class AngleMetricCalculator(object):
    """Calculates the angle metric b/w two word lists."""

    def calc_inner_product(self, wordFreqs1, wordFreqs2):
        """Calculate the inner (or dot) product of the two vectors 
        representing word frequencies. The calculation is the summation 
        of multiplying corresponding elements from each vector.

        Word frequency lists must be ordered.
        """
        innerProduct = 0
        
        for word1, freq1 in wordFreqs1:
            secondWordFreqIndex = 0
            
            while ((secondWordFreqIndex < len(wordFreqs2)) and
                    (wordFreqs2[secondWordFreqIndex][0] != word1)):
                secondWordFreqIndex += 1

            if (secondWordFreqIndex != len(wordFreqs2)):
                innerProduct += wordFreqs2[secondWordFreqIndex][1] * freq1
                secondWordFreqIndex += 1
            # else, ran off the end of the list

        return innerProduct

    def calc_vector_angle(self, wordFreqs1, wordFreqs2):
        """Calculate the angle b/w two vectors. The angle is the arccos
        of their inner product divided by the product of their norms
        which can be restated as the square root of their inner
        products."""
        wordFreqs1 = list(wordFreqs1.items())
        wordFreqs2 = list(wordFreqs2.items())
        numerator = self.calc_inner_product(wordFreqs1, wordFreqs2)
        denominator = math.sqrt(
            self.calc_inner_product(wordFreqs1, wordFreqs1) * 
            self.calc_inner_product(wordFreqs2, wordFreqs2))
         
        return math.acos(numerator / denominator)
