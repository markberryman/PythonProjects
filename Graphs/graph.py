class Graph(object):
    """A graph."""
    def __init__(self, nodes):
        self.nodes = nodes

    def shortest_path_bfs(self, curNode, goalNode, path):
        """Use breadth-first search to find shortest path to specific node."""

        assert curNode is not None
        assert goalNode is not None
        assert path is not None

        # found desired node?
        if (curNode.id == goalNode.id):
            path.append(goalNode)
            return path

        # add start node to queue
        # process head of queue
        
        # look at nodes edges and add them to queue
        # update path; don't forget to clone!