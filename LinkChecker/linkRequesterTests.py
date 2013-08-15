import linkRequester

class GetLinkTests(unittest.TestCase):
    def test_ReturnsBrokenLinkWhenLinkResponseStatusCodeLessThanOK(self):
        sut = linkChecker.LinkChecker("start link", 1, pageGetter_ = MockPageGetter(199))
        
        isLinkBroken, markup = sut.get_link("some link")

        self.assertTrue(isLinkBroken)
    
    def test_ReturnsBrokenLinkWhenLinkResponseStatusCodeGreaternThanOrEqualToBadRequest(self):
        sut = linkChecker.LinkChecker("start link", 1, pageGetter_ = MockPageGetter(400))
        
        isLinkBroken, markup = sut.get_link("some link")

        self.assertTrue(isLinkBroken)    

    def test_ReturnsLinkNotBrokenAndMarkupIfLinkNotBroken(self):
        sut = linkChecker.LinkChecker("start link", 1, pageGetter_ = MockPageGetter(200))
        
        isLinkBroken, markup = sut.get_link("some link")

        self.assertFalse(isLinkBroken)
        self.assertEqual("some markup", markup)

