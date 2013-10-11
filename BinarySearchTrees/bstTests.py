import bst
import unittest


class InOrderTraversalTests(unittest.TestCase):
    def test_OneNodeTree(self):
        node1 = bst.Node(1)
        sut = bst.BST()
        sut.insert(node1)
        expected = [1]
        actual = []

        sut.inorder_traversal(sut.root, actual)

        self.assertEqual(expected, actual)
        
    def test_SixNodeTree(self):
        node1 = bst.Node(1)
        node2 = bst.Node(2)
        node3 = bst.Node(3)
        node4 = bst.Node(4)
        node5 = bst.Node(5)
        node6 = bst.Node(6)
        sut = bst.BST()
        sut.insert(node4)
        sut.insert(node5)
        sut.insert(node6)
        sut.insert(node2)
        sut.insert(node1)
        sut.insert(node3)
        expected = [1, 2, 3, 4, 5, 6]
        actual = []

        sut.inorder_traversal(sut.root, actual)

        self.assertEqual(expected, actual)


class PreOrderTraversalTests(unittest.TestCase):
    def test_OneNodeTree(self):
        node1 = bst.Node(1)
        sut = bst.BST()
        sut.insert(node1)
        expected = [1]
        actual = []

        sut.preorder_traversal(sut.root, actual)

        self.assertEqual(expected, actual)
        
    def test_SixNodeTree(self):
        node1 = bst.Node(1)
        node2 = bst.Node(2)
        node3 = bst.Node(3)
        node4 = bst.Node(4)
        node5 = bst.Node(5)
        node6 = bst.Node(6)
        sut = bst.BST()
        sut.insert(node4)
        sut.insert(node5)
        sut.insert(node6)
        sut.insert(node2)
        sut.insert(node1)
        sut.insert(node3)
        actual = []

        expected = [4, 2, 1, 3, 5, 6]

        sut.preorder_traversal(sut.root, actual)

        self.assertEqual(expected, actual)


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


class SelectTests(unittest.TestCase):
    def test_ReturnsNoneForInvalidIndex(self):
        sut = bst.BST()

        # 1 based indexing here so 0 index is invalid
        result = sut.select(sut.root, 0)

        self.assertIsNone(result)

    def test_ReturnsNoneForEmptyTree(self):
        sut = bst.BST()

        result = sut.select(sut.root, 1)

        self.assertIsNone(result)

    def test_ReturnsNoneForIndexLargerThanTreeSize(self):
        node41 = bst.Node(41)
        node46 = bst.Node(46)
        node49 = bst.Node(49)
        node64 = bst.Node(64)
        node79 = bst.Node(79)
        sut = bst.BST()
        sut.insert(node49)
        sut.insert(node79)
        sut.insert(node46)
        sut.insert(node41)
        sut.insert(node64)

        result = sut.select(sut.root, 99)

        self.assertIsNone(result)

    def test_ReturnsNodeAtIndexOne(self):
        node41 = bst.Node(41)
        node46 = bst.Node(46)
        node49 = bst.Node(49)
        node64 = bst.Node(64)
        node79 = bst.Node(79)
        sut = bst.BST()
        sut.insert(node49)
        sut.insert(node79)
        sut.insert(node46)
        sut.insert(node41)
        sut.insert(node64)

        result = sut.select(sut.root, 1)

        self.assertEqual(node41, result)

    def test_ReturnsNodeAtIndexThree(self):
        node41 = bst.Node(41)
        node46 = bst.Node(46)
        node49 = bst.Node(49)
        node64 = bst.Node(64)
        node79 = bst.Node(79)
        sut = bst.BST()
        sut.insert(node49)
        sut.insert(node79)
        sut.insert(node46)
        sut.insert(node41)
        sut.insert(node64)

        result = sut.select(sut.root, 3)

        self.assertEqual(node49, result)

    def test_ReturnsNodeAtIndexFive(self):
        node41 = bst.Node(41)
        node46 = bst.Node(46)
        node49 = bst.Node(49)
        node64 = bst.Node(64)
        node79 = bst.Node(79)
        sut = bst.BST()
        sut.insert(node49)
        sut.insert(node79)
        sut.insert(node46)
        sut.insert(node41)
        sut.insert(node64)

        result = sut.select(sut.root, 5)

        self.assertEqual(node79, result)


if __name__ == '__main__':
    unittest.main()
