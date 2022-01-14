class AVLTreeNode:
    def __init__(self, value = None, left=None, right=None, height=1):
        self.value = value
        self.left = left
        self.right = right
        self.height = height
        self.count = 1
        
    def __str__(self):
        return str(self.value)
    
    def __repr__(self):
        return self.__str__()
    