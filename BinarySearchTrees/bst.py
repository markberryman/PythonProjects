class Node(object):
    def __init__(self, data):
        self.data = data
        self.lchild = None
        self.rchild = None


class BST(object):
    """
    Binary search tree.
    """

    def __init__(self):
        self.root = None

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

    def select(self, index):
        """
        Takes a 1-based index, and returns the element at that index,
        or None if the index is out-of-bounds.
        """
        return None
