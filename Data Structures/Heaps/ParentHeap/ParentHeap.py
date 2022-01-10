
class ParentHeap:
    def __new__(cls, *args, **kwargs):
        """This class should not be used, it is only the parent class of the Min-Heap and Max-Heap

        Raises:
            TypeError: Cannot instantiate ParentHeap.
        """
        if cls is ParentHeap:
            raise TypeError(f'Only children of {cls.__name__} may be instantiated (i.e. Min-Heap and Max-Heap).')
        return object.__new__(cls, *args, **kwargs)
    
    def __init__(self, root = None) -> None:
        self.heap = []
        if root:
            self.heap.append(root)
    
    def isEmpty(self):
        return len(self) > 0
    
    def parent(self, pos):
        return pos // 2
    
    def left(self, pos):
        return pos * 2
    
    def right(self, pos):
        return (pos * 2) + 1
    
    def isLeaf(self, pos):
        size = len(self) 
        if pos >= size // 2 and pos < size:
            return True
        return False
    
    def swap(self, pos1, pos2):
        self.heap[pos1], self.heap[pos2] = self.heap[pos2], self.heap[pos1]
    
    def peek(self):
        return self.heap[0]
    
    def pop(self):
        popped = self.heap.pop(0)
        return popped
    
    def replace(self, data): # More efficient than pop followed by insert, since only need to balance once.
        if self.isEmpty():
            raise IndexError("Cannot replace because heap is empty.")
        popped = self.heap[0]
        self.heap[0] = data
        return popped
                
    def insert(self, data):
        self.heap.insert(0, data)
            
    def merge(self, h):
        return self.heap + h  
            
    def __str__(self):
        return str(self.heap)
        
    def __len__(self):
        return len(self.heap)