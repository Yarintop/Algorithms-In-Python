from BinaryTreeNode import BinaryTreeNode
import random

class BinaryTree:
    def __init__(self, root) -> None:
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
                
    def remove(self, data, currNode=-1):
        if self.isEmpty():
            raise ValueError("Tree is empty.")
        if currNode == -1:
            currNode = self.root
        if currNode == None:
            return None
        
        if currNode.value != data:
            currNode.left = self.remove(data, currNode.left)
            currNode.right = self.remove(data, currNode.right)
        else:
            if not currNode.left:
                return currNode.right
            elif not currNode.right:
                return currNode.left
            
            temp = currNode.right
            while temp.left or temp.right:
                if temp.right:
                    temp = temp.right
                elif temp.left:
                    temp = temp.left
            currNode.value = temp.value
            currNode.right = self.remove(temp.value, currNode.right)
            
        return currNode
            
    def search(self, data, node=None, order=-1, parent=False):
        if node == None:
            if self.isEmpty():
                return -1
            node = self.root
        
        def left():
            if node.left:
                l = self.search(data, node.left, order, parent)
                if l != -1:
                    if parent and isinstance(l, BinaryTreeNode):
                        return l + [node]
                    return l
            return -1
                
        def middle():
            if node.value == data:
                if parent:
                    return [node]
                return node
            return -1
            
        def right():
            if node.right:
                r = self.search(data, node.right, order, parent)
                if r != -1:
                    if parent and isinstance(r, BinaryTreeNode):
                        return r + [node]
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
    