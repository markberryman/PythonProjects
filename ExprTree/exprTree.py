# todo - make subclasses of Node w/ one representing
# an operator and one representing an operand
# add the calc logic into operand type of nodes
class Node(object):
    def __init__(self, value):
        self.__value = value
        self.__lChild = None
        self.__rChild = None

    @property
    def value(self):
        return self.__value

    @property
    def lChild(self):
        return self.__lChild

    @lChild.setter
    def lChild(self, node):
        self.__lChild = node

    @property
    def rChild(self):
        return self.__rChild

    @rChild.setter
    def rChild(self, node):
        self.__rChild = node


class ExprTree(object):
    def apply_operand(self, operand, v1, v2):
        # todo - handle other operators
        if (operand == "+"):
            return v1 + v2

    def calc(self, node):
        # terminating condition, node is not an operator
        if (isinstance(node.value, int)):
            return node.value

        # calc left, calc right, apply operand
        lValue = self.calc(node.lChild)
        rValue = self.calc(node.rChild)

        return self.apply_operand(node.value, lValue, rValue)