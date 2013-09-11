import link
import markupProcessor
import unittest


class MockHtmlLinkParser(object):
    def __init__(self):
        self.links = set()

    def feed(self, markup):
        return None


class MockHtmlLinkParserFactory(object):
    def __init__(self, htmlLinkParser):
        self.htmlLinkParser = htmlLinkParser

    def create_html_link_parser(self):
        return self.htmlLinkParser


class GetLinksFromMarkup(unittest.TestCase):
    def test_returnsNoneIfMarkupProvidedIsNone(self):
        sut = markupProcessor.MarkupProcessor(None)

        result = sut.get_links_from_markup(None)

        self.assertTrue(result is None)

    def test_returnsLinksFromHtmlLinkParser(self):
        mockHtmlLinkParser = MockHtmlLinkParser()
        mockHtmlLinkParserFactory = MockHtmlLinkParserFactory(
            mockHtmlLinkParser)
        sut = markupProcessor.MarkupProcessor(mockHtmlLinkParserFactory)

        result = sut.get_links_from_markup("some markup")

        self.assertEqual(result, mockHtmlLinkParser.links)

if __name__ == '__main__':
    unittest.main()
