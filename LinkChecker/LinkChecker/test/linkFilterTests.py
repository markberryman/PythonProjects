import linkFilter
import unittest


class MailToFilterTests(unittest.TestCase):
    def test_FiltersMailToLinks(self):
        sut = linkFilter.MailToFilter()

        filterResult = sut.should_filter("mailto:foo")

        self.assertTrue(filterResult)


class DomainCheckFilterTests(unittest.TestCase):
    def test_ReturnsTrueWhenDomainsDoNotMatch(self):
        sut = linkFilter.DomainCheckFilter("http://www.markwberryman.com")

        filterResult = sut.should_filter("http://www.foo.com")

        self.assertTrue(filterResult)

    def test_ReturnsFalseWhenDomainsMatch(self):
        sut = linkFilter.DomainCheckFilter("http://www.markwberryman.com")

        filterResult = sut.should_filter("http://www.markwberryman.com/index.html")

        self.assertFalse(filterResult)


if __name__ == '__main__':
    unittest.main()
