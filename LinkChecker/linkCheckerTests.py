import linkChecker
import unittest

class MockPageGetter(object):
    def get_page(self, link):
        statusCode = 1  # indicates link is broken
        return statusCode, None


class GetLinkTests(unittest.TestCase):
    def test_ReturnsBrokenLinkWhenLinkBroken(self):
        sut = linkChecker.LinkChecker("start link", 1, MockPageGetter(), None)
        
        isLinkBroken, markup = sut.get_link("some link")

        self.assertTrue(isLinkBroken)
        

    #def test_ReturnsNotBrokenLinkWhenLinkNotBroken(self):
    #    self.assertTrue(False)

    #def test_ReturnsMarkupWhenLinkIsNotBroken(self):
    #    self.assertTrue(False)

#class MockHtmlLinkParser(object):


#class ProcessLinkTests(unittest.TestCase):
#    def test_ReturnsBrokenLinkWhenLinkBroken(self):
#        sut = linkChecker.LinkChecker("start link", 1, MockPageGetter(), 
#        self.assertTrue(False)

#    def test_ReturnsNotBrokenLinkWhenLinkNotBroken(self):
#        self.assertTrue(False)

#    def test_ReturnsNewLinks(self):
#        self.assertTrue(False)

if __name__ == '__main__':
    unittest.main()