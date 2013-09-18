import math


class AngleMetricCalculator(object):
    """Calculates the angle metric b/w two word lists."""

    def calc_inner_product(self, list1, list2):
        """Calculate the inner (or dot) product of the two vectors 
        representing word frequencies. The calculation is the summation 
        of multiplying matching words from each vector.

        Word frequency lists must be ordered.
        """
        list1Idx = 0
        list2Idx = 0
        innerProduct = 0

        # loop until either list runs out of words
        while ((list1Idx < len(list1)) and (list2Idx < len(list2))):
            # compare words at current indices
            if (list1[list1Idx][0] == list2[list2Idx][0]):
                # if match, calc product, advance both indices
                innerProduct += list1[list1Idx][1] * list2[list2Idx][1]
                list1Idx += 1
                list2Idx += 1
            else:
                # if no match, move index for list w/ word that is "less"
                if (list1[list1Idx][0] < list2[list2Idx][0]):
                    list1Idx += 1
                else:
                    list2Idx += 1

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
