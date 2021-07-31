

class Node:
    def __init__(self, value=-1, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class BinaryTree:
    def __init__(self):
        self.root = None
    
    def _print(self, node=None):
        if node == None:
            node = self.root
        if node == None:
            return
        
        print(node.value)
        if node.left != None:
            self._print(node.left)
        if node.right != None:
            self._print(node.right)
        
        
        
n = Node(10)
m = Node(11, n)
tree = BinaryTree()
tree.root = m


tree._print()