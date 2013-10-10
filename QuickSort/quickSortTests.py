import quickSort
import unittest


class SortTests(unittest.TestCase):
    def test_OneElement(self):
        data = [1]
        expected = [1]
        
        quickSort.QuickSort.sort(data, 0, len(data) - 1)

        self.assertEqual(expected, data)

    def test_TwoElement(self):
        data = [2,1]
        expected = [1,2]
        
        quickSort.QuickSort.sort(data, 0, len(data) - 1)

        self.assertEqual(expected, data)

    def test_ThreeElement(self):
        data = [1,3,2]
        expected = [1,2,3]
        
        quickSort.QuickSort.sort(data, 0, len(data) - 1)

        self.assertEqual(expected, data)

    def test_EightElement(self):
        data = [6,5,3,1,8,7,2,4]
        expected = [1,2,3,4,5,6,7,8]
        
        quickSort.QuickSort.sort(data, 0, len(data) - 1)

        self.assertEqual(expected, data)


class PartitionTests(unittest.TestCase):
    def test_OneElementOfData(self):
        data = [1]
        expectedData = [1]
        expected = 0
        
        actual = quickSort.QuickSort.partition(data, 0, 0, 0)

        self.assertEqual(expected, actual)
        self.assertEqual(expectedData, data)        

    def test_TwoElementsOfData(self):
        data = [2,1]
        expectedData = [1,2]
        expected = 1
        
        actual = quickSort.QuickSort.partition(data, 0, 1, 0)

        self.assertEqual(expected, actual)
        self.assertEqual(expectedData, data)

    def test_ThreeElementsOfData(self):
        data = [1,3,2]
        expectedData = [1,2,3]
        expected = 2
        
        actual = quickSort.QuickSort.partition(data, 0, 2, 1)

        self.assertEqual(expected, actual)
        self.assertEqual(expectedData, data)


if __name__ == '__main__':
    unittest.main()
