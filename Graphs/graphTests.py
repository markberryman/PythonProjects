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

    def test_TwoNodeGraph(self):
        n2 = dirNode.DirNode(1, [])
        n1 = dirNode.DirNode(0, [n2])
        expected = [n1, n2]
        sut = graph.Graph([n1, n2])
        
        actual = sut.shortest_path_bfs(n1, n2, [])

        self.assertEqual(expected, actual)

    def test_ThreeNodeGraph_AllNodesInARow(self):
        n3 = dirNode.DirNode(3, [])
        n2 = dirNode.DirNode(2, [n3])
        n1 = dirNode.DirNode(1, [n2])
        expected = [n1, n2, n3]
        sut = graph.Graph([n1, n2, n3])
        
        actual = sut.shortest_path_bfs(n1, n3, [])

        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()
