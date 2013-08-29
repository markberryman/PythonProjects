from html.parser import HTMLParser
import linkChecker
import linkRequester
import pageGetter
import unittest

class MockHtmlLinkParser(object):
    def __init__(self):
        self.feedMethodCalledCorrectly = False
        self.links = set()

    def feed(self, markup):
        if (markup == "some markup"):
            self.feedMethodCalledCorrectly = True

class MockHtmlLinkParser(HTMLParser):
    def __init__(self):
        super().__init__(self)
        self.links = set()

    # tag and attribute values are automatically lowercased
    def handle_starttag(self, tag, attrs):
        # todo - what type of tags do we want to look for?
        if (tag == "a"):
            for attr in attrs:
                # todo - use list comprehension to make this cleaner
                attrName, attrValue = attr

                if (attrName == "href"):
                    # todo - should do the link union here for optimization
                    self.links.add(attrValue)

class MockLinkRequester(object):
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

if __name__ == '__main__':
    unittest.main()