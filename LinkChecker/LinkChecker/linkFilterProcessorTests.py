import link
import linkFilterProcessor
import unittest

class MockFilter(object):
    def __init__(self, filterFn):
        self.filterFn = filterFn

    def should_filter(self, link):
        return self.filterFn(link)

class ApplyFiltersTests(unittest.TestCase):
    def test_ReturnsLinksWhenNoFiltersLeftToApply(self):
        dummyFilters = []
        dummyLinks = set([link.Link("a link", link.LinkType.ANCHOR)])
        
        result = linkFilterProcessor.LinkFilterProcessor.apply_filters(dummyFilters, dummyLinks)

        self.assertEqual(1, len(result))

    def test_AppliesMultipleAllFilters(self):
        dummyFilterIsLowerCase = MockFilter(lambda x: x.islower())
        dummyFilterIsUpperCase = MockFilter(lambda x: x.isupper())
        dummyFilters = [dummyFilterIsLowerCase, dummyFilterIsUpperCase]
        dummyLinks = set([
                         link.Link("lowercase", link.LinkType.ANCHOR),
                         link.Link("uppercase", link.LinkType.ANCHOR),
                         link.Link("MIXEDcase", link.LinkType.ANCHOR)
                         ])
        
        result = linkFilterProcessor.LinkFilterProcessor.apply_filters(dummyFilters, dummyLinks)

        self.assertEqual(1, len(result))

if __name__ == '__main__':
    unittest.main()