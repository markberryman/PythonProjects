from html.parser import HTMLParser
import linkChecker
import linkRequester
import pageGetter
import unittest

class MockHtmlLinkParser(HTMLParser):
    def __init__(self):
        super().__init__(self)
        self.links = set()

    # tag and attribute values are automatically lowercased
    def handle_starttag(self, tag, attrs):
        return None
        
class MockLinkRequester(object):
    def __init__(self, dummyMarkupToReturn):
        self.dummyMarkupToReturn = dummyMarkupToReturn

    def get_link(self, link):
        return "some markup"

# these are more functional tests rather than unit tests
class CheckLinksTests(unittest.TestCase):
    def test_CheckLinksFunctionalTest(self):
        mockHtmlLinkParser = MockHtmlLinkParser()
        mockLinkRequester = MockLinkRequester()
        sut = linkChecker.LinkChecker("bogus start link", 1, mockHtmlLinkParser, mockLinkRequester)

        sut.check_links()

        self.assertEqual(1, sut.numLinksProcessed)

    def test_CheckLinksAddsBrokenLink(self):
        mockHtmlLinkParser = MockHtmlLinkParser()
        mockLinkRequester = MockLinkRequester()
        sut = linkChecker.LinkChecker("a broken link", 1, mockHtmlLinkParser, mockLinkRequester)

        sut.check_links()

        self.assertEqual(1, sut.numLinksProcessed)

if __name__ == '__main__':
    unittest.main()