import linkAnalysisUtility
import unittest

class LinkAnalysisUtilityTests:
    def suite():
        suite = unittest.TestSuite()

        suite.addTest(IsLinkRelativeReturnsTrueWhenLinkIsRelative())

        return suite

class IsLinkRelativeReturnsTrueWhenLinkIsRelative(unittest.TestCase):
    def runTest(self):
        link = "/foo.html"
        
        result = linkAnalysisUtility.LinkAnalysisUtility.is_link_relative(link)

        self.assertTrue(result);
