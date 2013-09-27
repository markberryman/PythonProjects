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

    def test_ComputedValuesArrayCorrectSize_Weight1_1Item(self):
        item1 = knapsack.Item(0, 1, 1)
        sut = knapsack.Knapsack(1)

        actual = sut.calculate_values([item1])

        self.assertEqual(2, len(actual))
        self.assertEqual(2, len(actual[0]))

    def test_ComputedValuesArrayCorrectSize_Weight3_2Items(self):
        item1 = knapsack.Item(0, 1, 1)
        item2 = knapsack.Item(1, 2, 2)
        sut = knapsack.Knapsack(3)

        actual = sut.calculate_values([item1, item2])

        self.assertEqual(2, len(actual))
        self.assertEqual(3, len(actual[0]))

    def test_MaxWeight1_NoItemCanFit(self):
        item1 = knapsack.Item(0, 2, 1)
        sut = knapsack.Knapsack(1)

        actual = sut.calculate_values([item1])

        for row in range(len(actual)):
            for col in range(len(actual[0])):
                self.failUnlessEqual(0, actual[row][col])

    def test_MaxWeight1_SingleItemWithWeight1(self):
        itemValue = 99
        item1 = knapsack.Item(0, 1, itemValue)
        sut = knapsack.Knapsack(1)

        actual = sut.calculate_values([item1])

        # [0, 0]
        # [0, 1]
        self.assertEqual(itemValue, actual[1][1])


if __name__ == '__main__':
    unittest.main()
