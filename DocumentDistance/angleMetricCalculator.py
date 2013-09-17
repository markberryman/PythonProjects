import math


class AngleMetricCalculator(object):
    """Calculates the angle metric b/w two word lists."""

    def calc_norm(self, listOfWordFrequencies):
        """Calculate the norm of a vector composed of word frequencies.
        Norm is calculated as the square root of D dot product D."""
        dotProduct = 0

        for freq in listOfWordFrequencies:
            dotProduct += freq * freq

        norm = math.sqrt(dotProduct)

        return norm
    
    def calc_inner_product(self, wordFreqs1, wordFreqs2):
        """Calculate the inner (or dot) product of the two vectors 
        representing word frequencies. The calculation is the summation 
        of multiplying corresponding elements from each vector."""
        shorterList = wordFreqs1 if (len(wordFreqs1) < len(wordFreqs2)) else wordFreqs2
        innerProduct = 0

        # any values in one list that don't have a corresponding match
        # in the other equal zero so we ignore them
        for idx, val in enumerate(shorterList):
            innerProduct += wordFreqs1[idx] * wordFreqs2[idx]

        return innerProduct

    def calc_vector_angle(self, wordFreqs1, wordFreqs2):
        """Calculate the angle b/w two vectors. The angle is the arccos
        of their inner product divided by the product of their norms."""
        innerProduct = self.calc_inner_product(wordFreqs1, wordFreqs2)
        wordFreqs1Norm = self.calc_norm(wordFreqs1)
        wordFreqs2Norm = self.calc_norm(wordFreqs2)

        return math.acos(innerProduct / (wordFreqs1Norm * wordFreqs2Norm))
