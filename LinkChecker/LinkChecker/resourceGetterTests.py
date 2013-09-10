import link
import resourceGetter
import unittest


class MockResponse(object):
    def __init__(self):
        self.status = 200

    def read(self):
        return b"hi"


class MockRequester(object):
    def request_url(self, url):
        return MockResponse()


class ResourceGetterTests(unittest.TestCase):
    def test_GetResourceReturnsStatusCodeAndUrlContentForAnchorTag(self):
        mockRequester = MockRequester()
        dummyLink = link.Link("url", link.LinkType.ANCHOR)
        sut = resourceGetter.ResourceGetter(mockRequester)

        statusCodeResult, contentResult = sut.get_resource(dummyLink)

        self.assertEqual(200, statusCodeResult)
        self.assertEqual("hi", contentResult)

    def test_GetResourceReturnsNoneForMarkupForNonAnchorLink(self):
        mockRequester = MockRequester()
        dummyLink = link.Link("url", link.LinkType.IMAGE)
        sut = resourceGetter.ResourceGetter(mockRequester)

        statusCodeResult, contentResult = sut.get_resource(dummyLink)

        self.assertEqual(200, statusCodeResult)
        self.assertEqual(None, contentResult)

if __name__ == '__main__':
    unittest.main()
