from DataStructures.Lists.SelfOrganizingList.SelfOrganizingListNode import SelfOrganizingListNode

class SelfOrganizingList:
    def __init__(self) -> None:
        self.head = None
    
    def isEmpty(self):
        return self.head == None
    
    def append(self, data):
        if self.isEmpty():
            self.head = SelfOrganizingListNode(data)
        else:
            node = self.head
            while node.next:
                node = node.next
            node.next = SelfOrganizingListNode(data)
            
    def remove(self, data):
        if self.isEmpty():
            raise ValueError(f"{data} is not in list.")
        if self.head.value == data:
            self.head = self.head.next
        else:
            q = self.head
            while q and q.value != data:
                p = q
                q = q.next
            if not q:
                raise ValueError(f"{data} is not in list.")
            p.next = q.next
            
    def search(self, data):
        if self.isEmpty():
            return -1
        if self.head.value == data:
            self.head.count += 1
            return self.head
        q = self.head
        while q and q.value != data:
            p = q
            q = q.next
        if q:
            q.count += 1
            self.rearrange(q, p)
            return q
        return -1
        
    def rearrange(self, node, prevnode):
        if node.count <= prevnode.count:
            if not node.next or node.count >= node.next.count:
                return
        prevnode.next = node.next
        p = None
        q = self.head
        while q.next and q.count > node.count:
            p = q
            q = q.next
        if not q.next:
            q.next = node
        elif not p:
            node.next = self.head
            self.head = node
        else:
            node.next = q
            p.next = node
            
    def __str__(self):
        if self.isEmpty():
            return "List is empty."
        s = ''
        node = self.head
        while node:
            s += f'({node.value}, count: {node.count}) -> '
            node = node.next
        return s[:-4]
        
if __name__ == "__main__":
    l = SelfOrganizingList()
    l.append(3)
    l.append(6)
    l.append(4)
    l.append(9)
    l.append(313)
    l.append(24)
    l.append(76)
    print(l)
    l.remove(313)
    print(l)
    print(l.search(76))
    print(l)
    print(l.search(76))
    print(l)
    print(l.search(24))
    print(l)
    print(l.search(9))
    print(l)
    print(l.search(9))
    print(l)
    print(l.search(9))
    print(l)
    
    