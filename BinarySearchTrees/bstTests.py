import bst
import unittest


class InsertTests(unittest.TestCase):
    def test_FirstInsertSetsRootNode(self):
        node = bst.Node(1)
        sut = bst.BST()

        sut.insert(node)

        self.assertEqual(node, sut.root)

    def test_InsertNodeAsLeftChild(self):
        rootNode = bst.Node(1)
        leftChild = bst.Node(0)
        sut = bst.BST()

        sut.insert(rootNode)
        sut.insert(leftChild)

        self.assertEqual(rootNode.lchild, leftChild)

    def test_InsertNodeAsRightChild(self):
        rootNode = bst.Node(1)
        rightChild = bst.Node(2)
        sut = bst.BST()

        sut.insert(rootNode)
        sut.insert(rightChild)

        self.assertEqual(rootNode.rchild, rightChild)

    def test_InsertTwoNodesAsLeftChild(self):
        rootNode = bst.Node(2)
        leftChild1 = bst.Node(1)
        leftChild2 = bst.Node(0)
        sut = bst.BST()

        sut.insert(rootNode)
        sut.insert(leftChild1)
        sut.insert(leftChild2)

        self.assertEqual(rootNode.lchild, leftChild1)
        self.assertEqual(leftChild1.lchild, leftChild2)


class GetSmallestNodeTests(unittest.TestCase):
    def test_ReturnsNoneForEmptyTree(self):
        sut = bst.BST()

        result = sut.get_smallest_node()

        self.assertIsNone(result)

    def test_ReturnsSmallestNodeForSingleNodeTree(self):
        node = bst.Node(0)
        sut = bst.BST()
        sut.insert(node)

        result = sut.get_smallest_node()

        self.assertEqual(node, result)

    def test_ReturnsSmallestNodeForTwoNodeTree(self):
        node1 = bst.Node(2)
        node2 = bst.Node(1)
        sut = bst.BST()
        sut.insert(node1)
        sut.insert(node2)

        result = sut.get_smallest_node()

        self.assertEqual(node2, result)


class SelectTests(unittest.TestCase):
    def test_ReturnsNoneForEmptyTree(self):
        sut = bst.BST()

        result = sut.select(1)

        self.assertIsNone(result)

    def test_ReturnsNoneForNonPositiveIndex(self):
        sut = bst.BST()

        result = sut.select(0)

        self.assertIsNone(result)

    def test_ReturnsRootNodeIfIndexIsOne(self):
        node = bst.Node(1)
        sut = bst.BST()
        sut.insert(node)

        result = sut.select(1)

        self.assertEqual(sut.root, result)

    def test_ReturnsSecondOrderedNodeIfIndexIsTwo(self):
        node1 = bst.Node(1)
        node2 = bst.Node(2)
        sut = bst.BST()
        sut.insert(node1)
        sut.insert(node2)

        result = sut.select(2)

        self.assertEqual(node2, result)

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
