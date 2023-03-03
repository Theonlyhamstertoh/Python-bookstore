from Interfaces import Deque
class SLLDeque(Deque):
  class Node:
    def __init__(self, data: object):
      self.x = x
      self.next = None
  def __init__(self):
    self.head = None
    self.tail = None
    self.n = 0
    return
  def add_first(self, x: object):
    newNode = self.Node(x)
    newNode.next = self.head
    self.head = newNode
    if self.n ==0:
      self.tail = newNode
    self.n = self.n + 1
    return
