import graph
import dirNode
import unittest


class ShortestPathBFSTests(unittest.TestCase):
    def test_OneNodeGraph(self):
        n1 = dirNode.DirNode(0, [])
        expected = [n1]
        sut = graph.Graph([n1])
        
        actual = sut.shortest_path_bfs(n1, n1, [])

        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
