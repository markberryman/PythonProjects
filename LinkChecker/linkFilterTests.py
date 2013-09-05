import link
import linkFilter
import unittest

class MailToFilterTests(unittest.TestCase):
    def test_FiltersMailToLinks(self):
        sut = linkFilter.MailToFilter()

        filterResult = sut.shouldFilter("mailto:foo")

        self.assertTrue(filterResult)

class DomainCheckFilterTests(unittest.TestCase):
    def test_ReturnsTrueWhenHostnameDoesNotMatchBaseHostname(self):
        sut = linkFilter.DomainCheckFilter("http://www.markwberryman.com")

        filterResult = sut.shouldFilter("http://www.foo.com")

        self.assertTrue(filterResult)

if __name__ == '__main__':
    unittest.main()