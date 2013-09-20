class Node(object):
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

    def get_smallest_node(self):
        result = None

        if (self.root is not None):
            curNode = self.root

            while (curNode.lchild is not None):
                curNode = curNode.lchild

            result = curNode

        return result
        
    def get_next_node(self, node):
        """
        Gets the next node (in-order) based on the node provided.
        """
        result = None

        if (self.root is not None):
            if ((self.root.lchild is None) and
                (self.root.rchild is None)):
                # single node tree
                result = self.root
            else:
                curNode = self.root
                lastNode = curNode

                # traverse the tree tracking the last node
                # which will be the "next" node
                while ((curNode is not None) and
                       (curNode.data != node.data)):
                    if (node.data < curNode.data):
                        lastNode = curNode
                        curNode = curNode.lchild
                    else:
                        lastNode = curNode
                        curNode = curNode.rchild

                if (curNode is None):
                    # didn't find the node requested so we
                    # can't provide the "next" node
                    result = None
                else:
                    result = lastNode
                
        return result

    def select(self, index):
        """
        Takes a 1-based index, and returns the element at that index,
        or None if the index is out-of-bounds.
        """
        result = None

        # find the starting node; that would be the smallest node in the tree
        startNode = self.get_smallest_node()

        # traverse in-order (index - 1) nodes
        while (index > 1):
            # step through the tree in ordered fashing (index - 1) times

            index -= 1
            pass

        return result
