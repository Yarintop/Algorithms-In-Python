class GraphEdge:
    def __init__(self, start, end, weight = -1, directional=False) -> None:
        self.start = start
        self.end = end
        self.weight = weight
        self.directional = directional
        
    def getNodes(self):
        return (self.start, self.end)
    
    def __lt__(self, other):
        if other == None:
            return self
        if self.weight == -1:
            return other
        return self.weight < other.weight