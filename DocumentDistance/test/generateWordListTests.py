import docdist1
import unittest

class GenerateWordListTests(unittest.TestCase):
    def test_ReturnsCorrectWordCountForVerneTextFile(self):
        filename = "..\\t1.vern.txt"

        result = docdist1.generateWordList(filename)

        self.assertEqual(2150, len(result))

if __name__ == '__main__':
    unittest.main()
