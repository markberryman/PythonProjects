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

    def add_edge(self, id1, id2, w):
        """Add an edge between nodes w/ given id's and weight "w"."""
        if ((id1 not in self.__graph) or
            (id2 not in self.__graph)):
            raise ValueError("Can't add edge for non-existant node.")

        # undirected graph so add two edges
        self.__graph[id1].append([id2, w])
        self.__graph[id2].append([id1, w])
