class DirNode(object):
    """A directed node."""
    def __init__(self, id, edges):
        self.id = id
        self.edges = edges


class DirGraph(object):
    """A directed graph w/ breadth-first search."""
    def shortest_path_bfs(self, curNode, goalNode, path):
        """Use breadth-first search to find shortest path to specific node."""

        assert path is not None

        if ((curNode is None) or (goalNode is None)):
            return []

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
