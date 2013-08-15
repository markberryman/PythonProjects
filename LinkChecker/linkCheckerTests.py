import linkChecker
import unittest

class MockPageGetter(object):
    def __init__(self, statusCodeToReturn):
        self.statusCodeToReturn = statusCodeToReturn;

    def get_page(self, link):
        return self.statusCodeToReturn, None


class GetLinkTests(unittest.TestCase):
    def test_ReturnsBrokenLinkWhenLinkResponseStatusCodeLessThanOK(self):
        sut = linkChecker.LinkChecker("start link", 1, MockPageGetter(199), None)
        
        isLinkBroken, markup = sut.get_link("some link")

        self.assertTrue(isLinkBroken)
    
    def test_ReturnsBrokenLinkWhenLinkResponseStatusCodeGreaternThanOrEqualToBadRequest(self):
        sut = linkChecker.LinkChecker("start link", 1, MockPageGetter(400), None)
        
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