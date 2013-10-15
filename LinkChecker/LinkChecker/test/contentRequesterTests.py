import contentRequester
import unittest


class ContentRequester_RequestUrlTests(unittest.TestCase):
    def test_RaisesTypeErrorIfUrlIsNone(self):
        sut = contentRequester.ContentRequester()

        self.assertRaises(TypeError, sut.request_url, None)


if __name__ == '__main__':
    unittest.main()
