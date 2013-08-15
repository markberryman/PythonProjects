import linkChecker
import pageGetter
import unittest

class MockPageGetter(object):
    def __init__(self, statusCodeToReturn):
        self.statusCodeToReturn = statusCodeToReturn;

    def get_page(self, link):
        return self.statusCodeToReturn, "some markup"

class MockHtmlLinkParser(object):
    def __init__(self):
        self.feedMethodCalledCorrectly = False
        self.links = set()

    def feed(self, markup):
        if (markup == "some markup"):
            self.feedMethodCalledCorrectly = True

class GetLinkTests(unittest.TestCase):
    def test_ReturnsBrokenLinkWhenLinkResponseStatusCodeLessThanOK(self):
        sut = linkChecker.LinkChecker("start link", 1, pageGetter_ = MockPageGetter(199))
        
        isLinkBroken, markup = sut.get_link("some link")

        self.assertTrue(isLinkBroken)
    
    def test_ReturnsBrokenLinkWhenLinkResponseStatusCodeGreaternThanOrEqualToBadRequest(self):
        sut = linkChecker.LinkChecker("start link", 1, pageGetter_ = MockPageGetter(400))
        
        isLinkBroken, markup = sut.get_link("some link")

        self.assertTrue(isLinkBroken)    

    def test_ReturnsLinkNotBrokenAndMarkupIfLinkNotBroken(self):
        sut = linkChecker.LinkChecker("start link", 1, pageGetter_ = MockPageGetter(200))
        
        isLinkBroken, markup = sut.get_link("some link")

        self.assertFalse(isLinkBroken)
        self.assertEqual("some markup", markup)

class ProcessLinkTests(unittest.TestCase):
    def test_InvokesFeedMethodOnMarkup(self):
        mockHtmlLinkParser = MockHtmlLinkParser()
        sut = linkChecker.LinkChecker("start link", 1, htmlLinkParser_ = mockHtmlLinkParser)

        sut.process_link("some markup")

        self.assertTrue(mockHtmlLinkParser.feedMethodCalledCorrectly)

    def test_ReturnsLinks(self):
        mockHtmlLinkParser = MockHtmlLinkParser()
        mockHtmlLinkParser.links = set()
        sut = linkChecker.LinkChecker("start link", 1, htmlLinkParser_ = mockHtmlLinkParser)

        result = sut.process_link("some markup")

        self.assertTrue(result is mockHtmlLinkParser.links)

if __name__ == '__main__':
    unittest.main()