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

    def calc_inner_product(self, listOfWordFrequencies1, listOfWordFrequencies2):
        """Calculate the inner (or dot) product of the two vectors 
        representing word frequencies. The calculation is the summation 
        of multiplying corresponding elements from each vector."""
        length1 = len(listOfWordFrequencies1)
        length2 = len(listOfWordFrequencies2)
        innerProduct = 0

        # any values in one list that don't have a corresponding match
        # in the other equal zero so we ignore them
        if (length1 < length2):
            for idx, val in enumerate(listOfWordFrequencies1):
                innerProduct += listOfWordFrequencies1[idx] * listOfWordFrequencies2[idx]
        else:
            for idx, val in enumerate(listOfWordFrequencies2):
                innerProduct += listOfWordFrequencies1[idx] * listOfWordFrequencies2[idx]

        return innerProduct