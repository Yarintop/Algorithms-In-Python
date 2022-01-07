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
                
    def remove(self, data):
        pass
        
    def search(self, data, node=None, order=-1):
        if node == None:
            if self.isEmpty():
                return -1
            node = self.root
        
        def left():
            if node.left:
                l = self.searchPreOrder(data, node.left)
                if l != -1:
                    return l
            return -1
                
        def middle():
            if node.value == data:
                return node
            return -1
            
        def right():
            if node.right:
                r = self.searchPreOrder(data, node.right)
                if r != -1:
                    return r
            return -1
        
        def functionOrder(first, second, third):
            f = first()
            if f != -1:
                return f
            s = second()
            if s != -1:
                return s
            t = third()
            if t != -1:
                return t
            return -1
                
        if order == -1:
            return functionOrder(middle, left, right)
        elif order == 0:
            return functionOrder(left, middle, right)
        else:
            return functionOrder(left, right, middle)
        if node == None:
            if self.isEmpty():
                return -1
            node = self.root
        
        if node.value == data:
            return node
        
        if node.left:
            l = self.searchPreOrder(data, node.left)
            if l != -1:
                return l
            
        if node.right:
            r = self.searchPreOrder(data, node.right)
            if r != -1:
                return r
            
        return -1