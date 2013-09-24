import binaryPlusOne
import unittest


class AddOneTests(unittest.TestCase):
    def test_AddOneToZero(self):
        num = [0]
        expected = [1]
        
        actual = binaryPlusOne.BinaryPlusOne.add_one(num)

        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
