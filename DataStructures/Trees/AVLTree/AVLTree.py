from DataStructures.Trees.AVLTree.AVLTreeNode import AVLTreeNode
import random

class AVLTree:
    def __init__(self) -> None:
        self.root = None
        
    def isEmpty(self):
        return self.root == None
        
    def insert(self, data, root=None): 
        if self.isEmpty():
            self.root = AVLTreeNode(data)
            return
        
        if root == None:
            root =  self.root
            
        if data < root.value:
            if root.left:
                root.left = self.insert(data, root.left)
            else:
                root.left = AVLTreeNode(data)
        else:
            if root.right:
                root.right = self.insert(data, root.right)
            else:
                root.right = AVLTreeNode(data)
        
        leftHeight = self.getHeight(root.left)
        rightHeight = self.getHeight(root.right)
        
        root.height = 1 + max(leftHeight, rightHeight)
        balance = leftHeight - rightHeight
        
        if balance > 1:
            if data <= root.left.value:
                return self.rightRotate(root)
            else:
                root.left = self.leftRotate(root.left)
                return self.rightRotate(root)
        elif balance < -1:
            if data > root.right.value:
                return self.leftRotate(root)
            else:
                root.right = self.right(root.right)
                return self.leftRotate(root)
            
        return root
    
    def remove(self, data, root=None):
        if self.isEmpty():
            raise ValueError("Tree is empty.")
        if root == None:
            root = self.root
        
        if data < root.value:
            if root.left:
                root.left = self.remove(data, root.left)
            else:
                raise ValueError(f"{data} is not in tree so it couldn't be removed.")
        elif data > root.value:
            if root.right:
                root.right = self.remove(data, root.right)
            else:
                raise ValueError(f"{data} is not in tree so it couldn't be removed.")
        else:
            if not root.left and not root.right: # root is a leaf.
                if self.root == root:
                    self.root = None
                    return self.root
                return None
            elif not root.left: # root only has one child (the right one).
                if self.root == root:
                    self.root = root.right
                return root.right
            elif not root.right: # root only has one child (the left one).
                if self.root == root:
                    self.root = root.left
                return root.left
            
            # root has both children.
            
            temp = root.right
            while temp.left:
                temp = temp.left
                
            root.value = temp.value
            root.right = self.remove(temp.value, root.right)
            
        leftHeight = self.getHeight(root.left)
        rightHeight = self.getHeight(root.right)
        
        root.height = 1 + max(leftHeight, rightHeight)
        balance = leftHeight - rightHeight
        
        if balance > 1:
            if data <= root.left.value:
                return self.rightRotate(root)
            else:
                root.left = self.leftRotate(root.left)
                return self.rightRotate(root)
        elif balance < -1:
            if data > root.right.value:
                return self.leftRotate(root)
            else:
                root.right = self.right(root.right)
                return self.leftRotate(root)
            
        return root
        
    def leftRotate(self, node):
        rightNode = node.right
        rightLeftNode = rightNode.left
        
        rightNode.left = node
        node.right = rightLeftNode
        
        node.height = 1 + max(self.getHeight(node.left), self.getHeight(node.right))
        rightNode.height = 1 + max(self.getHeight(rightNode.left), self.getHeight(rightNode.right))
        
        if self.root == node:
            self.root = rightNode
        
        return rightNode
    
    def rightRotate(self, node):
        leftNode = node.left
        leftRightNode = leftNode.right
        
        leftNode.right = node
        node.left = leftRightNode
        
        node.height = 1 + max(self.getHeight(node.left), self.getHeight(node.right))
        leftNode.height = 1 + max(self.getHeight(leftNode.left), self.getHeight(leftNode.right))
        
        if self.root == node:
            self.root = leftNode
        
        return leftNode
    
    def getHeight(self, node):
        if node == None:
            return 0
        
        return node.height
            
    def search(self, data, node=None):
        if node == None:
            if self.isEmpty():
                return -1
            node = self.root
        
        if node.value == data:
            return node
        
        if node.value > data:
            if node.left:
                return self.search(data, node.left)
            return -1
        else:
            if node.right:
                return self.search(data, node.right)
            return -1
        
    def __str__(self):
        if self.isEmpty():
            return "Tree is Empty."
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
    avlTree = AVLTree()
    avlTree.insert(1)
    avlTree.insert(2)
    avlTree.insert(3)
    avlTree.insert(4)
    avlTree.insert(5)
    avlTree.insert(6)
    avlTree.insert(7)
    
    print(avlTree)
    
    n = avlTree.search(765)
    
    print(n)
    
    avlTree.remove(5)
    avlTree.remove(6)
    avlTree.remove(7)
    
    print(avlTree)
    
    a = AVLTree()
    a.insert(5)
    
    print(a)
    a.remove(5)
    print(a)
    