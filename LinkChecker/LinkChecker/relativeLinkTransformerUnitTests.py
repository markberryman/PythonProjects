import linkTransformer
import unittest

class RelativeLinkTransformerUnitTests(unittest.TestCase):
    def test_TransformsRelativeLink(self):
        dummyCurrentLink = "http://www.foo.com"
        dummyNewLink = "relativelink.html"
        sut = linkTransformer.RelativeLinkTransformer()

        result = sut.transform(dummyCurrentLink, dummyNewLink)

        self.assertEqual(result, "http://www.foo.com/relativelink.html")
        
    def test_DoesNotTransformsAbsoluteLink(self):
        dummyCurrentLink = "http://www.foo.com"
        dummyNewLink = "http://www.bar.com"
        sut = linkTransformer.RelativeLinkTransformer()

        result = sut.transform(dummyCurrentLink, dummyNewLink)

        self.assertEqual(result, dummyNewLink)


if __name__ == '__main__':
    unittest.main()