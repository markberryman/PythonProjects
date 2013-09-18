import angleMetricCalculator
import unittest


class CalcInnerProductTests(unittest.TestCase):
    def test_InnerProductOfTwoWordFreqListsSameSize(self):
        wordFreqs1 = [("a", 1), ("b", 2)]
        wordFreqs2 = [("a", 2), ("b", 3)]
        sut = angleMetricCalculator.AngleMetricCalculator()

        result = sut.calc_inner_product(wordFreqs1, wordFreqs2)

        self.assertEqual(8, result)

    def test_InnerProductOfTwoWordFreqListsDiffSize(self):
        wordFreqs1 = [("a", 1), ("b", 2)]
        wordFreqs2 = [("b", 3)]
        sut = angleMetricCalculator.AngleMetricCalculator()

        result = sut.calc_inner_product(wordFreqs1, wordFreqs2)

        self.assertEqual(6, result)

class CalcVectorAngleTests(unittest.TestCase):
    def test_BasicVectorAngleCalcWorks(self):
        # "To be or not to be" and "Doubt truth to be a liar"
        wordFreq1 = {
                     "be": 2, 
                     "to": 2,
                     "not": 1,
                     "or": 1
                     }
        wordFreq2 = {
                     "a": 1,
                     "be": 1,
                     "doubt": 1,
                     "liar": 1,
                     "to": 1,
                     "truth": 1
                     }
        sut = angleMetricCalculator.AngleMetricCalculator()

        result = sut.calc_vector_angle(wordFreq1, wordFreq2)

        self.assertEqual(1.028, round(result, 3))
        

if __name__ == '__main__':
    unittest.main()
