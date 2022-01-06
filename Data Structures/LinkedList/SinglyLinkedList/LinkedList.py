from LinkedListNode import LinkedListNode
import random

class LinkedList:
    def __init__(self, head=None) -> None:
        self.head = head
        
    def isEmpty(self):
        """Checks if linked list is empty.

        Returns:
            Boolean: If empty, True. Else False.
        """
        return not self.head
        
    # Insertion

    def push(self, node):
        """Pushes a node to the start of the linked list (it's the new head).

        Args:
            node (LinkedListNode): The node we want to insert.
        """
        node.next = self.head
        self.head = node
        
    def insertAt(self, node, index):
        """Inserts a node to the wanted index of the linked list.

        Args:
            node (LinkedListNode): The node we want to insert.
            index (Int): The index we want to insert "node" to

        Raises:
            IndexError: Index is out of bounds.
        """
        if index == 0:
            self.push(node)
        else:
            p = self.head
            for i in range(index - 1):
                if not p:
                    raise IndexError('Index is out of range')
                p = p.next
            node.next = p.next
            p.next = node

    def append(self, node):
        """Inserts a node as the last element of the linked list.

        Args:
            node (LinkedListNode): The node we want to insert.
        """
        if self.isEmpty():
            self.head = node
        else:
            p = self.head
            q = p.next
            while q != None:
                p = q
                q = q.next
            p.next = node
            node.next = None
            
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
        else:
            p = self.head
            q = p.next
            while q and q != node:
                p = q
                q = q.next
                
            if q:
                p.next = q.next
            else:
                raise ValueError
            
    def removeIndex(self, index):
        """Removes a node in the "index" position in the linked list.

        Args:
            node (LinkedListNode): The node we want to remove.

        Raises:
            IndexError: Index is out of bounds.
        """
        if index == 0 and self.head:
            self.head = self.head.next
        else:
            p = self.head
            for i in range(index - 1):
                if not p:
                    return
                p = p.next
                
            if p and p.next:
                p.next = p.next.next
            else:
                raise IndexError('Index is out of range')
           
    # Search
    
    def index(self, node):
        """Returns the index of the first occurence of node in the linked list.

        Args:
            node (LinkedListNode): The node we want to find.

        Returns:
            Int: Index of "node", -1 if node is not in the linked list.
        """
        p = self.head
        i = 0
        while p and p != node:
            p = p.next
            i += 1
            
        if p:
            return i
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
            return [self[ii] for ii in range(*index.indices(len(self)))]
        if self.isEmpty():
            raise IndexError('Index is out of range')
        p = self.head
        for i in range(index):
            p = p.next
            if not p:
                raise IndexError('Index is out of range')
        return p
    
    # Etc
    
    def isLooped(self):
        """Checks if the linked list contains a loop.

        Returns:
            LinkedListNode: Returns a node inside the loop. If there's no loop, returns False.
        """
        if self.isEmpty():
            return False
        p = self.head
        q = p.next
        while q and q.next and q != p:
            p = p.next
            q = q.next.next
            if p == q:
                return p
        return False
    
    def loopLength(self):
        """Returns the loop's length inside the linked list.

        Returns:
            Int: Length of loop in linked list. If there's no loop, returns -1.
        """
        p = self.isLooped()
        if not p:
            return -1
        count = 1
        step = p.next
        while p != step:
            count += 1
            step = step.next
        return count
    
    def isPalindrome(self):
        """Checks if values inside linked list are showing a palindrome pattern.

        Returns:
            Boolean: True if palindrome, else False.
        """
        n = len(self)
        l = n // 2
        if n % 2 == 1:
            u = l
        else:
            u = l + 1
            
        while l >= 0 and u < n:
            if self[l].value != self[u].value:
                return False
            l -= 1
            u += 1
        
        if l >= 0 or u < n:
            return False
        return True

    def __len__(self):
        """Returns how many elements are in the linked list.

        Returns:
            Int: number of elements.
        """
        count = 0
        p = self.head
        while p:
            count += 1
            p = p.next
            
        return count
    
    def __iter__(self):
        p = self.head
        while p:
            yield p
            p=p.next
            
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
    
    linked = LinkedList(LinkedListNode(123))
    for i in range(10):
        linked.append(LinkedListNode(random.randint(-20, 20)))
    print(linked)
    
    # Insertion
    
    print("Insertion")
    
    a = LinkedListNode(50)
    b = LinkedListNode(30)
    c = LinkedListNode(100)
    
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
    print(linked[2].value)
    
    a = LinkedListNode(123)
    b = LinkedListNode(20)
    c = LinkedListNode(15)
    d = LinkedListNode(76)
    e = LinkedListNode(82)
    
    linked2 = LinkedList(a)
    linked2.append(b)
    linked2.append(c)
    linked2.append(d)
    linked2.append(e)
    e.next = a
    
    print(linked2.loopLength())
    
    # print(any(x.value == 100 for x in linked))