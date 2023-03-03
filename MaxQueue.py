from SLLQueue import SLLQueue
from DLLDeque import DLLDeque


class MaxQueue(SLLQueue):
    def __init__(self):
        super().__init__()
        # self.queue = SLLQueue()
        self.max_deque = DLLDeque()  # NOTE: DLLDeque implements the Deque interface but also inherits all methods from DLList 

    def add(self, x : object):
      """
      adds an element to the end of this max queue
      INPUT: x the element to add
      """
      super().add(x)
      
      front = self.max_deque.dummy.next
      if self.max_deque.n == 0:
        self.max_deque.add_first(x)
        print("I AM RAN")
      elif front.x < x:
        self.max_deque.removeAll()
        self.max_deque.add_first(x)
      elif front.x > x:
        for i in range(self.max_deque.n -1, 0, -1):
          prevValue =self.max_deque.get(self.max_deque.n - 1) 
          if x > prevValue:
            print(x, ">", prevValue)
            self.max_deque.remove_last()
        self.max_deque.add_last(x)
      # self.queue.add(x)
      # print(super().add)
      # self.max_deque.add()

    def remove(self) -> object:
      """
      removes and returns the element at the head of the max queue
      """
      removedValue = super().remove()
      print("remove value", removedValue)
      for i in range (self.max_deque.n):
        if removedValue == self.max_deque.get(i):
          print(i, self.max_deque.get(i))
          self.max_deque.remove(i)
      return removedValue

    def max(self):
      """
      returns the maximum element stored in the queue
      """
      return self.max_deque.get(0)




# # TESTER
# mq = MaxQueue()
# mq.add(3)
# print("Added:", 3)
# print("MaxQueue contents:", mq)
# print("Max Dequeu contents", mq.max_deque)
# print("Max element", mq.max(), "\n\n")

# mq.add(2)
# print("Added:", 2)
# print("MaxQueue contents:", mq)
# print("Max Dequeu contents", mq.max_deque)
# print("Max element", mq.max(), "\n\n")

# mq.add(1)
# print("Added:", 1)
# print("MaxQueue contents:", mq)
# print("Max Dequeu contents", mq.max_deque)
# print("Max element", mq.max(), "\n\n")

# mq.add(4)
# print("Added:", 4)
# print("MaxQueue contents:", mq)
# print("Max Dequeu contents", mq.max_deque)
# print("Max element", mq.max(), "\n\n")

# r = mq.remove()
# print("Removed element:", r)
# print("MaxQueue contents:", mq)
# print("Max Dequeu contents", mq.max_deque)
# print("Max element", mq.max(), "\n\n")

# r = mq.remove()
# print("Removed element:", r)
# print("MaxQueue contents:", mq)
# print("Max Dequeu contents", mq.max_deque)
# print("Max element", mq.max(), "\n\n")

# r = mq.remove()
# print("Removed element:", r)
# print("MaxQueue contents:", mq)
# print("Max Dequeu contents", mq.max_deque)
# print("Max element", mq.max(), "\n\n")

# mq.add(8)
# print("Added:", 8)
# print("MaxQueue contents:", mq)
# print("Max Dequeu contents", mq.max_deque)
# print("Max element", mq.max(), "\n\n")

# mq.add(3)
# print("Added:", 3)
# print("MaxQueue contents:", mq)
# print("Max Dequeu contents", mq.max_deque)
# print("Max element", mq.max(), "\n\n")

# mq.add(5)
# print("Added:", 5)
# print("MaxQueue contents:", mq)
# print("Max Dequeu contents", mq.max_deque)
# print("Max element", mq.max(), "\n\n")

# mq.add(4)
# print("Added:", 4)
# print("MaxQueue contents:", mq)
# print("Max Dequeu contents", mq.max_deque)
# print("Max element", mq.max(), "\n\n")

# mq.add(1)
# print("Added:", 1)
# print("MaxQueue contents:", mq)
# print("Max Dequeu contents", mq.max_deque)
# print("Max element", mq.max(), "\n\n")

# mq.add(6)
# print("Added:", 6)
# print("MaxQueue contents:", mq)
# print("Max Dequeu contents", mq.max_deque)
# print("Max element", mq.max(), "\n\n")


# while mq.size() > 0:
#     r = mq.remove()
#     print("Removed element:", r)
#     print("MaxQueue contents:", mq)
#     print("Max Dequeu contents", mq.max_deque)
#     if mq.size() > 0:
#         print("Max element", mq.max(), "\n\n")
        