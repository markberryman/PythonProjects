import pageGetter
import unittest

class MockResponse(object):
    def __init__(self):
        self.status = 200

    def read(self):
        return b"hi"

class MockRequester(object):
    def request_url(self, url):
        return MockResponse()

class PageGetterTests(unittest.TestCase):
    def test_GetPageReturnsUrlContent(self):
        mockRequester = MockRequester()
        sut = pageGetter.PageGetter(mockRequester)
        
        result = sut.get_page("some url")

        self.assertEqual(result, "hi")

if __name__ == '__main__':
    unittest.main()