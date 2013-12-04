class Graph(object):
    """Graph with vertice/edge data stored in an adjacency matrix."""
    def __init__(self, num_vertices):
        self._graph_data = [[-1 for i in range(num_vertices)] for j in range(num_vertices)]

    def get_num_vertices(self):
        return len(self._graph_data)

    def add_edge(self, nodeId1, nodeId2, weight):
        """Node id's map to indices in the adjaceny matrix of graph data."""
        # undirected graph so we add two entries for each edge
        self._graph_data[nodeId1][nodeId2] = weight
        self._graph_data[nodeId2][nodeId1] = weight

    def find_neighbors(self, node_id):
        result = []

        edge_data = self._graph_data[node_id]

        for edge_id in edge_data:
            if (edge_id > 0):
                result.append(edge_id)

        return result

    def get_weight(self, node_id1, node_id2):
        return self._graph_data[nodeId1][nodeId2]


class Dijkstra(object):
    """Solve shortest path problem using Digkstra's algorithm."""
    def __init__(self, graph):
        self._graph = graph

        # assign initial distances to all nodes
        self._dist_dict = dict()

        for i in range(self._graph.get_num_vertices()):
            # node id's map to indices
            # using None to represent the infinity value
            # traditionally used in the algorithm
            self._dist_dict[i] = None

        # mark all nodes unvisited
        self._unvisited_nodes = set()

        for i in range(self._graph.get_num_vertices()):
            # node id's map to indices
            self._unvisited_nodes.add(i)

        # create set of visited nodes
        self._visited_nodes = set()

    def _eval_neighbors(self, node_id):
        # calcualte distances and update them if less
        # than current distances to the neighbor
        neighbor_ids = self._graph.find_neighbors(node_id)

        for neighbor_id in neighbor_ids:
            tenative_distance = self._graph.get_weight(node_id, neighbor_id)
            current_distance = self._dist_dict[neighbor_id]

            if (tenative_distance < current_distance):
                self._dist_dict[neighbor_id] = tenative_distance

    def _get_smallest_unvisited_node(self):
        smallest_node_id = None

        for node_id in self._unvisited_nodes:
            if (self._dist_dict[node_id] is None):
                continue

            if (smallest_node_id is None):
                # setting our base value for comparison
                smallest_node_id = node_id
            else:
                if (self._dist_dict[node_id] < self._dist_dict[smallest_node_id]):
                    smallest_node_id = node_id

        return smallest_node_id

    def find_shortest_path(self, start_node_id, end_node_id):
        """Finds shortest path b/w two nodes. Assumes path exists.
        Returns a tuple with the path and cost."""
        result = (None, None)

        # set initial distance to zero for our start node
        self._dist_dict[start_node_id] = 0
        
        # set initial node as "current"
        current_node_id = start_node_id

        while (len(self._unvisited_nodes) > 0):
            # for the current node, evaluate all neighbors
            self._eval_neighbors(current_node_id)

            # mark the current node as visited
            self._visited_nodes.add(current_node_id)

            # if destination node marked visited, done
            if (current_node_id == end_node_id):
                # todo - calc path
                path = None
                shortest_path_value = self._dist_dict[end_node_id]
                result = (path, shortest_path_value)
                break

            # else, select the unvisited node w/ the smallest
            # tenative distance and make it current node; repeat
            smallest_univisited_node_id = self._get_smallest_unvisited_node()

            current_node_id = smallest_univisited_node_id

        return result
