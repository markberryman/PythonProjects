import maxHeap
import unittest


class HeapSortTests(unittest.TestCase):
    # input heaps obey max-heap property
    def test_OneItemHeap(self):
        data = [1]
        expected = [1]
        sut = maxHeap.MaxHeap(data)

        actual = sut.heap_sort()
    
        self.assertEqual(expected, actual)

    def test_TwoItemHeap(self):
        data = [2,1]
        expected = [1,2]
        sut = maxHeap.MaxHeap(data)

        actual = sut.heap_sort()
    
        self.assertEqual(expected, actual)

    def test_EightItemHeap(self):
        data = [8, 6, 7, 4, 5, 3, 2, 1]
        expected = [1,2,3,4,5,6,7,8]
        sut = maxHeap.MaxHeap(data)

        actual = sut.heap_sort()
    
        self.assertEqual(expected, actual)


class AddDataTests(unittest.TestCase):
    def test_addFirstItem(self):
        item = 1
        expected = [1]
        sut = maxHeap.MaxHeap()

        sut.add_data(item)

        self.assertEqual(expected, sut.data)

    def test_addTwoOrderedItems(self):
        item1 = 1
        item2 = 2
        expected = [2,1]
        sut = maxHeap.MaxHeap()

        sut.add_data(item2)
        sut.add_data(item1)

        self.assertEqual(expected, sut.data)

    def test_addTwoUnOrderedItems(self):
        item1 = 1
        item2 = 2
        expected = [2,1]
        sut = maxHeap.MaxHeap()

        sut.add_data(item1)
        sut.add_data(item2)

        self.assertEqual(expected, sut.data)

    def test_addEightUnOrderedItems(self):
        item1 = 6
        item2 = 5
        item3 = 3
        item4 = 1
        item5 = 8
        item6 = 7
        item7 = 2
        item8 = 4
        expected = [8, 6, 7, 4, 5, 3, 2, 1]
        sut = maxHeap.MaxHeap()

        sut.add_data(item1)
        sut.add_data(item2)
        sut.add_data(item3)
        sut.add_data(item4)
        sut.add_data(item5)
        sut.add_data(item6)
        sut.add_data(item7)
        sut.add_data(item8)

        self.assertEqual(expected, sut.data)


class GetParentIdxTests(unittest.TestCase):
    def test_GetParentOfIdx1(self):
        expected = 0    # indicating root
        
        actual = maxHeap.MaxHeap.get_parentIdx(1)

        self.assertEqual(expected, actual)

    def test_GetParentOfIdx2(self):
        expected = 1    # indicating root
        
        actual = maxHeap.MaxHeap.get_parentIdx(2)

        self.assertEqual(expected, actual)


class GetChildIdxTests(unittest.TestCase):
    def test_GetLeftChildOf3ElementHeap(self):
        data = [3,2,1]
        expected = 2
        sut = maxHeap.MaxHeap(data)

        actual = maxHeap.MaxHeap.get_childIdx(1, 0)

        self.assertEqual(expected, actual)

    def test_GetRightChildOf3ElementHeap(self):
        data = [3,2,1]
        expected = 3
        sut = maxHeap.MaxHeap(data)

        actual = maxHeap.MaxHeap.get_childIdx(1, 1)

        self.assertEqual(expected, actual)


class MaxHeapifyTests(unittest.TestCase):
    def test_3ElementHeap(self):
        data = [1,2,3]
        expected = [3,2,1]
        sut = maxHeap.MaxHeap(data)

        # remember, we're one based so we're pointing
        # at the root here
        sut.max_heapify(1)
        actual = sut.data

        self.assertEqual(expected, actual)

    def test_10ElementHeapMaxHeapify2(self):
        data = [16,4,10,14,7,9,3,2,8,1]
        expected = [16,14,10,8,7,9,3,2,4,1]
        sut = maxHeap.MaxHeap(data)

        # remember, we're one based so we're pointing
        # at the root here
        sut.max_heapify(2)
        actual = sut.data

        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
