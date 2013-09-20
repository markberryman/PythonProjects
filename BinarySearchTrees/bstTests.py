import bst
import unittest


class InsertTests(unittest.TestCase):
    def test_FirstInsertSetsRootNode(self):
        node = bst.Node(1)
        sut = bst.BST()

        sut.insert(node)

        self.assertEqual(node, sut.root)

#class TestBST(unittest.TestCase):
#    def setUp(self):
#        pass

#    def test(self):
#        t = bstselect.BST()
#        t.insert(0)
#        t.insert(10)
#        t.insert(5)

#        ans = t.select(1)
#        self.assertEqual(ans.key, 0)
#        ans = t.select(2)
#        self.assertEqual(ans.key, 5)
#        ans = t.select(3)
#        self.assertEqual(ans.key, 10)

#        ans = t.select(0)
#        self.assertEqual(ans, None)
#        ans = t.select(4)
#        self.assertEqual(ans, None)

#        t.insert(6)
#        t.insert(8)
#        t.insert(7)
#        ans = t.select(4)
#        self.assertEqual(ans.key, 7)

if __name__ == '__main__':
    unittest.main()
