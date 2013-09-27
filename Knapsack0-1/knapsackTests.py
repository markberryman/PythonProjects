import knapsack
import unittest


class CalculateValuesTests(unittest.TestCase):
    def test_KnapsackWithCapacityZero(self):
        sut = knapsack.Knapsack(0)

        actual = sut.calculate_values([])

        self.assertIsNone(actual)

    def test_NoItems(self):
        sut = knapsack.Knapsack(1)

        actual = sut.calculate_values(None)

        self.assertIsNone(actual)

    def test_ComputedValuesArrayCorrectSize(self):
        item1 = knapsack.Item(0, 1, 1)
        item2 = knapsack.Item(1, 2, 2)
        sut = knapsack.Knapsack(3)

        actual = sut.calculate_values([item1, item2])

        # num rows check
        self.assertEqual(2, len(actual))
        # num cols check
        self.assertEqual(3, len(actual[0]))



if __name__ == '__main__':
    unittest.main()
