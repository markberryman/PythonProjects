import linkAnalysisUtility
import unittest

class LinkAnalysisUtilityTests:
    @staticmethod
    def suite():
        suite = unittest.TestSuite()
        
        suite.addTest(IsLinkRelativeReturnsTrueWhenLinkIsRelative())
        suite.addTest(IsLinkRelativeReturnsFalseWhenLinkIsNotRelative())

        return suite

class IsLinkRelativeReturnsTrueWhenLinkIsRelative(unittest.TestCase):
    def runTest(self):
        link = "/foo.html"
        
        result = linkAnalysisUtility.LinkAnalysisUtility.is_link_relative(link)

        self.assertTrue(result);

class IsLinkRelativeReturnsFalseWhenLinkIsNotRelative(unittest.TestCase):
    def runTest(self):
        link = "http://www.foo.com"
        
        result = linkAnalysisUtility.LinkAnalysisUtility.is_link_relative(link)

        self.assertFalse(result);
