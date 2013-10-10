import insertionSort
import unittest


class FindInsertIndexTests(unittest.TestCase):
    def test_InsertAtFront(self):
        data = [1]
        item = 0
        expected = 0

        actual = insertionSort.InsertionSort.find_insert_index(data, item)

        self.assertEqual(expected, actual)

    def test_InsertAtEnd(self):
        data = [1]
        item = 2
        expected = 1

        actual = insertionSort.InsertionSort.find_insert_index(data, item)

        self.assertEqual(expected, actual)

    def test_InsertInMiddle(self):
        data = [1,3]
        item = 2
        expected = 1

        actual = insertionSort.InsertionSort.find_insert_index(data, item)

        self.assertEqual(expected, actual)


class InsertTests(unittest.TestCase):
    def test_InsertItemAtFront(self):
        data = [1]
        item = 0
        expected = [0,1]

        insertionSort.InsertionSort.insert(data, item)

        self.assertEqual(expected, data)

    def test_InsertItemAtEnd(self):
        data = [0]
        item = 1
        expected = [0,1]

        insertionSort.InsertionSort.insert(data, item)

        self.assertEqual(expected, data)

    def test_InsertItemInMiddle(self):
        data = [0,2]
        item = 1
        expected = [0,1,2]

        insertionSort.InsertionSort.insert(data, item)

        self.assertEqual(expected, data)

    def test_InsertItemOneAwayFromMiddle(self):
        data = [1,2,5,7,8]
        item = 6
        expected = [1,2,5,6,7,8]

        insertionSort.InsertionSort.insert(data, item)

        self.assertEqual(expected, data)


class SortTests(unittest.TestCase):
    def test_OneElement(self):
        data = [0]
        expected = [0]
        
        actual = insertionSort.InsertionSort.sort(data)

        self.assertEqual(expected, actual)

    def test_TwoElement(self):
        data = [2,1]
        expected = [1,2]
        
        actual = insertionSort.InsertionSort.sort(data)

        self.assertEqual(expected, actual)

    def test_EightElement(self):
        data = [2,1,7,5,8,6,4,3]
        expected = [1,2,3,4,5,6,7,8]
        
        actual = insertionSort.InsertionSort.sort(data)

        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()
