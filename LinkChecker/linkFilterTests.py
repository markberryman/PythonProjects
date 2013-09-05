import link
import linkFilter
import unittest

class MailToFilterTests(unittest.TestCase):
    def test_FiltersMailToLinks(self):
        dummyLink = link.Link("mailto:foo", link.LinkType.ANCHOR)
        sut = linkFilter.MailToFilter()

        filterResult = sut.filter(dummyLink)

        self.assertTrue(filterResult)

if __name__ == '__main__':
    unittest.main()