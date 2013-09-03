import htmlLinkParser
import unittest

class HandleStartTagTests(unittest.TestCase):
    def test_ReturnsZeroLinksWhenMarkupContainsNoLinks(self):
        dummyMarkup = "<html>no links here</html>"
        sut = htmlLinkParser.HTMLLinkParser()
        
        sut.feed(dummyMarkup)

        self.assertEqual(0, len(sut.links))

    def test_DoesNotAddLinkFromTagWithNoLink(self):
        dummyMarkup = "<html> <a ></a> </html>"
        sut = htmlLinkParser.HTMLLinkParser()
        
        sut.feed(dummyMarkup)

        self.assertEqual(0, len(sut.links))

    def test_ReturnsLinkFromMarkupWithAnchorTag(self):
        dummyLink1 = "http://www.foo.com"
        dummyLink2 = "http://www.bar.com"
        dummyMarkup = "<html> <a href=\"{}\"></a> <a href=\"{}\"></a> </html>".format(dummyLink1, dummyLink2)
        sut = htmlLinkParser.HTMLLinkParser()
        
        sut.feed(dummyMarkup)

        self.assertEqual(2, len(sut.links))
        self.assertTrue(dummyLink1 in sut.links)
        self.assertTrue(dummyLink2 in sut.links)

    def test_ReturnsStylesheetLink(self):
        dummyLink = "http://www.foo.com/style.css"
        dummyMarkup = "<link rel=\"stylesheet\" href=\"{}\" />".format(dummyLink)
        sut = htmlLinkParser.HTMLLinkParser()
        
        sut.feed(dummyMarkup)

        self.assertEqual(1, len(sut.links))
        self.assertTrue(dummyLink in sut.links)

    def test_ReturnsScriptLink(self):
        dummyLink = "http://www.foo.com/script.js"
        dummyMarkup = "<script src=\"{}\" />".format(dummyLink)
        sut = htmlLinkParser.HTMLLinkParser()
        
        sut.feed(dummyMarkup)

        self.assertEqual(1, len(sut.links))
        self.assertTrue(dummyLink in sut.links)

if __name__ == '__main__':
    unittest.main()