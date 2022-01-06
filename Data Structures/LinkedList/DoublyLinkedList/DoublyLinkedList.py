from DoublyLinkedListNode import DoublyLinkedListNode
import random

class DoublyLinkedList:
    def __init__(self, head=None) -> None:
        self.head = head
            
    def isEmpty(self) -> bool:
        """Checks if linked list is empty.

        Returns:
            Boolean: If empty, True. Else False.
        """
        return self.head == None
    
    # Insertion
    
    def push(self, node):
        """Pushes a node to the start of the linked list (it's the new head).

        Args:
            node (LinkedListNode): The node we want to insert.
        """
        node.next = self.head
        self.head = node
        if node.next:
            node.next.prev = node
        
        
    def insertAt(self, node, index):
        """Inserts a node to the wanted index of the linked list.

        Args:
            node (LinkedListNode): The node we want to insert.
            index (Int): The index we want to insert "node" to
        """
        t = self.head
        for i in range(index - 1):
            if not t:
                raise IndexError("Index is out of range.")
            t = t.next
        
        node.next = t.next
        t.next = node
        node.prev = t
        if node.next:
            node.next.prev = node
        
    def append(self, node):
        """Inserts a node as the last element of the linked list.

        Args:
            node (LinkedListNode): The node we want to insert.
        """
        if self.isEmpty():
            self.head = node
        else:
            t = self.head
            while t.next:
                t = t.next
            t.next = node
            node.prev = t
        
    # Deletion
    
    def remove(self, node):
        """Removes the first occurence of a node in the linked list.

        Args:
            node (LinkedListNode): The node we want to remove.

        Raises:
            ValueError: node is not in the linked list.
        """
        if node == self.head:
            self.head = self.head.next
            self.head.prev = None
        else:
            t = self.head
            while t and t != node:
                t = t.next
                
            if t:
                if t.prev:
                    t.prev.next = t.next
                if t.next:
                    t.next.prev = t.prev
            else:
                raise ValueError("Node is not in list.")
        
    def removeIndex(self, index):
        """Removes a node in the "index" position in the linked list.

        Args:
            node (LinkedListNode): The node we want to remove.
        """
        t = self.head
        for i in range(index - 1):
            if not t:
                raise IndexError("Index is out of range.")
            t = t.next
        
        if t.next:
            t.next = t.next.next
            if t.next.next:
                t.next.next.prev = t
        else:
            raise IndexError("Index is out of range.")
            
    # Search
    
    def index(self, node):
        """Returns the index of the first occurence of node in the linked list.

        Args:
            node (LinkedListNode): The node we want to find.

        Returns:
            Int: Index of "node", -1 if node is not in the linked list.
        """
        t = self.head
        index = 0
        while t and t != node:
            t = t.next
            index += 1
            
        if t:
            return index
        return -1
    
    def __getitem__(self, index):
        """Returns the node in the "index" position, if index is a slice, then return a slice of nodes accordingly

        Args:
            index (Int): The index or slice we want to get.

        Raises:
            IndexError: Index is out of range.

        Returns:
            LinkedListNode: The node we want
            
            (Or, in case index is a Slice)
            
            List (LinkedListNodes): An array of LinkedListNodes according to the slice.
        """
        if isinstance(index, slice):
            return [self[i] for i in range(*index.indices(len(self)))]
        if self.isEmpty():
            raise IndexError("Index is out of range.")
        t = self.head
        for i in range(index - 1):
            if not t:
                raise IndexError("Index is out of range.")
            t = t.next
        
        if t:
            return t
        raise IndexError("Index is out of range.")
        
    def __len__(self):
        count = 0
        t = self.head
        while t:
            count += 1
            t = t.next
        
        return count
    
    def __str__(self):
        if self.isEmpty():
            return "The linked list is empty."
        p = self.head
        s = ''
        while p:
            s += f'{p.value} -> '
            p = p.next
        s = s[:-4]
        return s
            
if __name__ == "__main__":
        
    # Initialize linked
    
    print("Initialize linked")
    
    linked = DoublyLinkedList(DoublyLinkedListNode(123))
    for i in range(10):
        linked.append(DoublyLinkedListNode(random.randint(-20, 20)))
    print(linked)
    
    # # Insertion
    
    print("Insertion")
    
    a = DoublyLinkedListNode(50)
    b = DoublyLinkedListNode(30)
    c = DoublyLinkedListNode(100)
    
    linked.append(a)
    print(linked)
    linked.push(b)
    print(linked)
    linked.insertAt(c, len(linked) // 2)
    print(linked)
    
    # # Deletion
    
    print("Deletion")
    
    linked.remove(b)
    print(linked)
    linked.removeIndex(6)
    print(linked)
    linked.removeIndex(2)
    print(linked)
    linked.removeIndex(0)
    print(linked)
    
    # # # Search
    
    print(linked.index(a))
    print(linked.index(b))
    print(linked.index(c))
    print(linked[4].value)
    
    # print([x.value for x in linked[-7:8]])
    
    # # print(any(x.value == 100 for x in linked))
        
    
