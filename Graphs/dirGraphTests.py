import dirGraph
import unittest


class ShortestPathBFSTests(unittest.TestCase):
    def test_EmptyGraph(self):
        expected = []
        sut = dirGraph.DirGraph()
        
        actual = sut.shortest_path_bfs(None, None, [])

        self.assertEqual(expected, actual)

    def test_OneNodeGraph(self):
        n1 = dirGraph.DirNode(0, [])
        expected = [n1]
        sut = dirGraph.DirGraph()
        
        actual = sut.shortest_path_bfs(n1, n1, [])

        self.assertEqual(expected, actual)

    def test_TwoNodeGraph(self):
        n2 = dirGraph.DirNode(1, [])
        n1 = dirGraph.DirNode(0, [n2])
        expected = [n1, n2]
        sut = dirGraph.DirGraph()
        
        actual = sut.shortest_path_bfs(n1, n2, [])

        self.assertEqual(expected, actual)

    def test_ThreeNodeGraph_ShortestPath3(self):
        n3 = dirGraph.DirNode(3, [])
        n2 = dirGraph.DirNode(2, [n3])
        n1 = dirGraph.DirNode(1, [n2])
        expected = [n1, n2, n3]
        sut = dirGraph.DirGraph()
        
        actual = sut.shortest_path_bfs(n1, n3, [])

        self.assertEqual(expected, actual)

    def test_ThreeNodeGraph_ShortestPath2(self):
        n3 = dirGraph.DirNode(3, [])
        n2 = dirGraph.DirNode(2, [n3])
        n1 = dirGraph.DirNode(1, [n2, n3])
        expected = [n1, n3]
        sut = dirGraph.DirGraph()
        
        actual = sut.shortest_path_bfs(n1, n3, [])

        self.assertEqual(expected, actual)

    def test_4NodeGraph_ShortestPath2(self):
        n4 = dirGraph.DirNode(4, [])
        n3 = dirGraph.DirNode(3, [n4])
        n2 = dirGraph.DirNode(2, [n4])
        n1 = dirGraph.DirNode(1, [n2, n3])
        # could also be [n1, n3, n4]
        expected = [n1, n2, n4]
        sut = dirGraph.DirGraph()
        
        actual = sut.shortest_path_bfs(n1, n4, [])

        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()
