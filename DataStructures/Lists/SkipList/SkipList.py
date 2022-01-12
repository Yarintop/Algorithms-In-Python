from DataStructures.Lists.SkipList.SkipListNode import SkipListNode
import random

class SkipList:
    def __init__(self) -> None:
        self.head = None
        
    def isEmpty(self):
        return self.head == None
        
    def insert(self, data):
        if self.isEmpty():
            self.head = SkipListNode(data)
            self.head.nextNodeWidth = len(self)
        elif data <= self.head.value:
            newHead = tempNewHead = SkipListNode(data)
            tempHead = self.head
            while tempHead:
                newHeadLevel = SkipListNode(data)
                newHeadLevel.next = tempHead
                tempNewHead.nextLevel = newHeadLevel
                tempNewHead.nextNodeWidth = 1
                
                tempNewHead = newHeadLevel
                tempHead = tempHead.nextLevel
            tempNewHead.nextNodeWidth = 1
            self.head = newHead
            newHead.nextNodeWidth = len(self)
        else:
            levelNodes = []
            currNode = self.head
            while True:
                while currNode.next and currNode.next.value < data:
                    currNode = currNode.next
                if currNode.nextLevel == None:
                    break
                levelNodes.insert(0, currNode)
                currNode = currNode.nextLevel
            newNode = SkipListNode(data)
            if not currNode.next:
                currNode.next = newNode
            else:
                newNode.next = currNode.next
                currNode.next = newNode
            newNode.nextNodeWidth = 1
            self.randomizeLevel(levelNodes, newNode)
                
    def randomizeLevel(self, levelNodes, lowerLevelNode):
        while len(levelNodes) > 0:
            p = random.randint(0, 1)
            if p % 2 == 0:
                lastNode = levelNodes.pop(0)
                newNode = SkipListNode(lowerLevelNode.value)
                newNode.next = lastNode.next
                lastNode.next = newNode
                
                newNode.nextLevel = lowerLevelNode
                lowerLevelNode = newNode
                
                lastNodeIndex = self.getIndexOfNode(lastNode)
                newNodeIndex = self.getIndexOfNode(newNode)
                nextNodeIndex = self.getIndexOfNode(newNode.next)
                
                lastNode.nextNodeWidth = newNodeIndex - lastNodeIndex
                newNode.nextNodeWidth = nextNodeIndex - newNodeIndex
                
            else:
                break
            
        if len(levelNodes) == 0:
            newHead = SkipListNode(self.head.value)
            newHead.nextLevel = self.head
            newHead.nextNodeWidth = len(self)
            self.head = newHead
        
        while len(levelNodes) > 0:
            lastNode = levelNodes.pop(0)
            lastNode.nextNodeWidth += 1
            
    def remove(self, data):
        if self.isEmpty():
            return
        elif data == self.head.value:
            if len(self) == 1:
                self.head = None
            else:
                currHead = self.head
                while currHead.next == None or currHead.nextNodeWidth != 1:
                    currHead = currHead.nextLevel
                newData = currHead.next.value
                self.remove(newData)
                currHead = self.head
                while currHead != None:
                    currHead.value = newData
                    currHead = currHead.nextLevel
        else:
            head = self.head
            while head:
                while head.next and head.next.value < data:
                    head = head.next
                if head.next:
                    head.nextNodeWidth += head.next.nextNodeWidth - 1
                    head.next = head.next.next
                else:
                    head.nextNodeWidth -= 1
                head = head.nextLevel
                
    def search(self, data):
        if self.isEmpty():
            return None
        head = self.head
        while head:
            while head.next and head.next.value < data:
                head = head.next
            if head.next and head.next.value == data:
                return head.next
            head = head.nextLevel
        return None

    def update(self, oldData, newData):
        self.remove(oldData)
        self.insert(newData)
            
    def getIndexOfNode(self, node):
        if node == None:
            return len(self)
        head = self.head
        while node.nextLevel or head.nextLevel:
            if node.nextLevel:
                node = node.nextLevel
            if head.nextLevel:
                head = head.nextLevel
        index = 0
        while head != node:
            if head == None:
                raise ValueError("The node is not in the list.")
            index += 1
            head = head.next
        return index
    
    def __str__(self):
        head = self.head
        nodes = []
        while head:
            nodes.insert(0, [])
            node = head
            while node:
                nodes[0].append(node)
                node = node.next
            head = head.nextLevel
        res = ''
        for n in nodes[0]:
            res += f'{n.value} -> '
        res = res[:-4] + ' -> None'
        for level in nodes[1:]:
            i = 0
            tempRes = ''
            for n in level:
                tempRes += f'{n.value} '
                for j in range(1, n.nextNodeWidth):
                    tempRes += '-' * (4 + len(str(nodes[0][i + j].value)))
                i += n.nextNodeWidth
                tempRes += '-> '
            tempRes = tempRes[:-4] + ' -> None\n'
            res = tempRes + res
            
        return res
    
    def __len__(self):
        if self.isEmpty():
            return 0
        currNode = self.head
        while currNode.nextLevel:
            currNode = currNode.nextLevel
        count = 0
        while currNode:
            count += 1
            currNode = currNode.next
        return count
                
if __name__ == "__main__":
    s = SkipList()
    for i in range(10):
        s.insert(random.randint(-20, 20))
        
    s.insert(300)
    s.insert(0)
    s.insert(-300)
    s.insert(1)

    print(s)
    print('--------------')
    s.remove(300)
    print(s)
    print('--------------')
    s.remove(0)
    print(s)
    print('--------------')
    s.remove(-300)
    print(s)
    print(s.search(1))
    print(s.search(707))
    s.update(1, 707)
    print(s)
    print(s.search(40))
    print(s.search(707))
