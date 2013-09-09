import link
import markupProcessor
import unittest

class MockFilter(object):
    def __init__(self, filterFn):
        self.filterFn = filterFn

    def should_filter(self, link):
        return self.filterFn(link)

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

class ApplyFiltersUnitTests(unittest.TestCase):
    def test_ReturnsLinksWhenNoFiltersLeftToApply(self):
        dummyFilters = []
        dummyLinks = set([link.Link("a link")])
        sut = markupProcessor.MarkupProcessor(dummyFilters, None)
        
        result = sut.apply_filters(dummyLinks)

        self.assertEqual(1, len(result))

    def test_AppliesMultipleAllFilters(self):
        dummyFilterIsLowerCase = MockFilter(lambda x: x.islower())
        dummyFilterIsUpperCase = MockFilter(lambda x: x.isupper())
        dummyFilters = [dummyFilterIsLowerCase, dummyFilterIsUpperCase]
        dummyLinks = set([
                         link.Link("lowercase"),
                         link.Link("uppercase"),
                         link.Link("MIXEDcase")
                         ])
        sut = markupProcessor.MarkupProcessor(dummyFilters, None)

        result = sut.apply_filters(dummyLinks)

        self.assertEqual(1, len(result))

class GetLinksFromMarkup(unittest.TestCase):
    def test_returnsNoneIfMarkupProvidedIsNone(self):
        sut = markupProcessor.MarkupProcessor(None, None)

        result = sut.get_links_from_markup(None)

        self.assertTrue(result is None)

    def test_returnsLinksFromHtmlLinkParser(self):
        mockHtmlLinkParser = MockHtmlLinkParser()
        mockHtmlLinkParserFactory = MockHtmlLinkParserFactory(mockHtmlLinkParser)
        sut = markupProcessor.MarkupProcessor(None, mockHtmlLinkParserFactory)

        result = sut.get_links_from_markup("some markup")

        self.assertEqual(result, mockHtmlLinkParser.links)

if __name__ == '__main__':
    unittest.main()