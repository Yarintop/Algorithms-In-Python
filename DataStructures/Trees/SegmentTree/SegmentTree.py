from DataStructures.Trees.SegmentTree.SegmentTreeNode import SegmentTreeNode
import random

class SegmentTree:
    def __init__(self, maxSize=20, arr=None) -> None:
        if arr:
            self.maxSize = len(arr)
        else:
            self.maxSize = maxSize
            arr = [0] * maxSize
        self.head = self.recursiveInitTree(0, self.maxSize - 1, arr)

    def recursiveInitTree(self, minRange, maxRange, arr):
        currNode = SegmentTreeNode(minRange, maxRange)
        if minRange == maxRange:
            currNode.sum = arr[minRange]
            return currNode

        mid = (minRange + maxRange) // 2

        currNode.left = self.recursiveInitTree(minRange, mid, arr)
        currNode.right = self.recursiveInitTree(mid + 1, maxRange, arr)
        
        currNode.sum = currNode.left.sum + currNode.right.sum

        return currNode

    def update(self, index, data, currNode=None):
        if currNode == None:
            currNode = self.head

        if index == currNode.minRange and index == currNode.maxRange:
            diff = data - currNode.sum
            currNode.sum = data
            return diff
        
        diff = 0

        if index >= currNode.minRange and currNode.left:
            diff += self.update(index, data, currNode.left)
        if index <= currNode.maxRange and currNode.right:
            diff += self.update(index, data, currNode.right)
            
        currNode.sum += diff
        
        return diff 

    def getSum(self, minRange, maxRange, currNode=None):
        if minRange < 0 or maxRange < 0 or minRange >= self.maxSize or maxRange >= self.maxSize:
            return None
        if currNode == None:
            currNode = self.head

        if currNode.minRange >= minRange and currNode.maxRange <= maxRange:
            return currNode.sum

        if currNode.minRange > maxRange or currNode.maxRange < minRange:
            return 0

        return self.getSum(minRange, maxRange, currNode.left) + self.getSum(minRange, maxRange, currNode.right)

if __name__ == "__main__":
    arr = []
    for i in range(10):
        arr.append(random.randint(-20, 20))
    tree1 = SegmentTree(arr=arr)
    tree2 = SegmentTree()
    
    tree1.update(6, 100)
    
    tree2.update(0, 10)
    
    print()