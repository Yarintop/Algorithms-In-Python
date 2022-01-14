from DataStructures.Stack.StackNode import StackNode
import random

class Stack:
    def __init__(self, head=None) -> None:
        self.head = head
        
    def isEmpty(self):
        return self.head == None
    
    # Insertion
    
    def push(self, data):
        """Pushes node to the first poisition of the stack (LIFO).

        Args:
            node (StackNode): The node we're inserting.
        """
        node = StackNode(data)
        if self.isEmpty():
            self.head = node
        else:
            node.next = self.head
            self.head = node
            
    # Deletion
    
    def pop(self):
        """Taking out the first node from the stack and returning it.

        Returns:
            node (StackNode): The node we're returning.
        """
        if self.isEmpty():
            return None
        t = self.head
        self.head = self.head.next
        return t.value
    
    def peek(self):
        """Return the first node from the stack without taking it out.

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
            s += f'{p.value} -> '
            p = p.next
        s = s[:-4]
        return s
    
if __name__ == "__main__":
    print('Initialize Stack')
    stack = Stack()
    for i in range(10):
        stack.push(random.randint(-20, 20))
    print(stack)
    
    # Insertion
    
    print("Insertion")
    
    a = 50
    b = 30
    
    stack.push(a)
    print(stack)
    stack.push(b)
    print(stack)
    
    # Deletion
    
    print("Deletion")
    
    print(stack)
    print(stack.pop())
    print(stack)
    print(stack.pop())
    print(stack)
    print(stack.pop())