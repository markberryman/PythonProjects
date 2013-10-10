import quickSort
import unittest


class partitionTests(unittest.TestCase):
    def test_OneElementOfData(self):
        data = [1]
        expected = [1]
        
        quickSort.QuickSort.partition(data, 0, 0, 0)

        self.assertEqual(expected, data)

    def test_TwoElementsOfData(self):
        data = [2,1]
        expected = [1,2]
        
        quickSort.QuickSort.partition(data, 0, 1, 0)

        self.assertEqual(expected, data)

    def test_ThreeElementsOfData(self):
        data = [3,2,1]
        expected = [1,2,3]
        
        quickSort.QuickSort.partition(data, 0, 3, 1)

        self.assertEqual(expected, data)


if __name__ == '__main__':
    unittest.main()
