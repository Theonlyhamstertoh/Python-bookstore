from Interfaces import Set
from DLList import DLList
import numpy as np


class ChainedHashTable(Set):
    class Node:
        def __init__(self, key, value):
            self.key = key
            self.value = value

    def __init__(self, dtype=DLList):
        self.dtype = dtype
        self.d = 1
        self.t = self.alloc_table(2 ** self.d)
        self.z = 193759204821
        self.w = 31
        self.n = 0

    def alloc_table(self, n: int):
        t = np.zeros(n, dtype=object)
        for i in range(n):
            t[i] = self.dtype()
        return t

    def _hash(self, key: int) -> int:
        return self.z * hash(key) % (2 ** self.w) >> (self.w - self.d)

    def size(self) -> int:
        return self.n

    def find(self, key: object) -> object:
        bin = self._hash(key)
        
        for i in range(self.t[bin].size()):
            list = self.t[bin]
            if list.get(i).key == key:
                # print("FOUND KEY:")
                return list.get(i).value
        # todo

    def add(self, key: object, value: object):
        if self.find(key) != None: 
            # print("TERMINATING ADD FUNCTION. ALREADY EXISTS.", "key", key, "value:", value)
            return False;
        
        if self.n == len(self.t): 
            self.resize() 
            # print(key, value)
        bin = self._hash(key)
        item = self.Node(key, value)
        self.t[bin].add(0, item)
        self.n = self.n + 1
        return True

    def remove(self, key: int) -> object:
         # find the bin from hash
        if key == None: return None;
        bin = self._hash(key)
        
        list = self.t[bin]
        for i in range(list.size()):
            if list.get(i).key == key:
                list.remove(i)
                self.n = self.n - 1
                if len(self.t) > 3*self.size(): self.resize()
                return True 
        return None;
    
        pass;
    def resize(self):
        if self.n == len(self.t):
            self.d = self.d + 1
        else:
            self.d = self.d - 1
        newTable = self.alloc_table(2 ** self.d)
        for j in range(len(self.t)):
            for i in range(self.t[j].size()):
                bin = self._hash(self.t[j].get(i).key)
                newTable[bin].add(0, self.t[j].get(i))
        self.t = newTable

    def __str__(self):
        s = "["
        for i in range(len(self.t)):
            for j in range(len(self.t[i])):
                k = self.t[i][j]
                s += str(k.key)
                s += ":"
                s += str(k.value)
                s += ";"
        return s + "]"



# table = ChainedHashTable()
# table.add(23, "A")
# table.add(15, 'B')
# table.add(11, 'C')
# table.remove(23)
# table.remove(15)
# table.add(10, 'D')
# table.add(12, 'A')
# print(table)

# table.add( 12, 'F')
# table.add( 54, 'N')
# table.add( 58, 'U')
# table.add( 75, 'P')
# table.add( 22, 'B')
# table.add( 40, 'O')
# table.add( 35, 'N')
# table.add( 67, 'G')
# table.add( 53, 'E')
# table.add( 35, 'J')  
# table.add( 33, 'R')
# table.add( 38, 'G')

# print(table)
# (table.remove(12))
# print(table)
# print(table.find(12))
# print(table)
# print(table._hash(12))