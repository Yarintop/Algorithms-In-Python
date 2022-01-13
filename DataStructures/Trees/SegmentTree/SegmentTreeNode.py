class SegmentTreeNode:
    def __init__(self, minRange, maxRange, sum=0, left=None, right=None) -> None:
        self.sum = sum
        self.minRange = minRange
        self.maxRange = maxRange
        self.left = left
        self.right = right
        
