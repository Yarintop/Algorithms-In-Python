class SkipListNode:
    def __init__(self, value, levels) -> None:
        self.value = value
        self.nexts = [None] * levels
    
    def setNextInLevel(self, level, node):
        self.nexts[level] = node