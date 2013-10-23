import tree
import unittest


class Tree_BfsTests(unittest.TestCase):
    def test_OneNode(self):
        n1 = tree.Node(1)
        expected = [1]

        actual = tree.Tree.bfs(n1)

        self.assertEqual(expected, actual)

    def test_ThreeNodeBalancedTree(self):
        n1 = tree.Node(1)
        n2 = tree.Node(2)
        n3 = tree.Node(3)
        n1.lChild = n2
        n1.rChild = n3
        expected = [1, 2, 3]

        actual = tree.Tree.bfs(n1)

        self.assertEqual(expected, actual)

    def test_SevenNodeBalancedTree(self):
        n1 = tree.Node(1)
        n2 = tree.Node(2)
        n3 = tree.Node(3)
        n4 = tree.Node(4)
        n5 = tree.Node(5)
        n6 = tree.Node(6)
        n7 = tree.Node(7)

        n1.lChild = n2
        n1.rChild = n3

        n2.lChild = n4
        n2.rChild = n5

        n3.lChild = n6
        n3.rChild = n7

        expected = [1, 2, 3, 4, 5, 6, 7]

        actual = tree.Tree.bfs(n1)

        self.assertEqual(expected, actual)


class Tree_DfsTests(unittest.TestCase):
    def test_OneNode(self):
        n1 = tree.Node(1)
        expected = [1]

        actual = tree.Tree.dfs(n1)

        self.assertEqual(expected, actual)

    def test_ThreeNodeBalancedTree(self):
        n1 = tree.Node(1)
        n2 = tree.Node(2)
        n3 = tree.Node(3)
        n1.lChild = n2
        n1.rChild = n3
        expected = [1, 3, 2]

        actual = tree.Tree.dfs(n1)

        self.assertEqual(expected, actual)

    def test_SevenNodeBalancedTree(self):
        n1 = tree.Node(1)
        n2 = tree.Node(2)
        n3 = tree.Node(3)
        n4 = tree.Node(4)
        n5 = tree.Node(5)
        n6 = tree.Node(6)
        n7 = tree.Node(7)

        n1.lChild = n2
        n1.rChild = n3

        n2.lChild = n4
        n2.rChild = n5

        n3.lChild = n6
        n3.rChild = n7

        expected = [1, 3, 7, 6, 2, 5, 4]

        actual = tree.Tree.dfs(n1)

        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
