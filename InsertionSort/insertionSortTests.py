import insertionSort
import unittest


class SortTests(unittest.TestCase):
    def test_OneElement(self):
        data = [0]
        expected = [0]
        
        insertionSort.InsertionSort.sort(data)

        self.assertEqual(expected, data)

    def test_TwoElement(self):
        data = [2,1]
        expected = [1,2]
        
        insertionSort.InsertionSort.sort(data)

        self.assertEqual(expected, data)

    def test_EightElement(self):
        data = [2,1,7,5,8,6,4,3]
        expected = [1,2,3,4,5,6,7,8]
        
        insertionSort.InsertionSort.sort(data)

        self.assertEqual(expected, data)

if __name__ == '__main__':
    unittest.main()
