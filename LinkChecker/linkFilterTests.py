import link
import linkFilter
import unittest

class FilterLinksTests(unittest.TestCase):
    def test_FiltersMailToLinks(self):
        dummyLinks = set(link.Link("mailto:foo", link.LinkType.ANCHOR))
        sut = linkFilter.LinkFilter()

        filteredLinks = sut.filter_links(dummyLinks)

        self.assertEqual(0, len(filteredLinks))

if __name__ == '__main__':
    unittest.main()