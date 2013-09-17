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

if __name__ == '__main__':
    unittest.main()
