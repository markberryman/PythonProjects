from html.parser import HTMLParser
import linkChecker
import linkRequester
import pageGetter
import unittest

class MockHtmlLinkParser(HTMLParser):
    def __init__(self):
        super().__init__(self)
        self.links = set()

    def handle_starttag(self, tag, attrs):
        return None

class MockHtmlLinkParserFactory(object):
    def create_html_link_parser(self):
        return MockHtmlLinkParser()
    
class MockLinkRequester(object):
    def __init__(self, dummyMarkupToReturn = "dummy markup"):
        self.dummyMarkupToReturn = dummyMarkupToReturn

    def get_link(self, link):
        return self.dummyMarkupToReturn

# these are more functional tests rather than unit tests
class CheckLinksTests(unittest.TestCase):
    def test_CheckLinksFunctionalTest(self):
        mockHtmlLinkParserFactory = MockHtmlLinkParserFactory()
        mockLinkRequester = MockLinkRequester()
        sut = linkChecker.LinkChecker(mockHtmlLinkParserFactory, mockLinkRequester)
        linksToProcess = set()
        linksToProcess.add("bogus start link")

        sut.check_links(linksToProcess, 1)

        self.assertEqual(1, sut.numLinksProcessed)

    def test_CheckLinksAddsBrokenLink(self):
        mockHtmlLinkParserFactory = MockHtmlLinkParserFactory()
        mockLinkRequester = MockLinkRequester(None)
        sut = linkChecker.LinkChecker(mockHtmlLinkParserFactory, mockLinkRequester)
        linksToProcess = set()
        linksToProcess.add("a broken link")

        sut.check_links(linksToProcess, 1)

        self.assertEqual(1, len(sut.brokenLinks))

if __name__ == '__main__':
    unittest.main()