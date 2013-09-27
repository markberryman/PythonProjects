import knapsack
import unittest


class CalculateValuesTests(unittest.TestCase):
    def test_KnapsackWithCapacityZero(self):
        sut = knapsack.Knapsack(0)

        actual = sut.calculate_values(None)

        self.assertIsNone(actual)


if __name__ == '__main__':
    unittest.main()
