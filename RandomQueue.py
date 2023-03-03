import numpy as np
import random
from ArrayQueue import ArrayQueue


class RandomQueue(ArrayQueue):
    def __init__(self):
        ArrayQueue.__init__(self)


    def remove(self) -> object:
        '''
            remove a random element
            You can call the method of the parent class using super(). e.g.
            super().remove()
        '''

        if self.n <= 0: 
            raise IndexError()
        # if self.n < 2: self.resize()
        randomIndex = random.randint(0, self.n - 1)
        head = self.a[self.j % len(self.a)]
        randomEl = self.a[(self.j + randomIndex) % len(self.a)]
        print("element", head, randomEl)
        self.a[self.j % len(self.a)] = randomEl
        self.a[(self.j + randomIndex)% len(self.a)] = head
        return super().remove()


# array = RandomQueue()
# # array.a = array.new_array(4)
# array.add(2)
# # array.add(1)
# # array.add(4)
# # array.add(6)
# print(array.n)
# print(array.remove())
# print(array.remove())
# # print(array.remove())
# # print(array.remove())
# print(array)