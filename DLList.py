from Interfaces import List
import numpy as np


class DLList(List):
    class Node:
        def __init__(self, x: object):
            self.next = None
            self.prev = None
            self.x = x

    def __init__(self):
        self.dummy = DLList.Node("")
        self.dummy.next = self.dummy
        self.dummy.prev = self.dummy
        self.n = 0

    def get_node(self, i: int) -> Node:
        # todo
        if i < 0 or i > self.n :
            raise IndexError('out of range')
        p = None;
        if i < self.n / 2:
            p = self.dummy.next # stats at the head since dummy is between the last and the first
            for j in range(i):
                p = p.next
        else:
            p = self.dummy
            for j in range(self.n, i, -1):
                p = p.prev

        return p;
    def get(self, i) -> object:
        if i < 0 or i >= self.n :
            raise IndexError('out of range')
        return self.get_node(i).x

    def set(self, i: int, x: object) -> object:
        if i < 0 or i >= self.n :
            raise IndexError('out of range')
        node = self.get_node(i)
        old_x = node.x
        node.x = x   
        return old_x

    def add_before(self, w: Node, x: object) -> Node:
        #  create a new node
        newNode = DLList.Node(x)
        
        # get prevNode
        prevNode = w.prev
        # connect the prev node to new node. prev.next -> new   new.prev -> prev
        prevNode.next = newNode
        newNode.prev = prevNode
        
        #  repeat process for node in front of new
        newNode.next = w
        w.prev = newNode
        
        #  increment count
        self.n = self.n + 1
        return newNode

    def add(self, i: int, x: object):
        if i < 0 or i > self.n:
            raise IndexError('out of range')
        node = self.get_node(i)
        self.add_before(node, x)
        
    def reverse(self):
        front = self.dummy.next
        back = self.dummy.prev
        
        for k in range(int(self.n / 2 )):
            swap_holder = front.x
            front.x = back.x
            back.x = swap_holder
            
            front = front.next
            back = back.prev

    def _remove(self, w: Node):
        # w is the node we want to remove
        w.prev.next = w.next
        w.next.prev = w.prev
        
        

    def remove(self, i: int):
        if i < 0 or i >= self.n:  raise IndexError()
        removeNode = self.get_node(i)
        self._remove(removeNode)
        
        if self.n == 1:
            self.dummy.next = self.dummy
            self.dummy.prev = self.dummy
        self.n = self.n- 1
        return removeNode.x
    
    def removeAll(self):
        for i in range(self.n):
            self.remove(0)

    def size(self) -> int:
        return self.n

    def append(self, x: object):
        self.add(self.n, x)

    def isPalindrome(self) -> bool:
        front = self.dummy.next
        back = self.dummy.prev
        if self.size == 0:
            return False
        for k in range( int(self.n / 2)):
            print(k)
            if  front.x != back.x:
                
                return False
            front = front.next
            back = back.prev
        return True
        
        

    def __str__(self):
        s = "["
        u = self.dummy.next
        while u is not self.dummy:
            s += "%r" % u.x
            u = u.next
            if u is not None:
                s += ","
        return s + "]"

    def __iter__(self):
        self.iterator = self.dummy.next
        return self

    def __next__(self):
        if self.iterator != self.dummy:
            x = self.iterator.x
            self.iterator = self.iterator.next
        else:
            raise StopIteration()
        return x


list = DLList()
# list.add(0, 'a')
# list.add(0, 'a')
# list.add(0, 'a')
# list.add(0, 'b')
# list.add(1, 'a')
# print(list.isPalindrome())
list.add(0, 4)
list.add(0, 1)
list.add(1, 3)
list.add(1, 2)
list.add(4, 5)
# list.reverse()
# # list.remove(4)
# list.remove(4)
list.removeAll()
