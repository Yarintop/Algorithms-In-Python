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
            newHead.nextNodeWidth = 1
            self.head = newHead
        else: #TODO add nextNodeWidth while adding in middle of list.
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
            else:
                break
        if len(levelNodes) == 0:
            newHead = SkipListNode(self.head.value)
            newHead.nextLevel = self.head
            self.head = newHead
    
    def __str__(self):
        head = self.head
        nodes = []
        i = 0
        while head:
            nodes.append([])
            node = head
            while node:
                for j in range(i):
                    nodes[j].insert(nodes[j].index('None'), None)
                nodes[i].append(node.value)
                node = node.next
            nodes[i].append('None')
            i += 1
            head = head.nextLevel
        res = ''
        for level in nodes:
            for n in level:
                if n == None:
                    res = res[:-2] + f'--------'
                else:
                    res += f'{str(n)} -> '
            res = res[:-4] + '\n'
            
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
    test = [-20, -16, -6, -3, -2, 5, 12, 18, -8, 19]
    for t in test:
        s.insert(t)
    # for i in range(10):
    #     s.insert(random.randint(-20, 20))

    
    print(s)
