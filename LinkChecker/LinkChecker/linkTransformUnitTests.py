import link
import linkTransform
import unittest


class RelativeLinkTransformUnitTests(unittest.TestCase):
    def test_DoesNotTransformsAbsoluteLink(self):
        dummyCurrentLink = link.Link("some link")
        dummyNewLink = link.Link("http://www.foo.com")
        sut = linkTransform.RelativeLinkTransform()

        sut.transform(dummyCurrentLink, dummyNewLink)

        self.assertEqual(dummyNewLink.value, "http://www.foo.com")

    def test_DoesNotTransformsMailToLink(self):
        dummyCurrentLink = link.Link("http://www.foo.com")
        dummyNewLink = link.Link("mailto:...")
        sut = linkTransform.RelativeLinkTransform()

        sut.transform(dummyCurrentLink, dummyNewLink)

        self.assertEqual(dummyNewLink.value, "mailto:...")

    def test_TransformsRelativeLinkWithNetlocAndNoPath(self):
        # >>> urlparse("http://www.foo.com")
        # ParseResult(scheme='http', netloc='www.foo.com', path='', params='', query='', fragment='')
        dummyCurrentLink = link.Link("http://www.foo.com")
        dummyNewLink = link.Link("relativelink.html")
        sut = linkTransform.RelativeLinkTransform()

        sut.transform(dummyCurrentLink, dummyNewLink)

        self.assertEqual(dummyNewLink.value, "http://www.foo.com/relativelink.html")

    def test_TransformsRelativeLinkWithNoNetloc(self):
        # >>> urlparse("www.foo.com")
        # ParseResult(scheme='', netloc='', path='www.foo.com', params='', query='', fragment='')
        dummyCurrentLink = link.Link("www.foo.com")
        dummyNewLink = link.Link("relativelink.html")
        sut = linkTransform.RelativeLinkTransform()

        sut.transform(dummyCurrentLink, dummyNewLink)

        self.assertEqual(dummyNewLink.value, "www.foo.com/relativelink.html")

    def test_TransformsRelativeLinkWithNetlocAndOnlySlashForPath(self):
        # >>> urlparse("http://www.foo.com/")
        # ParseResult(scheme='http', netloc='www.foo.com', path='/', params='', query='', fragment='')
        dummyCurrentLink = link.Link("http://www.foo.com/")
        dummyNewLink = link.Link("relativelink.html")
        sut = linkTransform.RelativeLinkTransform()

        sut.transform(dummyCurrentLink, dummyNewLink)

        self.assertEqual(dummyNewLink.value, "http://www.foo.com/relativelink.html")

    def test_TransformsRelativeLinkWithNoNetlocAndPathEndingWithSlash(self):
        # >>> urlparse("www.foo.com/")
        # ParseResult(scheme='', netloc='', path='www.foo.com/', params='', query='', fragment='')
        dummyCurrentLink = link.Link("www.foo.com/")
        dummyNewLink = link.Link("relativelink.html")
        sut = linkTransform.RelativeLinkTransform()

        sut.transform(dummyCurrentLink, dummyNewLink)

        self.assertEqual(dummyNewLink.value, "www.foo.com/relativelink.html")

    def test_TransformsRelativeLinkWithNetlocAndPathEndingWithFileWithNoExtension(self):
        # >>> urlparse("http://www.foo.com/x")
        # ParseResult(scheme='http', netloc='www.foo.com', path='/x', params='', query='', fragment='')
        dummyCurrentLink = link.Link("http://www.foo.com/x")
        dummyNewLink = link.Link("relativelink.html")
        sut = linkTransform.RelativeLinkTransform()

        sut.transform(dummyCurrentLink, dummyNewLink)

        self.assertEqual(dummyNewLink.value, "http://www.foo.com/relativelink.html")

    def test_TransformsRelativeLinkWithNetlocAndPathEndingWithFileWithExtension(self):
        # >>> urlparse("http://www.foo.com/x.html")
        # ParseResult(scheme='http', netloc='www.foo.com', path='/x.html', params='', query='', fragment='')
        dummyCurrentLink = link.Link("http://www.foo.com/x.html")
        dummyNewLink = link.Link("relativelink.html")
        sut = linkTransform.RelativeLinkTransform()

        sut.transform(dummyCurrentLink, dummyNewLink)

        self.assertEqual(dummyNewLink.value, "http://www.foo.com/relativelink.html")

    def test_TransformsRelativeLinkWithNetlocAndPathContainingDirectoryAndFileWithExtension(self):
        # >>> urlparse("http://www.foo.com/x/y.html")
        # ParseResult(scheme='http', netloc='www.foo.com', path='/x/y.html', params='', query='', fragment='')
        dummyCurrentLink = link.Link("http://www.foo.com/x/y.html")
        dummyNewLink = link.Link("relativelink.html")
        sut = linkTransform.RelativeLinkTransform()

        sut.transform(dummyCurrentLink, dummyNewLink)

        self.assertEqual(dummyNewLink.value, "http://www.foo.com/x/relativelink.html")

    def test_TransformsRelativeLinkWithNoNetlocAndPathEndingWithFileWithNoExtension(self):
        # >>> urlparse("www.foo.com/x")
        # ParseResult(scheme='', netloc='', path='www.foo.com/x', params='', query='', fragment='')
        dummyCurrentLink = link.Link("www.foo.com/x")
        dummyNewLink = link.Link("relativelink.html")
        sut = linkTransform.RelativeLinkTransform()

        sut.transform(dummyCurrentLink, dummyNewLink)

        self.assertEqual(dummyNewLink.value, "www.foo.com/relativelink.html")

    def test_TransformsRelativeLinkWithNoNetlocAndPathEndingWithFileWithExtension(self):
        # >>> urlparse("www.foo.com/x.html")
        # ParseResult(scheme='', netloc='', path='www.foo.com/x.html', params='', query='', fragment='')
        dummyCurrentLink = link.Link("www.foo.com/x.html")
        dummyNewLink = link.Link("relativelink.html")
        sut = linkTransform.RelativeLinkTransform()

        sut.transform(dummyCurrentLink, dummyNewLink)

        self.assertEqual(dummyNewLink.value, "www.foo.com/relativelink.html")

    def test_TransformsRelativeLinkWithNoNetlocAndPathContainingDirectoryAndFileWithExtension(self):
        # >>> urlparse("www.foo.com/x/y.html")
        # ParseResult(scheme='', netloc='', path='www.foo.com/x/y.html', params='', query='', fragment='')
        dummyCurrentLink = link.Link("www.foo.com/x/y.html")
        dummyNewLink = link.Link("relativelink.html")
        sut = linkTransform.RelativeLinkTransform()

        sut.transform(dummyCurrentLink, dummyNewLink)

        self.assertEqual(dummyNewLink.value, "www.foo.com/x/relativelink.html")


if __name__ == '__main__':
    unittest.main()
