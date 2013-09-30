import knapsack
import unittest


class FindItemsTests(unittest.TestCase):
    def test_Knapsack_MaxWeight5_4Items(self):
        item1 = knapsack.Item(1, 2, 3)
        item2 = knapsack.Item(2, 3, 4)
        item3 = knapsack.Item(3, 4, 5)
        item4 = knapsack.Item(4, 5, 6)
        items = [item1, item2, item3, item4]        
        ks = knapsack.Knapsack(5)
        values = [[0, 0, 0, 0, 0, 0], [0, 0, 3, 3, 3, 3], [0, 0, 3, 4, 4, 7], [0, 0, 3, 4, 5, 7], [0, 0, 3, 4, 5, 7]]

        actual = ks.find_items(items, values)

        self.assertEqual(item2.id, actual[0].id)
        self.assertEqual(item1.id, actual[1].id)


class CalculateValuesTests(unittest.TestCase):
    def test_KnapsackWithCapacityZero(self):
        sut = knapsack.Knapsack(0)

        actual = sut.calculate_values([])

        self.assertIsNone(actual)

    def test_NoItems(self):
        sut = knapsack.Knapsack(1)

        actual = sut.calculate_values(None)

        self.assertIsNone(actual)

    def test_ComputedValuesArrayCorrectSize_MaxWeight1_1Item(self):
        item1 = knapsack.Item(0, 1, 1)
        items = [item1]
        maxWeight = 1
        sut = knapsack.Knapsack(1)

        actual = sut.calculate_values(items)

        # rows
        self.assertEqual(len(items) + 1, len(actual))
        # cols
        self.assertEqual(maxWeight + 1, len(actual[0]))

    def test_ComputedValuesArrayCorrectSize_MaxWeight3_2Items(self):
        item1 = knapsack.Item(0, 1, 1)
        item2 = knapsack.Item(1, 2, 2)
        items = [item1, item2]
        maxWeight = 3
        sut = knapsack.Knapsack(maxWeight)

        actual = sut.calculate_values(items)

        # rows
        self.assertEqual(len(items) + 1, len(actual))
        # cols
        self.assertEqual(maxWeight + 1, len(actual[0]))

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
