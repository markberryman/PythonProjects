import pLinkRequester
import unittest


class MockQueue(object):
    def __init__(self):
        self.data = []

    def put(self, item):
        self.data.append(item)

    def get(self):
        return None


class AddWorkTests(unittest.TestCase):
    def test_AddWorkAddsItemToInputQueue(self):
        dummyQueue = MockQueue()
        dummyItem = "x"
        sut = pLinkRequester.PLinkRequester(1, None, dummyQueue, None)

        sut.add_work(dummyItem)

        self.assertEqual(dummyItem, dummyQueue.data[0])

    def test_IncrementsNumOfActiveWorkItems(self):
        dummyQueue = MockQueue()
        sut = pLinkRequester.PLinkRequester(1, None, dummyQueue, None)

        sut.add_work(None)

        self.assertEqual(1, sut.numActiveWorkItems)


class GetResultTests(unittest.TestCase):
    def test_GetResultReturnsOutputQueueItem(self):
        dummyQueue = MockQueue()
        sut = pLinkRequester.PLinkRequester(1, None, None, dummyQueue)

        result = sut.get_result()

        self.assertEqual(None, result)

    def test_DecrementsNumOfActiveWorkItems(self):
        dummyQueue = MockQueue()
        sut = pLinkRequester.PLinkRequester(1, None, None, dummyQueue)

        sut.get_result()

        self.assertEqual(-1, sut.numActiveWorkItems)

if __name__ == '__main__':
    unittest.main()
