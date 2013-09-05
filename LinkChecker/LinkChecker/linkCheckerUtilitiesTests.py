import linkCheckerUtilities
import unittest

class GetLinksFromMarkup(unittest.TestCase):
    def test_returnsNoneIfMarkupProvidedIsNone(self):
        result = linkCheckerUtilities.linkCheckerUtilities.get_links_from_markup(None, None)

        self.assertTrue(result is None)

if __name__ == '__main__':
    unittest.main()