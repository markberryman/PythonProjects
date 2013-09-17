import angleMetricCalculator
import math
import unittest


class CalcNormTests(unittest.TestCase):
    def test_NormOfOneWordFrequency(self):
        wordFreqs = [2]
        sut = angleMetricCalculator.AngleMetricCalculator()

        result = sut.calc_norm(wordFreqs)
        
        self.assertEqual(2, result)

    def test_NormOfTwoWordFrequencies(self):
        wordFreqs = [2, 3]
        sut = angleMetricCalculator.AngleMetricCalculator()

        result = sut.calc_norm(wordFreqs)
        
        self.assertEqual(math.sqrt(13), result)


class CalcInnerProductTests(unittest.TestCase):
    def test_InnerProductOfTwoWordFreqListsWithSameSize(self):
        wordFreqs1 = [1, 2]
        wordFreqs2 = [2, 3]
        sut = angleMetricCalculator.AngleMetricCalculator()

        result = sut.calc_inner_product(wordFreqs1, wordFreqs2)

        self.assertEqual(8, result)

    def test_InnerProductOfTwoWordFreqListsWithDiffSize(self):
        wordFreqs1 = [1]
        wordFreqs2 = [2, 3]
        sut = angleMetricCalculator.AngleMetricCalculator()

        result = sut.calc_inner_product(wordFreqs1, wordFreqs2)

        self.assertEqual(2, result)

class CalcVectorAngleTests(unittest.TestCase):
    def test_BasicVectorAngleCalc(self):
        # "To be or not to be" and "Doubt truth to be a liar"
        # common words in each: "to be"
        wordFreq1 = [2, 2]
        wordFreq2 = [1, 1]
        sut = angleMetricCalculator.AngleMetricCalculator()

        result = sut.calc_vector_angle(wordFreq1, wordFreq2)

        self.assertEqual(1.028, result)


if __name__ == '__main__':
    unittest.main()
