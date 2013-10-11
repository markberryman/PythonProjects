import adjListGraph
import unittest


class AddEdgeTests(unittest.TestCase):
    def test_AddEdgeForNonExistantFirstNode(self):
        edge1 = adjListGraph.Edge(0, 1, 0)
        sut = adjListGraph.AdjListGraph()

        self.assertRaises(ValueError, sut.add_edge, edge1)

    # not a true unit test b/c we're adding a node
    # todo - mock this call
    def test_AddEdgeForNonExistantFirstNode(self):
        edge1 = adjListGraph.Edge(0, 1, 0)
        sut = adjListGraph.AdjListGraph()
        node1 = adjListGraph.Node(0)
        sut.add_node(node1)

        self.assertRaises(ValueError, sut.add_edge, edge1)


class AddNodeTests(unittest.TestCase):
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
