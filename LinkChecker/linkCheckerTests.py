import html.parser
from html.parser import HTMLParser
import linkChecker
import linkRequester
import resourceGetter
import unittest

class MockHtmlLinkParser(HTMLParser):
    def __init__(self):
        super().__init__(self)
        self.links = set()

    def feed(self, data):
        raise html.parser.HTMLParseError("error")

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

class MockLinkFilter(object):
    def filter_links(links):
        return links

# these are more functional tests rather than unit tests
class CheckLinksTests(unittest.TestCase):
    def test_CheckLinksFunctionalTest(self):
        mockHtmlLinkParserFactory = MockHtmlLinkParserFactory()
        mockLinkRequester = MockLinkRequester()
        mockLinkFilter = MockLinkFilter()
        sut = linkChecker.LinkChecker(mockHtmlLinkParserFactory, mockLinkRequester, mockLinkFilter)

        sut.check_links(set(["bogus start link"]), 1)

        self.assertEqual(1, sut.numLinksProcessed)

    def test_CheckLinksAddsBrokenLink(self):
        mockHtmlLinkParserFactory = MockHtmlLinkParserFactory()
        mockLinkRequester = MockLinkRequester(None)
        mockLinkFilter = MockLinkFilter()
        sut = linkChecker.LinkChecker(mockHtmlLinkParserFactory, mockLinkRequester, mockLinkFilter)

        sut.check_links(set(["broken link"]), 1)

        self.assertEqual(1, len(sut.brokenLinks))

    def test_CheckLinksTracksPagesWithInvalidMarkup(self):
        mockHtmlLinkParserFactory = MockHtmlLinkParserFactory()
        mockLinkRequester = MockLinkRequester()
        mockLinkFilter = MockLinkFilter()
        sut = linkChecker.LinkChecker(mockHtmlLinkParserFactory, mockLinkRequester, mockLinkFilter)

        sut.check_links(set(["link with invalid markup"]), 1)

        self.assertEqual(1, len(sut.invalidMarkupLinks))

if __name__ == '__main__':
    unittest.main()