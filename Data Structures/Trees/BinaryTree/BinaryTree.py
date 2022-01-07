import random

class BinaryTree:
    def __init__(self) -> None:
        self.root = None
        
    def isEmpty(self):
        return self.root == None
        
    def insert(self, node):
        if self.isEmpty():
            self.root = node
        else:
            r = self.root
            while r.left and r.right:
                if random.randint(0, 1) % 2 == 0:
                    r = r.left
                else:
                    r = r.right
            
            if not r.left:
                r.left = node
            else:
                r.right = node
                
    def remove(self, node):
        
        
    def searchPreOrder(self, node):
        