import linkAnalysisUtility
import unittest


class IsLinkRelativeTests(unittest.TestCase):
    def test_ReturnsTrueWhenLinkIsRelative(self):
        link = "/foo.html"

        result = linkAnalysisUtility.LinkAnalysisUtility.is_link_relative(link)

        self.assertTrue(result);

    def test_ReturnsFalseWhenLinkIsNotRelative(self):
        link = "http://www.foo.com"

        result = linkAnalysisUtility.LinkAnalysisUtility.is_link_relative(link)

        self.assertFalse(result);

    def test_ReturnsFalseWhenLinkIsNotRelativeAndIgnoresCase(self):
        link = "HTTP://www.foo.com"
        
        result = linkAnalysisUtility.LinkAnalysisUtility.is_link_relative(link)

        self.assertFalse(result);

if __name__ == '__main__':
    unittest.main()
