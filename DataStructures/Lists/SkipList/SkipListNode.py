class SkipListNode:
    def __init__(self, value, level=None, node=None, width=None) -> None:
        self.value = value
        self.nextLevel = level
        self.next = node
        self.nextNodeWidth = width
    
    def setNextInLevel(self, level, node):
        self.nexts[level] = node
        
    def __str__(self):
        return self.value
    
    def __repr__(self):
        return self.__str__()