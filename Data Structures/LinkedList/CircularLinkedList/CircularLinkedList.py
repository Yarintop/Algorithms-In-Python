from CircularLinkedListNode import CircularLinkedListNode
import random

class CircularLinkedList:
    def __init__(self, head=None) -> None:
        if not head:
            self.head = None
        else:
            if isinstance(head, CircularLinkedListNode):
                self.head = head
            else:
                self.head = CircularLinkedListNode(head)
            self.head.next = self.head
                
    def isEmpty(self) -> bool:
        """Checks if linked list is empty.

        Returns:
            Boolean: If empty, True. Else False.
        """
        return self.head == None
    
    # Insertion
    
    def push(self, data):
        """Pushes a node to the start of the linked list (it's the new head).

        Args:
            node (LinkedListNode): The node we want to insert.
        """
        if isinstance(data, CircularLinkedListNode):
            node = data
        else:
            node = CircularLinkedListNode(data)
        t = self.head
        while t.next != self.head:
            t = t.next
        t.next = node
        node.next = self.head
        self.head = node
           
    def insertAt(self, data, index):
        """Inserts a node to the wanted index of the linked list.

        Args:
            node (LinkedListNode): The node we want to insert.
            index (Int): The index we want to insert "node" to
        """
        if isinstance(data, CircularLinkedListNode):
            node = data
        else:
            node = CircularLinkedListNode(data)
        if self.isEmpty():
            self.head = index
        l = len(self)
        index = index % l # To prevent useless cycles
        if index < 0:
            index += l
        t = self.head
        for i in range(index - 1):
            t = t.next
        node.next = t.next
        t.next = node
        
    def append(self, data):
        """Inserts a node as the last element of the linked list.

        Args:
            node (LinkedListNode): The node we want to insert.
        """
        if isinstance(data, CircularLinkedListNode):
            node = data
        else:
            node = CircularLinkedListNode(data)
        t = self.head
        while t.next != self.head:
            t = t.next
        t.next = node
        node.next = self.head
        
    # Deletion
    
    def remove(self, data):
        """Removes the first occurence of a node in the linked list.

        Args:
            node (LinkedListNode): The node we want to remove.

        Raises:
            ValueError: node is not in the linked list.
        """
        if self.isEmpty():
            raise ValueError("node is not in the linked list.")
        
        if isinstance(data, CircularLinkedListNode):
            node = data
        else:
            node = CircularLinkedListNode(data)
        
        if len(self) == 1 and self.head.value == node.value:
            self.head = None
        else:
            t = self.head
            while t.next.value != node.value:
                t = t.next
                if t == self.head:
                    raise ValueError("node is not in the linked list.")
                
            if t.next == self.head:
                self.head = self.head.next
                
            t.next = t.next.next
        
    def removeIndex(self, index):
        """Removes a node in the "index" position in the linked list.

        Args:
            node (LinkedListNode): The node we want to remove.
        """
        if self.isEmpty():
            raise IndexError("List is empty, therefore every index is out of range.")
        l = len(self)
        index = index % l
        if index < 0:
            index += l
            
        if index == 0:
            self.remove(self.head)
        else:
            t = self.head
            for i in range(index - 1):
                t = t.next
                
            t.next = t.next.next
            
    # Search
    
    def index(self, data):
        """Returns the index of the first occurence of node in the linked list.

        Args:
            node (LinkedListNode): The node we want to find.

        Returns:
            Int: Index of "node", -1 if node is not in the linked list.
        """
        if self.isEmpty():
            return -1
        
        index = 0
        t = self.head
        while t.value != data:
            index += 1
            t = t.next
            if t == self.head:
                return -1
        return index
    
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
            return [self[i].value for i in range(*index.indices(len(self)))]
        index = index % len(self)
        if self.isEmpty():
            raise IndexError('Index is out of range')
        p = self.head
        for i in range(index):
            p = p.next
            if not p:
                raise IndexError('Index is out of range')
        return p.value
        
    def __len__(self):
        if self.isEmpty():
            return 0
        count = 1
        t = self.head.next
        while t and t != self.head:
            count += 1
            t = t.next
        
        return count
    
    def __str__(self):
        if self.isEmpty():
            return "The linked list is empty."
        p = self.head
        s = '╭'
        while True:
            s += f' -> {p.value} -> '
            p = p.next
            if p == self.head:
                break
        s += '╮'
        l = len(s)
        s += f'\n╰{"-" * (l - 2)}╯'
        return s
            
if __name__ == "__main__":
        
    print("Initialize linked")
    
    linked = CircularLinkedList(123)
    for i in range(10):
        linked.append(random.randint(-20, 20))
    print(linked)
    
    # Insertion
    
    print("Insertion")
    
    a = 50
    b = 30
    c = 100
    
    linked.append(a)
    print(linked)
    linked.push(b)
    print(linked)
    linked.insertAt(c, len(linked) // 2)
    print(linked)
    
    # Deletion
    
    print("Deletion")
    
    linked.remove(b)
    print(linked)
    linked.removeIndex(6)
    print(linked)
    linked.removeIndex(2)
    print(linked)
    linked.removeIndex(0)
    print(linked)
    
    # Search
    
    print(linked.index(a))
    print(linked.index(b))
    print(linked.index(c))
    print(linked[2])