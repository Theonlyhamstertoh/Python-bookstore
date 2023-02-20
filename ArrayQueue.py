import numpy as np
from Interfaces import Queue


class ArrayQueue(Queue):
    def __init__(self):
        self.n = 0
        self.j = 0
        self.a = self.new_array(1)

    def new_array(self, n: int) -> np.array:
        return np.zeros(n, object)

    def resize(self):
        '''
            Resize the array
        '''
        newArray = None
        if len(self.a) >= 3*self.n:
            newArray = self.new_array(
                max(int(len(self.a) /2), 1))
        else:
            newArray = self.new_array(max(1, len(self.a) * 2))
        for k in range(self.n):
            newArray[k] = self.a[(self.j + k) % len(self.a)]
        self.a = newArray
        
        self.j = 0

    def add(self, x: object):
        '''
            shift all j > i one position to the right
            and add element x in position i
        '''
        if len(self.a) == self.n:
            print('yes')
            self.resize()
        self.a[(self.j + self.n) % len(self.a)] = x
        self.n = self.n + 1
        print('n = ', self.n, self.a)


    def remove(self) -> object:
        '''
            remove the first element in the queue
        '''
        if self.n <= 0:
            raise IndexError("no more n")
        if len(self.a) > 3 * self.n:
            self.resize()
        x = self.a[self.j]
        
        self.a[(self.j) % len(self.a)] = 0

        print(len(self.a), self.n)
        self.n = self.n - 1
        
        print('n = ', self.n, self.a)

        self.j = self.j + 1
        return x

    def size(self):
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
            x = self.a[self.iterator]
            self.iterator += 1
        else:
            raise StopIteration()
        return x

array = ArrayQueue()
array.a = array.new_array(6)
array.j = 2
array.add("a")
array.add("b")
array.add("c")
array.add("e")
array.add("d")
array.add("f")
array.add("x")
array.remove()
array.remove()
array.remove()
array.remove()
array.resize()
print(array.a)