class BinarySearchTreeNode:
    def __init__(self, value = None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
        
    def __str__(self):
        return str(self.value)
    
    def __repr__(self):
        return self.__str__()
    