class DfsWithColors(object):
    """Depth-first search of a graph using colors for
    optimization."""
    #@staticmethod
    #def find_path(graphData, start, end):
    #    """Taking the data returned by the dfs that uses
    #    coloring, see if there exists a path b/w the
    #    start and end vertices."""

    @staticmethod
    def dfs(graph, start, end):
        """Using depth-first search, builds entire picture
        of graph using a coloring algorithm for optimization.
        Resulting calculated data can be used to check for a
        path (not necessarily shortest) b/w any two vertices."""
        vColors = []
        vPath = []
        
        # coloring each node white and 
        # initializing path data
        for x in range(len(graph)):
            vColors.append("w")
            vPath.append(-1)

        # begin search w/ start node
        GraphSearch.dfs_visit(start, end, graph, vColors, vPath)

        # todo - handle visiting remaining disconnected
        # nodes

    # todo - could move the params to class level
    # but since we've got multiple DFS implementations
    # in this class, we'll just pass them around for now
    @staticmethod
    def dfs_visit(v, end, graph, vColors, vPath):
        # terminating condition
        if (v == end):
            # return the path from end to start
            pass

        # color vertice 'v' Gray
        vColors[v] = "g"

        # for each neighbor of 'v'
        for neighbor in graph[v]:
            # if neighbor not colored white, visit
            if (vColors[neighbor[0]] == "w"):
                # record path back from neighbor to 'v'
                vPath[neighbor] = v
                # recurse on neighbor
                dfs_visit(neighbor)

        # done visiting all neighbors of 'v'; color 'v' black
        vColors[v] = "b"
