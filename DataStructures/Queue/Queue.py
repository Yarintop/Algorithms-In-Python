from QueueNode import QueueNode
import random

class Queue:
    def __init__(self, head=None) -> None:
        self.head = head
        self.tail = head
        
    def isEmpty(self):
        return self.head == None
    
    # Insertion
    
    def enqueue(self, data):
        """Pushes node to the last poisition of the queue (FIFO).

        Args:
            node (StackNode): The node we're inserting.
        """
        node = QueueNode(data)
        if self.isEmpty():
            self.head = node
            self.tail = node
        else:
            self.tail.prev = node
            self.tail = node
            
    # Deletion
    
    def dequeue(self):
        """Taking out the first node from the queue and returning it.

        Returns:
            node (StackNode): The node we're returning.
        """
        if self.isEmpty():
            return None
        t = self.head
        self.head = self.head.prev
        return t.value
    
    def peek(self):
        """Return the first node from the queue without taking it out.

        Returns:
            node (StackNode): The node we're returning.
        """
        return self.head.value
    
    def __str__(self):
        if self.isEmpty():
            return "The stack is empty."
        p = self.head
        s = ''
        while p:
            s = f'{p.value} -> ' + s
            p = p.prev
        s = s[:-4]
        return s
    
if __name__ == "__main__":
    print('Initialize Stack')
    stack = Queue()
    for i in range(10):
        stack.enqueue(random.randint(-20, 20))
    print(stack)
    
    # Insertion
    
    print("Insertion")
    
    a = 50
    b = 30
    
    stack.enqueue(a)
    print(stack)
    stack.enqueue(b)
    print(stack)
    
    # Deletion
    
    print("Deletion")
    
    print(stack)
    print(stack.dequeue())
    print(stack)
    print(stack.dequeue())
    print(stack)
    print(stack.dequeue())