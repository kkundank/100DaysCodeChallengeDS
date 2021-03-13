"""
Program to implement a single Linked List
"""


def main():
    s1 = SingleLinkedList()
    s1.insertDataBeginning(3)
    s1.insertDataBeginning(5)
    s1.insertDataLast(6)
    s1.print()


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SingleLinkedList:
    def __init__(self):
        self.head = None

    def insertDataBeginning(self, new_data):
        n1 = Node(new_data)
        n1.next = self.head
        self.head = n1

    def insertDataLast(self, new_data):
        n1 = Node(new_data)
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = n1

    def print(self):
        itr = self.head
        while itr is not None:
            print(itr.data)
            itr = itr.next


if __name__ == '__main__':
    main()
