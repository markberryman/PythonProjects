class DfsBasic(object):
    """Basic iterative depth-first search w/ no optimizations.
    Can revisit nodes that have already been visited
    as part of known non-solutions."""
    @staticmethod
    def search(graph, start, end):
        """Using depth-first search, attempt to find a path 
        from vertice w/ id "start" to vertice w/ id "end". 
        If a path is found, return the list of vertices to 
        visit. If path is not found, return None.
        Note - this implementation of DFS is inefficient
        as it revisits vertices on paths known not to
        result in a path to the end vertice."""
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
                # if not end, look at each edge from vertice 'v'
                foundNewEdgeToTraverse = False
                for e in graph[v]:
                    if (e[0] not in vPath):
                        # if not already in path, 
                        # add edge's target vertice to stack
                        vStack.append(e[0])
                        foundNewEdgeToTraverse = True

                if (foundNewEdgeToTraverse is False):
                    # all the edges we found for this vertice
                    # have already been covered
                    vPath.pop()
            else:
                # no edges to follow backtrack
                # remove last node from path
                vPath.pop()

        return vPath
