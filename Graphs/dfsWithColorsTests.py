import adjListGraph
import dfsWithColors
import unittest
import unittest.mock


# todo - add tests for dfs_visit


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
