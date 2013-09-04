import html.parser
from html.parser import HTMLParser
import link
import linkChecker
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

    def get_resource(self, link):
        return 404, self.dummyMarkupToReturn

class MockLinkFilter(object):
    def filter_links(self, links):
        return links

# these are more functional tests rather than unit tests
class CheckLinksTests(unittest.TestCase):
    def test_CheckLinksFunctionalTest(self):
        mockHtmlLinkParserFactory = MockHtmlLinkParserFactory()
        mockLinkRequester = MockLinkRequester()
        dummyLink = link.Link("some link", link.LinkType.ANCHOR)
        sut = linkChecker.LinkChecker(mockHtmlLinkParserFactory, mockLinkRequester, None)

        sut.check_links(set([dummyLink]), 1)

        self.assertEqual(1, sut.numLinksProcessed)

    def test_CheckLinksAddsBrokenLink(self):
        mockHtmlLinkParserFactory = MockHtmlLinkParserFactory()
        mockLinkRequester = MockLinkRequester(None)
        dummyLink = link.Link("broken link", link.LinkType.ANCHOR)
        sut = linkChecker.LinkChecker(mockHtmlLinkParserFactory, mockLinkRequester, None)

        sut.check_links(set([dummyLink]), 1)

        self.assertEqual(1, len(sut.brokenLinks))

    def test_CheckLinksTracksPagesWithInvalidMarkup(self):
        mockHtmlLinkParserFactory = MockHtmlLinkParserFactory()
        mockLinkRequester = MockLinkRequester()
        mockLinkFilter = MockLinkFilter()
        dummyLink = link.Link("link with invalid markup", link.LinkType.ANCHOR)
        sut = linkChecker.LinkChecker(mockHtmlLinkParserFactory, mockLinkRequester, mockLinkFilter)

        sut.check_links(set([dummyLink]), 1)

        self.assertEqual(1, len(sut.invalidMarkupLinks))

if __name__ == '__main__':
    unittest.main()