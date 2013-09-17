import math


class AngleMetricCalculator(object):
    """Calculates the angle metric b/w two word lists."""

    def calc_inner_product(self, wordFreqs1, wordFreqs2):
        """Calculate the inner (or dot) product of the two vectors 
        representing word frequencies. The calculation is the summation 
        of multiplying corresponding elements from each vector.

        Helps if the lists of word frequencies are ordered. Otherwise,
        we're headed to an O(n^2) algorithm here.
        """
        innerProduct = 0

        for word1, freq1 in wordFreqs1:
            for word2, freq2 in wordFreqs2:
                if (word2 == word1):
                    innerProduct += freq1 * freq2
                    break

        return innerProduct

    def calc_vector_angle(self, wordFreqs1, wordFreqs2):
        """Calculate the angle b/w two vectors. The angle is the arccos
        of their inner product divided by the product of their norms
        which can be restated as the square root of their inner
        products."""
        numerator = self.calc_inner_product(wordFreqs1, wordFreqs2)
        denominator = math.sqrt(
            self.calc_inner_product(wordFreqs1, wordFreqs1) * 
            self.calc_inner_product(wordFreqs2, wordFreqs2))
         
        return math.acos(numerator / denominator)
