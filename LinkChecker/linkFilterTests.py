import linkFilter
import unittest

class FilterLinksTests(unittest.TestCase):
    def test_FiltersMailToLinks(self):
        dummyLinks = set(["mailto:foo"])
        sut = linkFilter.LinkFilter()

        filteredLinks = sut.filter_links(dummyLinks)

        self.assertEqual(0, len(filteredLinks))

if __name__ == '__main__':
    unittest.main()