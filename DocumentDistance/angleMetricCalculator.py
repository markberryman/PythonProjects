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