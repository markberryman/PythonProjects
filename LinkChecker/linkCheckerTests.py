import linkChecker
import linkRequester
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

#class ProcessMarkupTests(unittest.TestCase):
#    def test_InvokesFeedMethodOnMarkup(self):
#        mockHtmlLinkParser = MockHtmlLinkParser()
#        sut = linkChecker.LinkChecker("start link", 1, mockHtmlLinkParser, None)

#        sut.process_markup("some markup")

#        self.assertTrue(mockHtmlLinkParser.feedMethodCalledCorrectly)

#    def test_ReturnsLinks(self):
#        mockHtmlLinkParser = MockHtmlLinkParser()
#        mockHtmlLinkParser.links = set()
#        sut = linkChecker.LinkChecker("start link", 1, mockHtmlLinkParser, None)

#        result = sut.process_markup("some markup")

#        self.assertTrue(result is mockHtmlLinkParser.links)

class MockLinkRequester(object):
    def get_link(self, link):
        return False, "markup"

class CheckLinksHelperTests(unittest.TestCase):
    def test_ProcessesNoLinksIfCurrentLinkDepthExceedsMaxDepth(self):
        sut = linkChecker.LinkChecker("start link", 1, None, None)

        sut.check_links_helper(set(), 2)

        self.assertEqual(0, sut.numLinksProcessed)

    #def test_RecordsNumberOfLinksProcessed(self):
    #    mockLinkRequester = MockLinkRequester()
    #    linksToProcess = set()
    #    linksToProcess.add("http://www.foo.com")

    #    sut = linkChecker.LinkChecker("start link", 1, None, mockLinkRequester)
        
    #    sut.check_links_helper(linksToProcess, 1)

    #    self.assertEqual(1, sut.numLinksProcessed)


if __name__ == '__main__':
    unittest.main()