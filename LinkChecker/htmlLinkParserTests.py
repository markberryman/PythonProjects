import htmlLinkParser
import unittest

class HandleStartTagTests(unittest.TestCase):
    def test_ReturnsZeroLinksWhenMarkupContainsNoLinks(self):
        dummyMarkup = "<html>no links here</html>"
        sut = htmlLinkParser.HTMLLinkParser()
        
        sut.feed(dummyMarkup)

        self.assertEqual(0, len(sut.links))

    def test_ReturnsLinkFromMarkupWithAnchorTag(self):
        dummyLink = "http://www.foo.com"
        dummyMarkup = "<html><a href=\"" + dummyLink + "\"></a></html>";
        sut = htmlLinkParser.HTMLLinkParser()
        
        sut.feed(dummyMarkup)

        self.assertEqual(1, len(sut.links))
        self.assertTrue(dummyLink in sut.links)

if __name__ == '__main__':
    unittest.main()