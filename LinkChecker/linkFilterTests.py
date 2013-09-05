import link
import linkFilter
import unittest

class MailToFilterTests(unittest.TestCase):
    def test_FiltersMailToLinks(self):
        dummyLink = link.Link("mailto:foo", link.LinkType.ANCHOR)
        sut = linkFilter.MailToFilter()

        filterResult = sut.filter(dummyLink)

        self.assertTrue(filterResult)

class DomainCheckFilterTests(unittest.TestCase):
    def test_ReturnsTrueWhenHostnameDoesNotMatchBaseHostname(self):
        dummyLink = link.Link("http://www.foo.com", link.LinkType.ANCHOR)
        sut = linkFilter.DomainCheckFilter(link.Link("http://www.markwberryman.com", link.LinkType.ANCHOR))

        filterResult = sut.filter(dummyLink)

        self.assertTrue(filterResult)

if __name__ == '__main__':
    unittest.main()