class Node(object):
    """Node with just a left and right child pointer. No parent pointer."""
    def __init__(self, data=0):
        self.data = data
        self.lchild = None
        self.rchild = None


class BST(object):
    """
    Binary search tree.
    """

    def __init__(self):
        self.root = None
        self.curCount = 0

    def inorder_traversal(self, node, result):
        """Traverse left node, current, then right."""
        if (node is None):
            return

        self.inorder_traversal(node.lchild, result)
        result.append(node.data)
        self.inorder_traversal(node.rchild, result)

    def preorder_traversal(self, node, result):
        """Traverse current node, then left, then right."""
        if (node is None):
            return

        result.append(node.data)
        self.preorder_traversal(node.lchild, result)
        self.preorder_traversal(node.rchild, result)

    def print_tree(self):
        result = self.inorder_traversal(self.root, [])
        print(result)

    def select(self, node, idx):
        if ((idx >= 1) and (self.root is not None)):
            if (node.lchild is not None):
                result = self.select(node.lchild, idx)

                if (result is not None):
                    return result

            self.curCount += 1

            if (self.curCount == idx):
                return node

            if (node.rchild is not None):
                result = self.select(node.rchild, idx)

                if (result is not None):
                    return result
        else:
            return None

    def insert(self, node):
        if (self.root is not None):
            curNode = self.root

            while (curNode is not None):
                if (node.data < curNode.data):
                    if (curNode.lchild is None):
                        curNode.lchild = node
                        break
                    else:
                        curNode = curNode.lchild
                else:
                    if (curNode.rchild is None):
                        curNode.rchild = node
                        break
                    else:
                        curNode = curNode.rchild
        else:
            self.root = node
