class Graph(object):
    """A graph."""
    def __init__(self, nodes):
        self.nodes = nodes
        self.nodeQueue = []

    def shortest_path_bfs(self, curNode, goalNode, path):
        """Use breadth-first search to find shortest path to specific node."""

        assert curNode is not None
        assert goalNode is not None
        assert path is not None

        path.append(curNode)

        # found desired node?
        if (curNode.id == goalNode.id):
            return path
        
        for node in curNode.edges:
            self.nodeQueue.append(node)

        # update path; don't forget to clone!
        assert len(self.nodeQueue) > 0

        return self.shortest_path_bfs(self.nodeQueue.pop(0), goalNode, list(path))