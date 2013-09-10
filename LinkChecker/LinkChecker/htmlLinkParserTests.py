import htmlLinkParser
import link
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
        dummyLink = "http://www.foo.com"
        dummyMarkup = "<html> <a href=\"{}\"></a> </html>".format(dummyLink)
        sut = htmlLinkParser.HTMLLinkParser()

        sut.feed(dummyMarkup)

        self.assertEqual(1, len(sut.links))
        self.assertEqual(list(sut.links)[0].type, link.LinkType.ANCHOR)

    def test_DoesNotAddLinkForAnchorTagWithNoHref(self):
        dummyLink = "http://www.foo.com"
        dummyMarkup = "<html> <a></a> </html>"
        sut = htmlLinkParser.HTMLLinkParser()

        sut.feed(dummyMarkup)

        self.assertEqual(0, len(sut.links))

    def test_ReturnsStylesheetLink(self):
        dummyLink = "http://www.foo.com/style.css"
        dummyMarkup = "<link rel=\"stylesheet\" href=\"{}\" />".format(dummyLink)
        sut = htmlLinkParser.HTMLLinkParser()

        sut.feed(dummyMarkup)

        self.assertEqual(1, len(sut.links))
        self.assertEqual(list(sut.links)[0].type, link.LinkType.STYLESHEET)

    def test_ReturnsScriptLink(self):
        dummyLink = "http://www.foo.com/script.js"
        dummyMarkup = "<script src=\"{}\" />".format(dummyLink)
        sut = htmlLinkParser.HTMLLinkParser()

        sut.feed(dummyMarkup)

        self.assertEqual(1, len(sut.links))
        self.assertEqual(list(sut.links)[0].type, link.LinkType.SCRIPT)

    def test_ReturnsImageLink(self):
        dummyLink = "http://www.foo.com/bar.jpg"
        dummyMarkup = "<img src=\"{}\" />".format(dummyLink)
        sut = htmlLinkParser.HTMLLinkParser()

        sut.feed(dummyMarkup)

        self.assertEqual(1, len(sut.links))
        self.assertEqual(list(sut.links)[0].type, link.LinkType.IMAGE)

if __name__ == '__main__':
    unittest.main()
