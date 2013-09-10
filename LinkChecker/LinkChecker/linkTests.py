import link
import unittest


class IsLinkBrokenTests(unittest.TestCase):
    def test_ReturnsTrueIfStatusCodeLessThanOK(self):
        sut = link.Link("some link")
        sut.resultStatusCode = 199

        result = sut.is_link_broken()

        self.assertTrue(result)

    def test_ReturnsTrueIfStatusCodeGreaterThanOrEqualToBAD_REQUEST(self):
        sut = link.Link("some link")
        sut.resultStatusCode = 400

        result = sut.is_link_broken()

        self.assertTrue(result)

    def test_ReturnsFalseIfLinkIsNotBroken(self):
        sut = link.Link("some link")
        sut.resultStatusCode = 200

        result = sut.is_link_broken()

        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()
