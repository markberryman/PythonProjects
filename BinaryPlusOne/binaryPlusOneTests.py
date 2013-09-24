import binaryPlusOne
import unittest


class AddOneTests(unittest.TestCase):
    def test_AddOneToZero(self):
        num = [0]
        expected = [1]
        
        binaryPlusOne.BinaryPlusOne.add_one(num)

        self.assertEqual(expected, num)

    def test_AddOneToOne(self):
        num = [0, 1]
        expected = [1, 0]
        
        binaryPlusOne.BinaryPlusOne.add_one(num)

        self.assertEqual(expected, num)

    def test_AddOneToTwo(self):
        num = [1, 0]
        expected = [1, 1]
        
        binaryPlusOne.BinaryPlusOne.add_one(num)

        self.assertEqual(expected, num)

    def test_AddOneToThree(self):
        num = [0, 1, 1]
        expected = [1, 0, 0]
        
        binaryPlusOne.BinaryPlusOne.add_one(num)

        self.assertEqual(expected, num)

    def test_AddOneToFour(self):
        num = [1, 0, 0]
        expected = [1, 0, 1]
        
        binaryPlusOne.BinaryPlusOne.add_one(num)

        self.assertEqual(expected, num)

    def test_AddOneToFive(self):
        num = [1, 0, 1]
        expected = [1, 1, 0]
        
        binaryPlusOne.BinaryPlusOne.add_one(num)

        self.assertEqual(expected, num)


if __name__ == '__main__':
    unittest.main()
