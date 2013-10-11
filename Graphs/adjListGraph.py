class GraphSearch(object):
    @staticmethod
    def dfs(graph, start, end):
        """Using depth-first search, attempt to find a path 
        from vertice w/ id "start" to vertice w/ id "end". 
        If a path is found, return the list of vertices to 
        visit. If path is not found, return None."""
        vStack = []
        vPath = []      # path to solution

        # add start node to stack
        vStack.append(start)

        while (len(vStack) > 0):
            # pop node from stack
            v = vStack.pop()
                
            # add node to path followed
            # no need to check at this point if the vertice
            # was already followed as we wouldn't have this
            # case since we never add the edge to this vertice
            # if it's already in the path
            vPath.append(v)

            # check for end
            if (v == end):
                return vPath
            
            if (len(graph[v]) > 0):
                # if not end, look at each edge from 'n'
                for e in graph[v]:
                    if (e[0] not in vPath):
                        # if not already in path, 
                        # add edge's target vertice to stack
                        vStack.append(e[0])
            else:
                # no edges to follow backtrack
                # remove last node from path
                vPath.pop()

        return vPath


class AdjListGraph(object):
    """Undirected graph structure stored in the adjacency list form.
    Using a dictionary for the data structure so we have
    fast lookup of nodes. The value of each element
    in the dictionary will be a list of the node's edges."""
    def __init__(self):
        self.__graph = dict()

    @property
    def graph(self):
        return self.__graph

    def add_node(self, id):
        """Add a vertice with the given id."""
        if (id not in self.__graph):
            self.__graph[id] = []
        else:
            raise ValueError("Can't add duplicate node.")

    def _is_dupe_edge(self, id1, id2):
        # assuming our adding of undirected edges is 
        # correct such that we get two edges for each
        # edge added
        for edge in self.__graph[id1]:
            if (edge[0] == id2):
                return True

        return False

    def add_edge(self, id1, id2, w):
        """Add an edge between nodes w/ given id's and weight "w"."""
        if ((id1 not in self.__graph) or
            (id2 not in self.__graph)):
            raise ValueError("Can't add edge for non-existant node.")

        if (self._is_dupe_edge(id1, id2)):
            raise ValueError("Can't add duplicate edge.")

        # undirected graph so add two edges
        self.__graph[id1].append([id2, w])
        self.__graph[id2].append([id1, w])
