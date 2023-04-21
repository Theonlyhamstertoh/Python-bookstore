import numpy as np
import math
from Interfaces import Queue
from Interfaces import Tree
import BinaryTree

def left(i: int) -> int:
    """
    helper method; returns the index of the left child of the element at index i
    """
    return 2 * i + 1


def right(i: int) -> int:
    """
    helper method; returns the index of the right child of the element at index i
    """
    # todo
    return 2 * (i + 1)


def parent(i: int) -> int:
    """
    helper method; returns the index of the parent of the element at index i
    """
    return (i - 1) // 2
    pass

def _new_array(n: int) -> np.array:
    """
    helper method; creates a new numpy array of 0's of size n
    """
    return np.zeros(n, object)

class BinaryHeap(Queue, Tree):
    def __init__(self):
        self.a = _new_array(1)
        self.n = 0

    def add(self, x: object):
        # todo
        # fill row from left to right
        # child has to be greater than parent

        if len(self.a) == self.n:
            self._resize()
        
        self.a[self.n] =  x;
        self.n += 1
        self._bubble_up_last()
        return True;
    def add_node(self, k: object, x: object):
        # todo
        # fill row from left to right
        # child has to be greater than parent

        if len(self.a) == self.n:
            self._resize()
        
        self.a[self.n] =  BinaryTree.BinaryTree.Node(k, x);
        self.n += 1
        self._bubble_up_last_node()
        return True;

    def remove(self):
        if self.n == 0: raise IndexError("Can not remove from an empty heap.")
        root = self.a[0]
        self.a[0] = self.a[self.n - 1]
        self.a[self.n - 1] = 0
        self.n -= 1
        self._trickle_down_root(0)      
        # if 3 * self.n < len(self.a):
            # self._resize()
        return root;
    def remove_node(self):
        if self.n == 0: raise IndexError("Can not remove from an empty heap.")
        root = self.a[0]
        self.a[0] = self.a[self.n - 1]
        self.a[self.n - 1] = 0
        self.n -= 1
        self._trickle_down_root_node(0)      
        if 3 * self.n < len(self.a):
            self._resize()
        return root;
    def depth(self, u) -> int: 
        if u == None: return -1 
        index = None
        depth = 0;
        for i in range(self.n):
            if self.a[i] == u:
                index = i;
        
        while index != 0:
            print(index)
            depth += 1
            index = parent(index)
        return depth;


    def height(self) -> int:
        return math.floor(math.sqrt(self.n)) 

    def bf_order(self) -> list:
        nodes = []
        nodes.extend(self.a[0: self.n])
        return nodes;

    def in_order(self) -> list:
        indexes = self._in_order()
        nodes = []
        for x in indexes:
            nodes.append(self.a[x])
        return nodes;
            
    def _in_order(self, u = 0) -> list:
        indexes = []
        
        if left(u) < self.n :
            indexes.extend(self._in_order(left(u)))
        indexes.append(u)
        
        if right(u) < self.n :
            indexes.extend(self._in_order(right(u)))

        return indexes

    
    
            

    def post_order(self) -> list:
        indexes = self._post_order()
        nodes = []
        for x in indexes:
            nodes.append(self.a[x])
        return (nodes)
    def _post_order(self, u = 0) -> list:
        indexes = []
        if left(u) < self.n :
            indexes.extend(self._post_order(left(u)))
            # indexes.extend(self.in_order(left(u)))
        
        if right(u) < self.n :
            indexes.extend(self._post_order(right(u)))

            # indexes.extend(self.in_order(self.a[right(u)]))
        indexes.append(u)
        return indexes

    def pre_order(self) -> list:
        indexes = self._pre_order()
        nodes = []
        for x in indexes:
            nodes.append(self.a[x])
        return nodes;
    def _pre_order(self, u= 0) -> list:
        indexes = []
        
        indexes.append(u)
        if left(u) < self.n:
            indexes.extend(self._pre_order(left(u)))
        
        if right(u) < self.n :
            indexes.extend(self._pre_order(right(u)))
        return indexes

    def size(self) -> int:
        return self.n

    def find_min(self):
        if self.n == 0: raise IndexError()
        return self.a[0]

    def _bubble_up_last(self):
        # index of the last item in the tree
        index = self.n - 1;
        
        parent_index = parent(index)
        
        while index > 0 and self.a[index] < self.a[parent_index]:
            # if the child is less than the parent, swap them
            self.a[index], self.a[parent_index] = self.a[parent_index], self.a[index]
            index = parent_index;
            parent_index = parent(index)
    def _bubble_up_last_node(self):
        # index of the last item in the tree
        index = self.n - 1;
        
        parent_index = parent(index)
        
        while index > 0 and self.a[index].k < self.a[parent_index].k:
            # if the child is less than the parent, swap them
            self.a[index], self.a[parent_index] = self.a[parent_index], self.a[index]
            index = parent_index;
            parent_index = parent(index)
            

    def _resize(self):
        # todo
        if len(self.a) >= 3*self.n:
            newArray = _new_array(
                max(int(len(self.a) /2), 1))
        else:
            newArray = _new_array(max(1, len(self.a) * 2))
        for k in range(self.n):
            newArray[k] = self.a[k]
        self.a = newArray
        return True

    def _trickle_down_root(self, index):
        if self.n <= 1: 
            # print("EMPTY IN _TRICKLE_DOWN_ROOT()")
            return
        # print("IN _TRICKLE_DOWN_ROOT()", self)
        # index = 0
        left_index = left(index)
        right_index = right(index)
        smallest = index; 
        
        if left_index < self.n and (self.a[left_index] < self.a[index]):
            smallest = left_index
        
        if right_index < self.n and (self.a[right_index] < self.a[index]) and (self.a[right_index] < self.a[left_index]):
            smallest = right_index
        
        if smallest != index:
            self.a[index], self.a[smallest] = self.a[smallest], self.a[index]
            self._trickle_down_root(smallest)
            
    def _trickle_down_root_node(self, index):
        if self.n <= 1: 
            # print("EMPTY IN _TRICKLE_DOWN_ROOT()")
            return
        # print("IN _TRICKLE_DOWN_ROOT()", self)
        # index = 0
        left_index = left(index)
        right_index = right(index)
        smallest = index; 
        
        if left_index < self.n and (self.a[left_index].k < self.a[index].k):
            smallest = left_index
        
        if right_index < self.n and (self.a[right_index].k < self.a[index].k) and (self.a[right_index].k < self.a[left_index].k):
            smallest = right_index
        
        if smallest != index:
            self.a[index], self.a[smallest] = self.a[smallest], self.a[index]
            self._trickle_down_root_node(smallest)
            
            
        
        
 

    def __str__(self):
        return str(self.a[0:self.n])
    
    
# tree = BinaryHeap()
# for x in [5, 2, 1, 4, 3, ]:
#     tree.add(x)
    
# for x in range(tree.n):
#     print(tree.remove())
    
# print(tree.bf_order())
# tree.add(x) for every in 1 8 3 16 15 29 10 19 17 28 
# tree.add(1)
# tree.add(8)
# tree.add(3)
# tree.add(16)
# tree.add(15)
# tree.add(29)
# tree.add(10)
# tree.add(19)
# tree.add(17)
# tree.add(28)
# tree.add(5)
# print(tree.bf_order())
# print(tree.in_order())
# print(tree.post_order())
# print(tree.pre_order())
# tree.remove()
# tree.add(4)
# tree.add(1)
# tree.add(3)
# print(tree)
# print(tree.depth(29))
# print(tree.size())
# print(tree.height())