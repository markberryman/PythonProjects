import link
import linkTransformer
import unittest

class RelativeLinkTransformerUnitTests(unittest.TestCase):
    def test_TransformsRelativeLink(self):
        dummyCurrentLink = link.Link("http://www.foo.com")
        dummyNewLink = link.Link("relativelink.html")
        sut = linkTransformer.RelativeLinkTransformer(dummyCurrentLink)

        result = sut.transform(dummyNewLink)

        self.assertEqual(result.value, "http://www.foo.com/relativelink.html")
        
    def test_DoesNotTransformsAbsoluteLink(self):
        dummyCurrentLink = link.Link("http://www.foo.com")
        dummyNewLink = link.Link("http://www.bar.com")
        sut = linkTransformer.RelativeLinkTransformer(dummyCurrentLink)

        result = sut.transform(dummyNewLink)

        self.assertEqual(result, dummyNewLink)


if __name__ == '__main__':
    unittest.main()