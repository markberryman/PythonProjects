class Graph(object):
    """A graph."""
    def __init__(self, nodes):
        self.nodes = nodes

    def shortest_path_bfs(self, curNode, goalNode, path):
        """Use breadth-first search to find shortest path to specific node."""

        assert curNode is not None
        assert goalNode is not None
        assert path is not None

        path.append(curNode)

        # special case of 1 node graph
        if (curNode == goalNode):
            return path
       
        # for each "next node", see if it's the end node
        for i in range(len(curNode.edges)):
            if (curNode.edges[i].id == goalNode.id):
                path.append(goalNode)
                return path
            
        # we've evaluated all nodes at the current depth
        # recurse
        for i in range(len(curNode.edges)):
            result = self.shortest_path_bfs(curNode.edges[i], goalNode, list(path))

            if (result is not None):
                return result
