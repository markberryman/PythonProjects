import linkRequester
import unittest

class MockPageGetter(object):
    def __init__(self, statusCodeToReturn):
        self.statusCodeToReturn = statusCodeToReturn;

    def get_page(self, link):
        return self.statusCodeToReturn, "some markup"

class GetLinkTests(unittest.TestCase):
    def test_ReturnsNoneWhenLinkResponseStatusCodeLessThanOK(self):
        sut = linkRequester.LinkRequester(MockPageGetter(199))
        
        result = sut.get_link("some link")

        self.assertTrue(result is None)
    
    def test_ReturnsNoneWhenLinkResponseStatusCodeGreaternThanOrEqualToBadRequest(self):
        sut = linkRequester.LinkRequester(MockPageGetter(400))
        
        result = sut.get_link("some link")

        self.assertTrue(result is None)  

    def test_ReturnsMarkupIfLinkNotBroken(self):
        sut = linkRequester.LinkRequester(MockPageGetter(200))
        
        result = sut.get_link("some link")

        self.assertEqual("some markup", result)

if __name__ == '__main__':
    unittest.main()