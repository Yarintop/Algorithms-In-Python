from DataStructures.Trees.BinaryTree.BinaryTreeNode import BinaryTreeNode
import random

class BinaryTree:
    def __init__(self, root=None) -> None:
        if isinstance(root, BinaryTreeNode):
            self.root = root
        else:
            if root:
                self.root = BinaryTreeNode(root)
            else:
                self.root = None
        
    def isEmpty(self):
        return self.root == None
        
    def insert(self, data):
        if isinstance(data, BinaryTreeNode):
            node = data
        else:
            node = BinaryTreeNode(data)
            
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
                
    def remove(self, data, root=-1):
        if self.isEmpty():
            raise ValueError("Tree is empty.")
        if root == -1:
            root = self.root
        if root == None:
            return None
        
        if root.value != data:
            root.left = self.remove(data, root.left)
            root.right = self.remove(data, root.right)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            
            temp = root.right
            while temp.left or temp.right:
                if temp.right:
                    temp = temp.right
                elif temp.left:
                    temp = temp.left
            root.value = temp.value
            root.right = self.remove(temp.value, root.right)
            
        return root
            
    def search(self, data, node=None, order=-1, parent=False):
        if node == None:
            if self.isEmpty():
                return -1
            node = self.root
        
        def left():
            if node.left:
                l = self.search(data, node.left, order, parent)
                if l != None:
                    if parent and isinstance(l, BinaryTreeNode):
                        return l + [node]
                    return l
            return None
                
        def middle():
            if node.value == data:
                if parent:
                    return [node]
                return node
            return None
            
        def right():
            if node.right:
                r = self.search(data, node.right, order, parent)
                if r != None:
                    if parent and isinstance(r, BinaryTreeNode):
                        return r + [node]
                    return r
            return None
        
        def functionOrder(first, second, third):
            f = first()
            if f != None:
                return f
            s = second()
            if s != None:
                return s
            t = third()
            if t != None:
                return t
            return None
                
        if order == -1:
            return functionOrder(middle, left, right)
        elif order == 0:
            return functionOrder(left, middle, right)
        else:
            return functionOrder(left, right, middle)
        
    def __str__(self):
        s = []
        q = [self.root]
        while len(q):
            t = q.pop(0)
            s.append(t)
            if t.left:
                q.append(t.left)
            if t.right:
                q.append(t.right)
        return str(s)
    
    
if __name__ == "__main__":
    binaryTree = BinaryTree(123)
    binaryTree.insert(543)
    binaryTree.insert(1)
    binaryTree.insert(4)
    binaryTree.insert(765)
    
    print(binaryTree)
    
    n = binaryTree.search(543)
    
    binaryTree.remove(123)
    print(binaryTree)
    