from Interfaces import Queue
import numpy as np


class SLLQueue(Queue):
    class Node:
        def __init__(self, x: object):
            self.next = None
            self.x = x

    def __init__(self):
        self.head = None
        self.tail = None
        self.n = 0

    def add(self, x: object):
        newNode = self.Node(x)
        if self.n ==0:
            self.head = newNode
        else:
            self.tail.next = newNode
        self.tail = newNode
        self.n = self.n + 1
        return True

    def remove(self) -> object:
        
        
        if self.n == 0:
            self.tail = self.head = None
            raise IndexError('Queue is empty. There is nothing to be removed')
        removedNode = self.head
        if self.n == 1:
            self.tail = self.head = None
        elif self.n > 1:
            self.head = self.head.next
        self.n = self.n -1    
        return removedNode.x
    def size(self) -> int:
        return self.n

    def __str__(self):
        s = "["
        u = self.head
        while u is not None:
            s += "%r" % u.x
            u = u.next
            if u is not None:
                s += ","
        return s + "]"

    def __iter__(self):
        self.iterator = self.head
        return self

    def __next__(self):
        if self.iterator != None:
            x = self.iterator.x
            self.iterator = self.iterator.next
        else:
            raise StopIteration()
        return x

# list = SLLQueue()
# list.add(1)
# list.add(2)
# list.add(3)
# list.add(4)
# list.add(5)

# # list.remove()
# print(list)
# list.remove()
# print(list)
# list.remove()
# print(list)
# list.remove()
# print(list)
# list.remove()
# print(list)
# list.remove()
# print(list)
# list.remove()
# print(list)