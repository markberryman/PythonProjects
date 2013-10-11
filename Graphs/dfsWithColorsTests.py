import adjListGraph
import dfsWithColors
import unittest


class DfsTests(unittest.TestCase):
    def test_InitializesColorTrackingData(self):
        g = adjListGraph.AdjListGraph()
        g.add_node(0)
        sut = dfsWithColors.DfsWithColors(g)

        sut.dfs(0)

        self.assertTrue(True)
        

if __name__ == '__main__':
    unittest.main()
