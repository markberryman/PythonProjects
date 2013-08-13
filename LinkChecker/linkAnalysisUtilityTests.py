import linkAnalysisUtility
import unittest

class LinkAnalysisUtilityTests(unittest.TestCase):
    @staticmethod
    def suite():
        tests = [
            'IsLinkRelativeReturnsTrueWhenLinkIsRelative',
            'IsLinkRelativeReturnsFalseWhenLinkIsNotRelative'
            ]

        return unittest.TestSuite(map(LinkAnalysisUtilityTests, tests))

    def IsLinkRelativeReturnsTrueWhenLinkIsRelative(self):
        link = "/foo.html"
        
        result = linkAnalysisUtility.LinkAnalysisUtility.is_link_relative(link)

        self.assertTrue(result);

    def IsLinkRelativeReturnsFalseWhenLinkIsNotRelative(self):
        link = "http://www.foo.com"
        
        result = linkAnalysisUtility.LinkAnalysisUtility.is_link_relative(link)

        self.assertFalse(result);
