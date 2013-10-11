import adjListGraph
import dfsWithColors
import unittest
import unittest.mock


# todo - add tests for dfs_visit

class FindPathTests(unittest.TestCase):
    def test_ReturnsPathWhenPathExists(self):
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
