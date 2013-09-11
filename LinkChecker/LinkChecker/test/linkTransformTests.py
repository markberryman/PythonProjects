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
    def test_DoesNotTransformsAbsoluteLink(self):
        dummyContext = {
            "currentLink": link.Link("some link")
            }
        dummyNewLink = link.Link("http://www.foo.com")
        sut = linkTransform.RelativeLinkTransform()

        sut.transform(dummyContext, dummyNewLink)

        self.assertEqual(dummyNewLink.value, "http://www.foo.com")

    def test_DoesNotTransformsMailToLink(self):
        dummyContext = {
            "currentLink": link.Link("http://www.foo.com")
            }
        dummyNewLink = link.Link("mailto:...")
        sut = linkTransform.RelativeLinkTransform()

        sut.transform(dummyContext, dummyNewLink)

        self.assertEqual(dummyNewLink.value, "mailto:...")

    def test_TransformsLinkWithNetlocAndNoPath(self):
        # >>> urlparse("http://www.foo.com")
        # ParseResult(scheme='http', netloc='www.foo.com', path='')
        dummyContext = {
            "currentLink": link.Link("http://www.foo.com")
            }
        dummyNewLink = link.Link("relativelink.html")
        sut = linkTransform.RelativeLinkTransform()

        sut.transform(dummyContext, dummyNewLink)

        self.assertEqual(
            dummyNewLink.value, "http://www.foo.com/relativelink.html")

    def test_TransformsLinkWithNoNetloc(self):
        # >>> urlparse("www.foo.com")
        # ParseResult(scheme='', netloc='', path='www.foo.com')
        dummyContext = {
            "currentLink": link.Link("www.foo.com")
            }
        dummyNewLink = link.Link("relativelink.html")
        sut = linkTransform.RelativeLinkTransform()

        sut.transform(dummyContext, dummyNewLink)

        self.assertEqual(
            dummyNewLink.value, "www.foo.com/relativelink.html")

    def test_TransformsLinkWithNetlocAndOnlySlashForPath(self):
        # >>> urlparse("http://www.foo.com/")
        # ParseResult(scheme='http', netloc='www.foo.com', path='/')
        dummyContext = {
            "currentLink": link.Link("http://www.foo.com/")
            }
        dummyNewLink = link.Link("relativelink.html")
        sut = linkTransform.RelativeLinkTransform()

        sut.transform(dummyContext, dummyNewLink)

        self.assertEqual(
            dummyNewLink.value, "http://www.foo.com/relativelink.html")

    def test_TransformsLinkWithNoNetlocAndPathEndingWithSlash(self):
        # >>> urlparse("www.foo.com/")
        # ParseResult(scheme='', netloc='', path='www.foo.com/')
        dummyContext = {
            "currentLink": link.Link("www.foo.com/")
            }
        dummyNewLink = link.Link("relativelink.html")
        sut = linkTransform.RelativeLinkTransform()

        sut.transform(dummyContext, dummyNewLink)

        self.assertEqual(
            dummyNewLink.value, "www.foo.com/relativelink.html")

    def test_TransformsLinkWithNetlocAndPathEndingWithNoExtension(self):
        # >>> urlparse("http://www.foo.com/x")
        # ParseResult(scheme='http', netloc='www.foo.com', path='/x')
        dummyContext = {
            "currentLink": link.Link("http://www.foo.com/x")
            }
        dummyNewLink = link.Link("relativelink.html")
        sut = linkTransform.RelativeLinkTransform()

        sut.transform(dummyContext, dummyNewLink)

        self.assertEqual(
            dummyNewLink.value, "http://www.foo.com/relativelink.html")

    def test_TransformsLinkWithNetlocAndPathEndingWithFileExtension(self):
        # >>> urlparse("http://www.foo.com/x.html")
        # ParseResult(scheme='http', netloc='www.foo.com', path='/x.html')
        dummyContext = {
            "currentLink": link.Link("http://www.foo.com/x.html")
            }
        dummyNewLink = link.Link("relativelink.html")
        sut = linkTransform.RelativeLinkTransform()

        sut.transform(dummyContext, dummyNewLink)

        self.assertEqual(
            dummyNewLink.value, "http://www.foo.com/relativelink.html")

    def test_TransformsLinkWithNetlocAndPathWithDirAndFileExtension(self):
        # >>> urlparse("http://www.foo.com/x/y.html")
        # ParseResult(scheme='http', netloc='www.foo.com', path='/x/y.html')
        dummyContext = {
            "currentLink": link.Link("http://www.foo.com/x/y.html")
            }
        dummyNewLink = link.Link("relativelink.html")
        sut = linkTransform.RelativeLinkTransform()

        sut.transform(dummyContext, dummyNewLink)

        self.assertEqual(
            dummyNewLink.value, "http://www.foo.com/x/relativelink.html")

    def test_TransformsLinkWithNoNetlocAndPathEndingWithNoExtension(self):
        # >>> urlparse("www.foo.com/x")
        # ParseResult(scheme='', netloc='', path='www.foo.com/x')
        dummyContext = {
            "currentLink": link.Link("www.foo.com/x")
            }
        dummyNewLink = link.Link("relativelink.html")
        sut = linkTransform.RelativeLinkTransform()

        sut.transform(dummyContext, dummyNewLink)

        self.assertEqual(dummyNewLink.value, "www.foo.com/relativelink.html")

    def test_TransformsLinkWithNoNetlocAndPathEndingWithFileExtension(self):
        # >>> urlparse("www.foo.com/x.html")
        # ParseResult(scheme='', netloc='', path='www.foo.com/x.html')
        dummyContext = {
            "currentLink": link.Link("www.foo.com/x.html")
            }
        dummyNewLink = link.Link("relativelink.html")
        sut = linkTransform.RelativeLinkTransform()

        sut.transform(dummyContext, dummyNewLink)

        self.assertEqual(dummyNewLink.value, "www.foo.com/relativelink.html")

    def test_TransformsLinkWithNoNetlocAndPathWithDirAndFileExtension(self):
        # >>> urlparse("www.foo.com/x/y.html")
        # ParseResult(scheme='', netloc='', path='www.foo.com/x/y.html')
        dummyContext = {
            "currentLink": link.Link("www.foo.com/x/y.html")
            }
        dummyNewLink = link.Link("relativelink.html")
        sut = linkTransform.RelativeLinkTransform()

        sut.transform(dummyContext, dummyNewLink)

        self.assertEqual(
            dummyNewLink.value, "www.foo.com/x/relativelink.html")


if __name__ == '__main__':
    unittest.main()
