import pLinkRequester
import unittest


class MockQueue(object):
    def get(self):
        return None


class GetResultTests(unittest.TestCase):
    def test_GetResultReturnsOutputQueueItem(self):
        dummyQueue = MockQueue()
        sut = pLinkRequester.PLinkRequester(1, None, dummyQueue)

        result = sut.get_result()

        self.assertEqual(None, result)

if __name__ == '__main__':
    unittest.main()
