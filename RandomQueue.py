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
        randomIndex = random.randint(0, self.n)
        tail = self.a[self.n - 1]
        self.a[self.n -1] = self.a[randomIndex]
        self.a[randomIndex] = tail 
        super().remove()



array = RandomQueue()
array.a = array.new_array(4)
array.add(2)
array.add(1)
array.add(4)
array.add(6)
print(array)
array.remove()
print(array)