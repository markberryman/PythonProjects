import linkAnalysisUtility
import unittest

class LinkAnalysisUtilityTests(unittest.TestCase):
    @staticmethod
    def suite():
        # todo - how to merge multiple test suites?
        return IsLinkRelativeMethodTests.suite()

class IsLinkRelativeMethodTests(unittest.TestCase):
    @staticmethod
    def suite():
        tests = [
            'IsLinkRelativeReturnsTrueWhenLinkIsRelative',
            'IsLinkRelativeReturnsFalseWhenLinkIsNotRelative',
            'IsLinkRelativeReturnsFalseWhenLinkIsNotRelativeAndIgnoresCase'
            ]

        return unittest.TestSuite(map(IsLinkRelativeMethodTests, tests))

    def IsLinkRelativeReturnsTrueWhenLinkIsRelative(self):
        link = "/foo.html"
        
        result = linkAnalysisUtility.LinkAnalysisUtility.is_link_relative(link)

        self.assertTrue(result);

    def IsLinkRelativeReturnsFalseWhenLinkIsNotRelative(self):
        link = "http://www.foo.com"
        
        result = linkAnalysisUtility.LinkAnalysisUtility.is_link_relative(link)

        self.assertFalse(result);
        
    def IsLinkRelativeReturnsFalseWhenLinkIsNotRelativeAndIgnoresCase(self):
        link = "HTTP://www.foo.com"
        
        result = linkAnalysisUtility.LinkAnalysisUtility.is_link_relative(link)

        self.assertFalse(result);
