import docdist1
import unittest

class GenerateWordListTests(unittest.TestCase):
    def test_ReturnsCorrectWordCountForVerneTextFile(self):
        filename = "../t1.verne.txt"

        result = docdist1.generateWordList(filename)

        self.assertEqual(8943, len(result))

    def test_ReturnsCorrectWordCountForBobseyTextFile(self):
        filename = "../t2.bobsey.txt"

        result = docdist1.generateWordList(filename)

        self.assertEqual(49785, len(result))

if __name__ == '__main__':
    unittest.main()
