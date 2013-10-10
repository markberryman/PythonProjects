import exprTree
import unittest


class CalcTests(unittest.TestCase):
    def test_SingleExprTree(self):
        oprNode1 = exprTree.Node("+")
        opdNode1 = exprTree.Node(1)
        opdNode2 = exprTree.Node(2)
        oprNode1.lChild = opdNode1
        oprNode1.rChild = opdNode2
        expected = 3
        sut = exprTree.ExprTree()

        actual = sut.calc(oprNode1)

        self.assertEqual(expected, actual)

    def test_TwoExprTree(self):
        oprNode1 = exprTree.Node("+")
        oprNode2 = exprTree.Node("+")
        opdNode1 = exprTree.Node(1)
        opdNode2 = exprTree.Node(2)
        opdNode3 = exprTree.Node(3)
        oprNode1.lChild = oprNode2
        oprNode1.rChild = opdNode3
        oprNode2.lChild = opdNode1
        oprNode2.rChild = opdNode2

        expected = 6
        sut = exprTree.ExprTree()

        actual = sut.calc(oprNode1)

        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
