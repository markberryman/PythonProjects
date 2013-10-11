import adjListGraph
import unittest


class DfsTests(unittest.TestCase):
    def test_NoPathExists(self):
        g = adjListGraph.AdjListGraph()
        g.add_node(0)
        g.add_node(1)
        expected = None

        actual = adjListGraph.GraphSearch.dfs(g, 0, 1)

        self.assertEqual(expected, actual)

    def test_OneStepPathExistsBetweenTwoNodes(self):
        g = adjListGraph.AdjListGraph()
        g.add_node(0)
        g.add_node(1)
        g.add_edge(0, 1, 50)
        expected = [0, 1]

        actual = adjListGraph.GraphSearch.dfs(g, 0, 1)

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
