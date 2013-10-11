import adjListGraph
import dfsBasic
import unittest


class SearchTests(unittest.TestCase):
    def test_NoPathExists(self):
        g = adjListGraph.AdjListGraph()
        g.add_node(0)
        g.add_node(1)
        expected = []

        actual = dfsBasic.DfsBasic.search(g.graph, 0, 1)

        self.assertEqual(expected, actual)

    def test_OneStepPathExistsBetweenTwoNodes(self):
        g = adjListGraph.AdjListGraph()
        g.add_node(0)
        g.add_node(1)
        g.add_edge(0, 1, 50)
        expected = [0, 1]

        actual = dfsBasic.DfsBasic.search(g.graph, 0, 1)

        self.assertEqual(expected, actual)

    def test_TwoStepPathExistsBetweenThreeNodes(self):
        # 0-1-2
        g = adjListGraph.AdjListGraph()
        g.add_node(0)
        g.add_node(1)
        g.add_node(2)
        g.add_edge(0, 1, 50)
        g.add_edge(1, 2, 50)
        expected = [0, 1, 2]

        actual = dfsBasic.DfsBasic.search(g.graph, 0, 2)

        self.assertEqual(expected, actual)

    def test_GraphNeedingBacktracking(self):
        # 0-1
        # 0-2-3 (end)
        g = adjListGraph.AdjListGraph()
        g.add_node(0)
        g.add_node(1)
        g.add_node(2)
        g.add_node(3)
        g.add_edge(0, 2, 50)
        g.add_edge(0, 1, 50)
        g.add_edge(2, 3, 50)
        expected = [0, 2, 3]

        actual = dfsBasic.DfsBasic.search(g.graph, 0, 3)

        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
