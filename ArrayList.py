import numpy as np
from Interfaces import List
 
class ArrayList(List):
    '''
        ArrayList: Implementation of a List interface using Arrays. 
    '''
 
    def __init__(self):
        '''
        __init__: Initialize the state (array, n and j). 
        '''
        self.n = 0
        self.j = 0
        self.a = self.new_array(1)
 
    def new_array(self, n: int) -> np.array:
        '''
        new_array: Create a new array of size n
        Input:
            n: the size of the new array
        Return:
            An array of size n
        '''
        return np.zeros(n, object)
 
    def resize(self):
        '''
        resize: Create a new array and copy the old values. 
        '''
        newArray = None
        if len(self.a) > 3*self.n:
          newArray = self.new_array(int(len(self.a) /2))
        else:
          newArray = self.new_array(len(self.a) * 2)
        for k in range(self.n):
            newArray[k] = self.a[(self.j + k) % len(self.a)]
        
        print(newArray, "new array")
        self.j = 0
        self.a = newArray
        # self.a = np.concatenate(((self.a, self.new_array(len(self.a)))))
 
    def get(self, i: int) -> object:
        '''
        get: returns the element at position i
        Inputs:
            i: Index that is integer non negative and at most n
        '''
        if i < 0 or i >= self.n:
            raise Exception
        return self.a[(self.j + i) % len(self.a)]
 
 
    def set(self, i: int, x: object) -> object:
        '''
        set: Set the value x at the index i.
        Inputs:
            i: Index that is integer non negative and at most n
            x: Object type, i.e., any object 
        '''
        if i < 0 or i >= len(self.a): 
            raise Exception("Sorry, no numbers below zero or above n")
        else:
            self.a[(self.j + i) % len(self.a)] = x
            if self.n == 0: self.j = i
            self.n = self.n + 1
            return x
 
    def append(self, x: object):
        self.add(self.n, x)
 
    def add(self, i: int, x: object):
        '''
            add: shift one position all the items j>=i, insert an element 
            at position i of the list and increment the number of elements 
            in the list
            Inputs:
                i: Index that is integer non negative and at most n
                x: Object type, i.e., any object
        '''
        if i < 0 or i > len(self.a) : raise Exception 
        if len(self.a) == self.n : self.resize()
        # i = 2, 2.5
        if self.a[(self.j + i) % len(self.a)] == 0:
            self.a[(self.j + i) % len(self.a)] = x
 
        elif i < self.n / 2:
          # print('--------<<<<------------')
          #  if add at i=3, shift only units before down
          # 
          for k in range(0, i):
            currentIndex = (self.j + k) % len(self.a)
            prevIndex = (self.j + k - 1) % len(self.a)
            # print("j =", self.j)
            # print("n =", self.n)
            # print("i =",i )
            # print("current Index:", currentIndex, self.a[currentIndex])
            # print("Prev Index:", prevIndex, self.a[prevIndex])
 
            self.a[prevIndex] = self.a[currentIndex]
            # print("result", self.a)
            # print('-------------------- ')
          self.j = self.j - 1
          if self.j == -1: self.j = len(self.a ) - 1 
          indexToPut = (self.j + i ) % len(self.a)
          self.a[indexToPut] = x
                
 
        elif i >= self.n/2: 
 
            for k in range(self.n - 1, i -1 ,-1 ):
                currentIndex = (self.j + k) % len(self.a)
                nextIndex = (self.j + k + 1) % len(self.a)
                prevIndex = (self.j + k - 1) % len(self.a)
 
                self.a[nextIndex] = self.a[currentIndex]
                # print("result", self.a)
                # print('-------------------- ')
            indexToPut = (self.j + i) % len(self.a)
            self.a[indexToPut] = x
        self.n = self.n + 1
 
        # self.a = np.insert(self.a, i, x)
        
 
    def remove(self, i: int) -> object:
        if self.n <= 0:
            raise IndexError("no more elements in array")
        toRemoveIndex = (self.j + i) % len(self.a)
        x = self.a[toRemoveIndex]
        if i < self.n/2:
          print("remove index", toRemoveIndex, self.a[toRemoveIndex])
          for k in range(self.j + i , self.j, -1 ):
            print('ran k=', k)
            currentIndex = (self.j + k) % len(self.a)
            prevIndex = (self.j + k - 1) % len(self.a)
            print("current:", self.a[currentIndex], currentIndex, "prev", self.a[prevIndex], prevIndex)
            self.a[currentIndex] = self.a[prevIndex]
            # self.a[currentIndex] = 0

 
          self.j = self.j + 1
          # if self.j == -1: self.j = len(self.a ) - 1 
 
        elif i >= self.n/2:
          for k in range(i, self.n):
            currentIndex = (self.j + k) % len(self.a)
            nextIndex = (self.j + k + 1) % len(self.a)
            self.a[currentIndex] = self.a[nextIndex]
        self.n = self.n - 1
        if len(self.a) > 3* self.n:
          self.resize()
        
        return x
        # if i < self.n / 2:
        #     for k in range(self.n):
        #         self.a[(self.j + k) % len(self.a)] = self.a[(self.j + k + 1) % len(self.a)]
        #         self.j = self.j -1
        # elif i >= self.n / 2:
        #     for k in range(self.n):
        #         self.a[(self.j + k) % len(self.a)] = self.a[(self.j + k - 1) % len(self.a)]
        #         self.j = self.j +1
 
        # if len(self.a) > 3 * self.n:
        #     self.resize()
        
 
    def size(self) -> int:
        return self.n
 
    def __str__(self):
        s = "["
        for i in range(0, self.n):
            s += "%r" % self.a[(i + self.j) % len(self.a)]
            if i < self.n - 1:
                s += ","
        return s + "]"
 
    def __iter__(self):
        self.iterator = 0
        return self
 
    def __next__(self):
        if self.iterator < self.n:
            x = self.a[(self.iterator + self.j) % len(self.a)]
            self.iterator += 1
        else:
            raise StopIteration()
        return x
 
# a = np.zeros(3, object)
 
array = ArrayList()
array.a = array.new_array(6)
# array.set(0, "A")
# array.set(1, "B")
# array.set(2, "C")
# array.set(3, "d")
# array.set(4, "e")
# array.set(5, "f")
# array.set(6, "g")
# array.set(7, "h")
# array.j = 4
# print(array.a)
# print(array.remove(0))
# print(array.a)

array.j = 2
array.add(0, "a")
array.add(1, "b")
array.add(2, "c")
array.add(3, "d")
array.add(2, "e")
array.add(2, "f")
array.add(0, "A")
array.remove(5)
array.remove(2)
print(array.a)

# print(array.a, "(set) j:"+ str(array.j))
# array.add(3, "D")
# print(array.a)
# array.add(2, "E")
# print(array.a)
# array.add(2, "F")
# print(array.a)
# array.add(0, "A")
# print(array.a, array.j)
# array.remove(5)
# print(array.a)
# array.remove(2)
# print(array.a)
# array.remove(1)
# print(array.a)
# print(array.remove(3))
# print(array.a)
# print(array.add(3, "A"))
# print(array.get(2))
# array.add(0,66)
# print(array.a, array.j, array.n)
# array.add(1,66)
# array.add(1,66)?
# print(array.a, array.j, array.n)
# myArray = ArrayList()
# myArray.a = myArray.new_array(5)
# myArray.append(66)
# myArray.remove(0)
# myArray.get(4)
# myArray.resize()
# myArray.set(2, 77)
# print(myArray.a)
# print(a)
# a= np.insert(a, 0,(1, 2, 3))
# # a = np.insert(a, 5,2)
# # print(np.concatenate((a[:2], [12], a[2:])))
 
# print(np.delete(a, 1))
# print(np.concatenate((a, np.zeros(len(a), object))))
# print(np.concatenate((a[:2], [66], a[2:])))
# print(np.flatnonzero(a == 2)[0])
 
 