import maxHeap
import unittest


class AddDataTests(unittest.TestCase):
    def test_addFirstItem(self):
        item = 1
        expected = [1]
        sut = maxHeap.maxHeap()

        sut.add_data(item)

        self.assertEqual(expected, sut.data)


class GetChildTests(unittest.TestCase):
    def test_GetLeftChildOf3ElementHeap(self):
        data = [3,2,1]
        expected = 2
        sut = maxHeap.maxHeap(data)

        actual = sut.get_child(1, 0)

        self.assertEqual(expected, actual)

    def test_GetRightChildOf3ElementHeap(self):
        data = [3,2,1]
        expected = 3
        sut = maxHeap.maxHeap(data)

        actual = sut.get_child(1, 1)

        self.assertEqual(expected, actual)


class MaxHeapifyTests(unittest.TestCase):
    def test_3ElementHeap(self):
        data = [1,2,3]
        expected = [3,2,1]
        sut = maxHeap.maxHeap(data)

        # remember, we're one based so we're pointing
        # at the root here
        sut.max_heapify(1)
        actual = sut.data

        self.assertEqual(expected, actual)

    def test_10ElementHeapMaxHeapify2(self):
        data = [16,4,10,14,7,9,3,2,8,1]
        expected = [16,14,10,8,7,9,3,2,4,1]
        sut = maxHeap.maxHeap(data)

        # remember, we're one based so we're pointing
        # at the root here
        sut.max_heapify(2)
        actual = sut.data

        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
