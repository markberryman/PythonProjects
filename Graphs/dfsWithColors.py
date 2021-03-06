class DfsWithColors(object):
    """Depth-first search of a graph using colors for
    optimization."""
    def __init__(self, graph):
        self.__graph = graph
        self.__vColors = []
        self.__vPath = []   # vertice paths

    @property
    def vColors(self):
        return self.__vColors

    @property
    def vPath(self):
        return self.__vPath

    @staticmethod
    def find_path(vPath, start, end):
        """Taking the data returned by the dfs that uses
        coloring, see if there exists a path b/w the
        start and end vertices."""
        result = []
        v = end

        while (vPath[v] != - 1):
            result.append(v)
            v = vPath[v]

        # could have gotten back to the start
        # or maybe there was no path
        if (v == start):
            result.append(v)
        else:
            # no path
            result = []

        result.reverse()

        return result

    def dfs(self, start):
        """Using depth-first search, builds entire picture
        of graph using a coloring algorithm for optimization.
        Resulting calculated data can be used to check for a
        path (not necessarily shortest) b/w any two vertices."""
        # coloring each node white and 
        # initializing path data
        for x in range(self.__graph.get_num_vertices()):
            self.__vColors.append("w")
            self.__vPath.append(-1)

        # begin search w/ start node
        self.dfs_visit(start)

        # todo - handle visiting remaining disconnected
        # nodes

    def dfs_visit(self, v):
        # color vertice 'v' Gray
        self.__vColors[v] = "g"

        # for each neighbor of 'v'
        for neighbor in self.__graph.get_vertice_neighbors(v):
            # if neighbor not colored white, visit
            if (self.__vColors[neighbor] == "w"):
                # record path back from neighbor to 'v'
                self.__vPath[neighbor] = v
                # recurse on neighbor
                self.dfs_visit(neighbor)

        # done visiting all neighbors of 'v'; color 'v' black
        self.__vColors[v] = "b"
