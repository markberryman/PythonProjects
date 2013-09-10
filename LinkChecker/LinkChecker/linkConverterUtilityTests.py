import linkConverterUtility
import unittest


class ConvertRelativeLinkToAbsoluateLinkTests(unittest.TestCase):
    def test_ConvertsRelativeLinkToAbsoluateLink(self):
        host = "www.foo.com"
        link = "/foo.html"
        
        result = linkConverterUtility.LinkConverterUtility.convert_relative_link_to_absolute_link(host, link)

        self.assertEqual(result, "www.foo.com/foo.html")


if __name__ == '__main__':
    unittest.main()
