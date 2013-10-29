class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

class LList(object):
    @staticmethod
    def merge_two_sorted_lists(l1, l2):
        # exc handling
        if (l1 is None):
            return l2
        
        if (l2 is None):
            return l1

        head = None
        tail = None

        if (l1.data < l2.data):
            head = l1
            l1 = l1.next
        else:
            head = l2
            l2 = l2.next

        tail = head

        while ((l1 is not None) and
               (l2 is not None)):
            if (l1.data < l2.data):
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next

            tail = tail.next

        # append trailing list
        if (l1 is None):
            tail.next = l2
        else:
            tail.next = l1

        return head


# list 1
n0 = Node(0)
n1 = Node(4)
n2 = Node(5)
n3 = Node(10)
n0.next = n1
n1.next = n2
n2.next = n3

# list 2
n4 = Node(2)
n5 = Node(3)
n6 = Node(7)
n4.next = n5
n5.next = n6

answer = LList.merge_two_sorted_lists(n0, n4)

while (answer is not None):
    print(answer.data)
    answer = answer.next

input("Enter to exit...")
