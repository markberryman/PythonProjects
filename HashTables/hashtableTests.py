import hashtable
import unittest


class AsciiSumHashTests(unittest.TestCase):
    def test_SingleCharString(self):
        s = "A"
        expected = 0
        sut = hashtable.Hashtable(1)

        actual = sut.asciiSumHashFn(s)
        
        self.assertEqual(expected, actual)

    def test_TwoCharString(self):
        s = "AA"    # 65 + 65
        expected = 4
        sut = hashtable.Hashtable(7)

        actual = sut.asciiSumHashFn(s)
        
        self.assertEqual(expected, actual)


class FindTests(unittest.TestCase):
    def test_NotExist(self):
        sut = hashtable.Hashtable(1)

        actual = sut.find("x")

        self.assertIsNone(actual)

    def test_ItemExists(self):
        s = "x"
        sut = hashtable.Hashtable(1)
        sut.add(s)

        actual = sut.find("x")

        self.assertEqual(s, actual)

class AddTests(unittest.TestCase):
    def test_ReturnsFalseOnHashCollision(self):
        s1 = "x"
        s2 = "x"
        sut = hashtable.Hashtable(1)
        sut.add(s1)

        actual = sut.add(s2)

        self.assertFalse(actual)

    def test_ReturnsTrueOnSuccessfullAdd(self):
        s1 = "x"
        sut = hashtable.Hashtable(1)

        actual = sut.add(s1)

        self.assertTrue(actual)

    def test_AddOneItemToOneSlotTable(self):
        s = "x"
        sut = hashtable.Hashtable(1)

        sut.add(s)

        self.assertEqual(s, sut.table[0][0])

    def test_AddTwoItemsSameHashToOneSlotTable(self):
        s1 = "x"
        s2 = "y"
        sut = hashtable.Hashtable(1)        

        sut.add(s1)
        sut.add(s2)

        self.assertEqual(s1, sut.table[0][0])
        self.assertEqual(s2, sut.table[0][1])


class RemoveTests(unittest.TestCase):
    def test_ReturnsFalseIfItemNotFound(self):
        sut = hashtable.Hashtable(1)

        actual = sut.remove("x")

        self.assertFalse(actual)

    def test_ReturnsTrueIfItemFound(self):
        s1 = "x"
        sut = hashtable.Hashtable(1)
        sut.add(s1)

        actual = sut.remove(s1)

        self.assertTrue(actual)

    def test_RemovesItem(self):
        s1 = "x"
        sut = hashtable.Hashtable(1)
        sut.add(s1)

        actual = sut.remove(s1)

        self.assertEqual(0, len(sut.table[0]))


if __name__ == '__main__':
    unittest.main()
