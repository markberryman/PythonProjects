import link
import linkTransform
import unittest


class LowerCaseTransformUnitTests(unittest.TestCase):
    def test_OnlyLowerCasesUrlSchemeNetlocAndPath(self):
        dummyLink = link.Link("HTTP://WWW.FOO.COM/SOMEPATH/INDEX.HTML?A=FOO")
        expected = "http://www.foo.com/somepath/index.html?A=FOO"
        sut = linkTransform.LowerCaseTransform()

        sut.transform(None, dummyLink)

        self.assertEqual(expected, dummyLink.value)


class RelativeLinkTransformUnitTests(unittest.TestCase):
    # only need a single sanity unit test here since the transform
    # is pretty much just running urljoin
    def test_TransformsLinkWithNetlocAndOnlySlashForPath(self):
        dummyContext = {
            "currentLink": link.Link("http://www.foo.com/")
            }
        dummyNewLink = link.Link("relativelink.html")
        sut = linkTransform.RelativeLinkTransform()

        sut.transform(dummyContext, dummyNewLink)

        self.assertEqual(
            dummyNewLink.value, "http://www.foo.com/relativelink.html")


if __name__ == '__main__':
    unittest.main()