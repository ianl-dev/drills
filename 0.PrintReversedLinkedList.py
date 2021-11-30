"""
Stack is Last-In, First out
In English: did you just go in, get out from my house!

Problem:
How can we print a linked list (stack) from end to beginning? Given the very beginning of the stack
"""
def printReverseStack(head):
    # Try adding elements from linked list to the stack
    nodes = []
    start = head
    while start is not None:
        nodes.append(start.data)
        start = start.next
    
    # Now print node value in reverse
    while nodes:
        print(nodes.pop()) # Pop without argument always pop the last element

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

a = Node(1, Node(2, Node(3, Node(4, None))))
printReverseStack(a)