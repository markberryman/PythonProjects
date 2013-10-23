class Node(object):
    def __init__(self, data):
        self.data = data
        self.lChild = None
        self.rChild = None


class Tree(object):
    @staticmethod
    def bfs(node):
        """Breadth first traversal."""
        # use a FIFO queue approach
        result = []
        queue = []

        queue.append(node)

        while (len(queue) > 0):
            node = queue.pop(0)

            result.append(node.data)

            if (node.lChild is not None):
                queue.append(node.lChild)

            if (node.rChild is not None):
                queue.append(node.rChild)        

        return result

    @staticmethod
    def dfs(node):
        """Depth first traversal."""
        # use a stack approach
        result = []
        stack = []

        stack.append(node)

        while (len(stack) > 0):
            node = stack.pop()

            result.append(node.data)

            if (node.lChild is not None):
                stack.append(node.lChild)

            if (node.rChild is not None):
                stack.append(node.rChild)        

        return result
