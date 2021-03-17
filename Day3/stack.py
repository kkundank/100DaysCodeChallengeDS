"""
Implementation of Stack and all operations.

Using:
    1. List
"""

# Using List
list1 = []

list1.append('1st')
list1.append('2nd')
list1.append('3rd')

list1.pop()
print(list1)
list1.pop()
print(list1)

# Using collections.deque collection
from collections import deque

stack = deque('abcd')

stack.append('e')
stack.append('f')

print(stack)

stack.pop()
stack.pop()

print(stack)
