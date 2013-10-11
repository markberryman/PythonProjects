import adjListGraph
import unittest


class GetVerticeNeighbors(unittest.TestCase):
    # todo - add test for non-existent v
    def test_NonExistentVerticeRaisesException(self):
        sut = adjListGraph.AdjListGraph()

        self.assertRaises(ValueError, sut.get_vertice_neighbors, 0)
        
    def test_VerticeWithZeroNeighbors(self):
        sut = adjListGraph.AdjListGraph()
        sut.add_node(0)
        expected = []

        actual = sut.get_vertice_neighbors(0)

        self.assertEqual(expected, actual)

    def test_VerticeWithTwoNeighbors(self):
        sut = adjListGraph.AdjListGraph()
        sut.add_node(0)
        sut.add_node(1)
        sut.add_node(2)
        sut.add_edge(0, 1, 0)
        sut.add_edge(0, 2, 0)
        expected = [1, 2]

        actual = sut.get_vertice_neighbors(0)

        self.assertEqual(expected, actual)


class GetNumNodesTests(unittest.TestCase):
    def test_GraphWithZeroVertices(self):
        sut = adjListGraph.AdjListGraph()
        expected = 0

        actual = sut.get_num_vertices()

        self.assertEqual(expected, actual)

    def test_GraphWithOneVertice(self):
        sut = adjListGraph.AdjListGraph()
        sut.add_node(0)
        expected = 1

        actual = sut.get_num_vertices()

        self.assertEqual(expected, actual)


class AddEdgeTests(unittest.TestCase):
    def test_AddEdgeForNonExistantFirstNode(self):
        sut = adjListGraph.AdjListGraph()

        self.assertRaises(ValueError, sut.add_edge, 0, 1, 50)

    # not a true unit test b/c we're adding a node
    # todo - mock this call
    def test_AddEdgeForNonExistantSecondNode(self):
        sut = adjListGraph.AdjListGraph()
        sut.add_node(0)

        self.assertRaises(ValueError, sut.add_edge, 0, 1, 50)

    # not a true unit test b/c we're adding a node
    # todo - mock this call
    def test_AddEdgeBetweenNodes(self):
        sut = adjListGraph.AdjListGraph()
        sut.add_node(0)
        sut.add_node(1)

        sut.add_edge(0, 1, 50)

        self.assertEqual(sut.graph[0][0], [1, 50])
        self.assertEqual(sut.graph[1][0], [0, 50])

    # not a true unit test b/c we're adding a node
    # todo - mock this call
    def test_AddTwoEdgesFromANode(self):
        sut = adjListGraph.AdjListGraph()
        sut.add_node(0)
        sut.add_node(1)
        sut.add_node(2)

        sut.add_edge(0, 1, 50)
        sut.add_edge(0, 2, 25)

        self.assertEqual(sut.graph[0][0], [1, 50])
        self.assertEqual(sut.graph[0][1], [2, 25])

    # not a true unit test b/c we're adding a node
    # todo - mock this call
    def test_AddDupeEdgeRaisesValueException(self):
        sut = adjListGraph.AdjListGraph()
        sut.add_node(0)
        sut.add_node(1)

        sut.add_edge(0, 1, 50)

        self.assertRaises(ValueError, sut.add_edge, 0, 1, 50)


class AddNodeTests(unittest.TestCase):
    def test_AddNewNodeToGraphAddsNode(self):
        sut = adjListGraph.AdjListGraph()

        sut.add_node(0)

        self.assertEqual(1, len(sut.graph))

    def test_AddDupeNodeRaisesExc(self):
        sut = adjListGraph.AdjListGraph()

        sut.add_node(0)

        self.assertRaises(ValueError, sut.add_node, 0)

    def test_AddingTwoNodesToGraphAddsTwoNodes(self):
        sut = adjListGraph.AdjListGraph()

        sut.add_node(0)
        sut.add_node(1)

        self.assertEqual(2, len(sut.graph))


if __name__ == '__main__':
    unittest.main()
