"""
Implementing Double Linked List.
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DLL:
    def __init__(self):
        self.head = None

    def print(self):
        itr = self.head
        while itr is not None:
            print(itr.data)
            itr = itr.next

    def insertAtBeginning(self, new_data):
        n1 = Node(new_data)
        n1.next = self.head
        self.head = n1

    def insertAtEnd(self, new_data):
        n2 = Node(new_data)
        itr = self.head
        while itr.next is not None:
            itr = itr.next
        itr.next = n2
        n2.prev = itr


d1 = DLL()
d1.insertAtBeginning(5)
d1.insertAtBeginning(6)
d1.insertAtBeginning(7)
d1.insertAtEnd(10)
d1.print()
