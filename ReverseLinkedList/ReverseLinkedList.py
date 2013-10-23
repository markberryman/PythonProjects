class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

class LList(object):
    @staticmethod
    def reverse(node):
        if (node is None):
            return node

        head = node
        node = node.next
        head.next = None

        while (node is not None):
            temp = node.next
            node.next = head
            head = node
            node = temp

        return head

n1 = Node(4)
n2 = Node(5)
n3 = Node(10)
n1.next = n2
n2.next = n3

answer = LList.reverse(n1)

while (answer is not None):
    print(answer.data)
    answer = answer.next

input("Enter to exit...")
