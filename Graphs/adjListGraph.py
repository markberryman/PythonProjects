class Edge(object):
    def __init__(self, id1, id2, w):
        """Id's of the two nodes for the edge and a weight w."""
        # todo - feeling too lazy to define properties...
        self.id1 = id1
        self.id2 = id2
        self.w = w


class Node(object):
    def __init__(self, id):
        self.__id = id

    @property
    def id(self):
        return self.__id


class AdjListGraph(object):
    """Graph structure stored in the adjacency list form.
    Using a dictionary for the data structure so we have
    fast lookup of nodes. The value of each element
    in the dictionary will be a list of the node's edges."""
    def __init__(self):
        self.__graph = dict()

    @property
    def graph(self):
        return self.__graph

    def add_node(self, node):
        if (node.id not in self.__graph):
            self.__graph[node.id] = []
        else:
            raise ValueError("Can't add duplicate node.")

    def add_edge(self, edge):
        if ((edge.id1 not in self.__graph) or
            (edge.id2 not in self.__graph)):
            raise ValueError("Can't add edge for non-existant node.")
