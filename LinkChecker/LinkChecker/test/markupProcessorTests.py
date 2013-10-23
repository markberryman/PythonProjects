import markupProcessor
import unittest


class MockHtmlLinkParser(object):
    def __init__(self):
        self.links = set()

    def process_markup(self, markup):
        return self.links


class MarkupProcessor_GetLinksFromMarkupTests(unittest.TestCase):
    def test_returnsEmptySetIfMarkupProvidedIsNone(self):
        sut = markupProcessor.MarkupProcessor(None)

        result = sut.get_links_from_markup(None)

        self.assertEqual(0, len(result))

    def test_returnsLinksFromHtmlLinkParser(self):
        mockHtmlLinkParser = MockHtmlLinkParser()
        sut = markupProcessor.MarkupProcessor(mockHtmlLinkParser)

        result = sut.get_links_from_markup("some markup")

        self.assertEqual(result, mockHtmlLinkParser.links)


if __name__ == '__main__':
    unittest.main()
