class MinHeap:
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
        if self.isEmpty():
            return None
        self.swap(0, len(self) - 1)
        popped = self.heap.pop(len(self) - 1)
        self.heapifyPos(0)
        return popped
    
    def replace(self, data): # More efficient than pop followed by insert, since only need to balance once.
        if self.isEmpty():
            raise IndexError("Cannot replace because heap is empty.")
        popped = self.heap[0]
        self.heap[0] = data
        self.heapifyPos(0)
        return popped
    
    def heapify(self):
        for i in reversed(range(0, len(self) // 2)):
            self.heapifyPos(i)
    
    def heapifyPos(self, pos):
        if not self.isLeaf(pos):
            leftPos = self.left(pos)
            rightPos = self.right(pos)
            if leftPos < len(self) and self.heap[leftPos] < self.heap[pos]:
                self.swap(pos, leftPos)
            elif rightPos < len(self) and self.heap[rightPos] < self.heap[pos]:
                self.swap(pos, rightPos)
                
    def insert(self, data):
        currPos = len(self)
        self.heap.append(data)
        while self.heap[currPos] < self.heap[self.parent(currPos)]:
            self.swap(currPos, self.parent(currPos))
            currPos = self.parent(currPos)
            
    def merge(self, h):
        currHeap = self.heap
        self.heap += h
        self.heapify()
        newHeap = self.heap
        self.heap = currHeap
        return newHeap
    

            
    def __str__(self):
        return str(self.heap)
        
    def __len__(self):
        return len(self.heap)