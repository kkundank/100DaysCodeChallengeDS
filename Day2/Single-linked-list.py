"""
Single Linked List implementation.
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SLL:
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

    def insertAtLast(self, new_data):
        itr = self.head
        n2 = Node(new_data)
        while itr.next is not None:
            itr = itr.next
        itr.next = n2


s1 = SLL()
s1.insertAtBeginning(3)
s1.insertAtBeginning(4)
s1.insertAtLast(6)
s1.print()
