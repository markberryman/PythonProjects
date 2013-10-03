import node
import graph


n1 = node.DirNode(1, [2])  # points to n2
n2 = node.DirNode(2, [])

g = graph.Graph([n1, n2])

