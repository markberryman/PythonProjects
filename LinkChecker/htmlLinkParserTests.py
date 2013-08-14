import htmlLinkParser
import unittest

class HandleStartTagTests(unittest.TestCase):
    def test_ReturnsZeroLinksWhenMarkupContainsNoLinks(self):
        dummyMarkup = "<html>no links here</html>"
        sut = htmlLinkParser.HTMLLinkParser()
        
        sut.feed(dummyMarkup)

        self.assertEqual(0, len(sut.links))

    def test_ReturnsLinkFromMarkupWithAnchorTag(self):
        dummyLink1 = "http://www.foo.com"
        dummyLink2 = "http://www.bar.com"
        dummyMarkup = "<html>" + "<a href=\"" + dummyLink1 + "\"></a>" + "<a href=\"" + dummyLink2 + "\"></a>" + "</html>";
        sut = htmlLinkParser.HTMLLinkParser()
        
        sut.feed(dummyMarkup)

        self.assertEqual(2, len(sut.links))
        self.assertTrue(dummyLink1 in sut.links)
        self.assertTrue(dummyLink2 in sut.links)

if __name__ == '__main__':
    unittest.main()