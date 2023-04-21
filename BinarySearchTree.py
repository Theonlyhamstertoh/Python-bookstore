from BinaryTree import BinaryTree
from Interfaces import Set


class BinarySearchTree(BinaryTree, Set):

    def __init__(self):
        BinaryTree.__init__(self)
        self.n = 0

    def add(self, key: object, value: object = None) -> bool:
        """
        If the key does not exist in this BinarySearchTree,
        adds a new node with given key and value, in the correct position.
        Returns True if the key-value pair was added to the tree, False otherwise.
        """
        parent = self._find_last(key)
        return self._add_child(parent, BinaryTree.Node(key, value))

    def find(self, key: object) -> object:
        """
        returns the value corresponding to the given key if the key
        exists in the BinarySearchTree, None otherwise
        """
        node = self._find_eq(key)
        if node == None: return None
        return node.v

    
    def remove(self, key: object):
        """
        removes the node with given key if it exists in this BinarySearchTree.
        Returns the value corresponding to the removed key, if the key was in the tree.
        If given key does not exist in the tree, ValueError is raised.
        """
        u = self._find_eq(key)
        if u == None:
            raise ValueError("Key not found")
        value = u.v
        self._remove_node(u)
        return value;
        

    def _find_eq(self, key: object) -> BinaryTree.Node:
        """
        helper method; returns the node in this tree that contains the given key,
        None otherwise.
        """
        current = self.r
        while current != None:
            if key == current.k:
                return current
            elif key < current.k:
                current = current.left
            elif key > current.k:
                current = current.right
        return None;
    def _find_last(self, key: object) -> BinaryTree.Node:
        """
        helper method; returns the node in this tree that contains the given key, if it exists.
        Otherwise, returns the node that would have been the parent of the node
        with the given key, if it existed
        """
        parent = None;
        current = self.r;
        
        while current != None:
            parent = current;
            if key == current.k:
                return current;
            elif key < current.k:
                current = current.left;
            elif key > current.k:
                current = current.right
        return parent;
            
    def find_nearest_node(self, key:object):
        # node = self._find_eq(key)
        current = self.r
        smallest = None;
    
        # find the node that is equal to the key or smallest key greater han the key 
        while current is not None:
            if key.lower() == current.k.lower():
                return current
            elif key < current.k:
                smallest = current
                current = current.left
            elif key > current.k:
                current = current.right
        return smallest
        
    def _add_child(self, p: BinaryTree.Node, u: BinaryTree.Node) -> bool:
        """
        helper method; adds node u as the child of node p, assuming node p has at most 1 child
        """
        if p == None:
            self.r = u
        else:
            if u.k < p.k:
                p.left  = u;
            elif u.k > p.k:
                p.right = u;
            else:
                return False
            u.parent = p
        self.n += 1
        return True

    def _splice(self, u: BinaryTree.Node):
        """
        helper method; links the parent of given node u to the child
        of node u, assuming u has at most one child
        """
        child, root, parent = None, None, None
        # todo
        
        if u.left:
            child = u.left
        else:
            child = u.right
        
        if u == self.r:
            child = self.r
            parent = None;
        else:
            parent = u.parent
            if u == parent.left:
                parent.left = child;
            elif u == parent.right:
                parent.right = child;
        
        if child:
            child.parent = parent;
            
        self.n -= 1
        
            

    def _remove_node(self, u: BinaryTree.Node):
        if u.left is None or u.right is None:    
            self._splice(u)
        else:
            w = u.right;
            while w.left != None:
                w = w.left;
            u.k = w.k
            u.v = w.v
            self._splice(w)
            
    def clear(self):
        """
        empties this BinarySearchTree
        """
        self.r = None
        self.n = 0

    def __iter__(self):
        u = self.first_node()
        while u is not None:
            yield u.k
            u = self.next_node(u)

    def first_node(self):
        w = self.r
        if w is None: return None
        while w.left is not None:
            w = w.left
        return w

    def next_node(self, w):
        if w.right is not None:
            w = w.right
            while w.left is not None:
                w = w.left
        else:
            while w.parent is not None and w.parent.left != w:
                w = w.parent
            w = w.parent
        return w



# tree = BinarySearchTree()

# tree.add(1, "b")
# tree.add(25, "z")
# tree.add(3, "d")
# tree.add(12, "m")
# tree.add(13, "n")
# tree.add(23, "x")
# tree.add(21, "v")
# tree.add(19, "t")
# tree.add(13, "n")
# tree.add(0, "a")
# tree.add(18, "s")

# tree.add(10, "b")
# tree.add(6, "z")
# tree.add(14, "d")
# tree.add(2, "m")
# tree.add(12, "n")
# tree.add(8, "x")
# tree.add(16, "v")
# tree.add(13, "t")

# tree.add(10, "b")
# tree.add(14, "d")
# tree.add(12, "n")
# tree.add(6, "z")
# tree.add(16, "v")
# tree.add(13, "t")
# tree.add(8, "x")
# tree.add(2, "m")



# for index, node in enumerate(tree.bf_order()):
#     print(node.k, node.v, "------", index + 1)