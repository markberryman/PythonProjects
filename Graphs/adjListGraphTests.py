import adjListGraph
import unittest


class Test_adjListGraphTests(unittest.TestCase):
    def test_AddNewNodeToGraphAddsNode(self):
        node = adjListGraph.Node(0)
        sut = adjListGraph.AdjListGraph()

        sut.add_node(node)

        self.assertEqual(1, len(sut.graph))

    def test_AddDupeNodeRaisesExc(self):
        node1 = adjListGraph.Node(0)
        node2 = adjListGraph.Node(0)
        sut = adjListGraph.AdjListGraph()

        sut.add_node(node1)

        self.assertRaises(ValueError, sut.add_node, node2)

    def test_AddingTwoNodesToGraphAddsTwoNodes(self):
        node1 = adjListGraph.Node(0)
        node2 = adjListGraph.Node(1)
        sut = adjListGraph.AdjListGraph()

        sut.add_node(node1)
        sut.add_node(node2)

        self.assertEqual(2, len(sut.graph))

if __name__ == '__main__':
    unittest.main()
