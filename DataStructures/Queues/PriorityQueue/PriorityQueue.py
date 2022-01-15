# TODO: Change Min Heap to a Fibonacci Heap
from DataStructures.Heaps.MinHeap import MinHeap

class PriorityQueue: # Note that although a priority queue is ESSENTIALLY a heap, it's sometimes better to have an interface like this.
    def __init__(self):
        self.heap = MinHeap.MinHeap()
        
    def push(self, item):
        if item.__lt__ is object.__lt__:
            raise ValueError("An item must be comparable before inserting it to a priority queue.")
            
        self.heap.insert(item)
        
    def get(self):
        return self.heap.pop()
    
    def __len__(self):
        return len(self.heap)
        