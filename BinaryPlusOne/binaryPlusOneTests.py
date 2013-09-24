import binaryPlusOne
import unittest


class AddOneTests(unittest.TestCase):
    def test_AddOneToZero(self):
        num = [0]
        expected = [1]
        
        binaryPlusOne.BinaryPlusOne.add_one(num)

        self.assertEqual(expected, num)


if __name__ == '__main__':
    unittest.main()
