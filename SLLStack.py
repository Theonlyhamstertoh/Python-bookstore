from Interfaces import Stack
import numpy as np


class SLLStack(Stack):
    class Node:
        def __init__(self, x: object):
            self.next = None
            self.x = x

    def __init__(self):
        self.head = None
        self.tail = None
        self.n = 0


    def push(self, x: object):
        newNode = self.Node(x)
        newNode.next = self.head
        self.head = newNode;
        
        if self.n == 0:
            self.tail = self.head
        self.n = self.n+ 1
            
        

    def pop(self) -> object:
        if self.n == 0:
            self.head = self.tail = None
            self.n = 0
            
            raise IndexError('The stack is empty; there is nothing to remove')
        
        removedNode = self.head
        if self.n == 1:
            self.head = None;
            self.tail = None;
            self.n = 0;
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
