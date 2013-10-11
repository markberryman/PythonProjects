import adjListGraph
import dfsWithColors
import unittest
import unittest.mock


class DfsWithColorsTests(unittest.TestCase):
    def test_ReturnsPathForFifteenVerticeGraph(self):
        g = adjListGraph.AdjListGraph()
        g.add_node(0)
        g.add_node(1)
        g.add_node(2)
        g.add_node(3)
        g.add_node(4)
        g.add_node(5)
        g.add_node(6)
        g.add_node(7)
        g.add_node(8)
        g.add_node(9)
        g.add_node(10)
        g.add_node(11)
        g.add_node(12)
        g.add_node(13)
        g.add_node(14)
        g.add_node(15)
        
        g.add_edge(0, 1, 0)
        g.add_edge(0, 6, 0)
        g.add_edge(0, 8, 0)
        g.add_edge(1, 2, 0)
        g.add_edge(1, 3, 0)
        g.add_edge(2, 10, 0)
        g.add_edge(2, 11, 0)
        g.add_edge(3, 4, 0)
        g.add_edge(3, 12, 0)
        g.add_edge(4, 5, 0)
        g.add_edge(4, 13, 0)
        g.add_edge(5, 6, 0)
        g.add_edge(5, 9, 0)
        g.add_edge(6, 7, 0)
        g.add_edge(7, 8, 0)
        g.add_edge(7, 9, 0)
        g.add_edge(8, 14, 0)
        g.add_edge(9, 15, 0)

        sut = dfsWithColors.DfsWithColors(g)
        sut.dfs(0)
        expected = [0, 1, 3, 4, 5, 6, 7, 9, 15]

        actual = sut.find_path(sut.vPath, 0, 15)

        self.assertEqual(expected, actual)

# todo - add tests for dfs_visit


class FindPathTests(unittest.TestCase):
    def test_ReturnsPathForTwoVerticeGraph(self):
        # vertice 1 points back to vertice 0
        vPath = [-1, 0]
        expected = [0, 1]
        
        actual = dfsWithColors.DfsWithColors.find_path(vPath, 0, 1)

        self.assertEqual(expected, actual)

    def test_ReturnsEmptyListWhenPathDoesNotExists(self):
        # vertice 1 points back to vertice 0
        vPath = [-1, -1, 1]
        expected = []
        
        actual = dfsWithColors.DfsWithColors.find_path(vPath, 0, 2)

        self.assertEqual(expected, actual)


class DfsTests(unittest.TestCase):
    def test_InitializesColorTrackingData(self):
        g = adjListGraph.AdjListGraph()
        g.add_node(0)
        g.add_node(1)
        sut = dfsWithColors.DfsWithColors(g)
        # stub method
        sut.dfs_visit = unittest.mock.MagicMock(name='method')

        sut.dfs(0)

        self.assertEqual("w", sut.vColors[0])
        self.assertEqual("w", sut.vColors[1])
    
    def test_InitializesPathTrackingData(self):
        g = adjListGraph.AdjListGraph()
        g.add_node(0)
        g.add_node(1)
        sut = dfsWithColors.DfsWithColors(g)
        # stub method
        sut.dfs_visit = unittest.mock.MagicMock(name='method')

        sut.dfs(0)

        self.assertEqual(-1, sut.vPath[0])
        self.assertEqual(-1, sut.vPath[1])    


if __name__ == '__main__':
    unittest.main()
